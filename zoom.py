import requests
import time
import concurrent.futures


# 可同时处理的省份列表
provinces = ['上海']
# provinces = ['北京', '天津', '上海', '重庆', '河北', '山西', '内蒙古', '辽宁', 
#             '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', 
#             '河南', '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州',
#                 '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']

# 从 URL 加载后缀
def load_suffixes(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        response.raise_for_status()  # 确保请求成功
        urls = []
        for line in response.text.splitlines():
            url = line.strip().split(',')[0]  # 只取逗号前面的部分
            urls.append(url)
        return urls
    except requests.exceptions.RequestException as e:
        print(f"Failed to load suffixes from {url}: {e}")
        return []

# 从 URL 加载 URL 对应名称
def load_url_names(url):
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        response.raise_for_status()  # 确保请求成功
        formatted_names = {}
        for line in response.text.splitlines():
            line = line.strip()  # 去除前后的空白字符
            # 检查行是否有效，包含逗号并且非空
            if line and ',' in line:
                url, name = line.split(',', 1)  # 采用split(',',1)以避免过多分割
                formatted_names[url.split('/')[-1]] = name  # 仅保留路径部分作为键
            else:
                print(f"无效行：{line}")  # 打印无效行以供调试
        return formatted_names
    except requests.exceptions.RequestException as e:
        print(f"Failed to load URL names from {url}: {e}")
        return {}

# 获取省份数据
def fetch_province_data(province):
    headers = {
        'Host': 'www.zoomeye.org',
        'Connection': 'keep-alive',
        'Cube-Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEwNWRiYmIxNTA1NiIsImVtYWlsIjoiMTkxMDQ5NjU5QHFxLmNvbSIsImV4cCI6MTczMDA1NDcyMC4wfQ.d35Goc_OgCKXKLqZxtuKgXbo7Th52Bl60jlFccGhMuQ',
        'sec-ch-ua-platform': '"Windows"',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        #'Referer': 'https://www.zoomeye.org/searchResult?q=app%3A%22udpxy+multicast+UDP-to-HTTP%22++%2Bsubdivisions%3A%22%E5%8C%97%E4%BA%AC%22&page=1&pageSize=50',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie': '__jsluid_s=7d9cc8c3315d6d4c14d336d3105edf57; token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImEwNWRiYmIxNTA1NiIsImVtYWlsIjoiMTkxMDQ5NjU5QHFxLmNvbSIsImV4cCI6MTcyOTk2MDE3Ny4wfQ.pKOL8BGZz2FuKY7SGhdEgRDWQ6oc1SXouZ0_UcDSny8',
        'If-None-Match': 'W/"be6364d336b5b8f4d112349dd5166a37d1cd7cdc"'
    }
    url = f"https://www.zoomeye.org/api/search?q=app%3A%22udpxy+multicast+UDP-to-HTTP%22++%2Bsubdivisions%3A%22{province}%22&page=1&pageSize=50&t=v4%2Bv6%2Bweb"
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code == 200:
        #print (data)
        return data  #   # 返回JSON格式的内容
    


# 提取host和port
def extract_urls(json_data):
    found_urls = []
    if 'matches' in json_data:
        for match in json_data['matches']:
            ip = match['ip']
            port = match['portinfo']['port']
            url = f"http://{ip}:{port}"
            found_urls.append(url)
    print(found_urls)
    return found_urls
# 测量下载速度
def measure_download_speed(url, name, duration=10):
    try:
       # print(f"开始测量下载速度：{url}")
        start_time = time.time()
        response = requests.get(url, stream=True, timeout=3)

        total_downloaded = 0
        for data in response.iter_content(1024 * 1024):
            total_downloaded += len(data)
            break  # 读取完1MB数据后立即结束

        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            speed = 0.0  # 超过时限则速度为0
        else:
            speed = total_downloaded / elapsed_time / 1024 / 1024  # MB/s
            print(f"测试源速度：{name} -- {url} -- {speed:.2f} MB/s")
        return name, url, speed
    except requests.exceptions.RequestException as e:
        # print(f"Failed to download {url}: {e}")
        return name, url, 0.0

# 为每个省份处理数据
def process_province(province, output_file):
    print(f"处理 {province} 数据")

    # 加载该省份的后缀和URL对应名称
    suffixes = load_suffixes(f'http://8.138.87.43:2020/%E7%BB%84%E6%92%AD/url_names_{province}.txt')
    url_names = load_url_names(f'http://8.138.87.43:2020/%E7%BB%84%E6%92%AD/url_names_{province}.txt')

    # 获取该省份的JSON数据
    json_data = fetch_province_data(province)
    found_urls = extract_urls(json_data)  # 提取URL

    usable_urls = []
    for original_url in found_urls:
        test_url = f"{original_url}/status"
        try:
            response = requests.get(test_url, timeout=2)
            if response.status_code == 200:
                print(f"发现可用URL：{test_url}")
                usable_urls.append(original_url)
        except requests.exceptions.RequestException:
            pass

    # 构建带后缀的URL
    urls = set()
    for original_url in usable_urls:
        for suffix in suffixes:
            urls.add(f"{original_url}{suffix}")

    # 并发测量下载速度
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(measure_download_speed, url, url_names.get(url.split('/')[-1], "Unknown")): url for url in urls}

        for future in concurrent.futures.as_completed(future_to_url):
            result = future.result()
            results.append(result)

    # 将结果按name排序
    sorted_results = sorted(results, key=lambda x: x[0])

    # 处理完一个省份，立即写入文件
    with open(output_file, "a", encoding='utf-8') as file:  # 以追加模式打开文件
        file.write(f"\n#{province},#genre#\n")  # 写入省份名称作为区分
        for name, url, speed in sorted_results:
            if speed > 0:
                file.write(f"{name},{url} -- {speed:.2f} MB/s\n")

def main():
    output_file = "/www/wwwroot/zhibophp/源/zoom_results.txt"
    
    # 清空文件内容（如果文件存在）
    open(output_file, "w").close()

    # 顺序处理每个省份的数据
    # for province in provinces:
    #     process_province(province, output_file)

    # 并发处理每个省份的数据，但每个请求间隔1秒
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # with concurrent.futures.ThreadPoolExecutor() as executor:
        
        futures = []
        for province in provinces:
            futures.append(executor.submit(process_province, province, output_file))
            time.sleep(5)  # 在每个任务提交前延迟1秒

        
    # 等待所有任务完成
    concurrent.futures.wait(futures)

    print(f"所有省份数据处理完成，结果写入 {output_file}")

if __name__ == "__main__":
    main()

import requests
import time
import concurrent.futures

# 基础的POST请求和Headers
url = 'https://quake.360.net/api/search/query_string/quake_service'
headers = {
    'Host': 'quake.360.net',
    'Connection': 'keep-alive',
    'Content-Length': '514',
    'sec-ch-ua-platform': '"Windows"',
    'Authorization': '233',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'Origin': 'https://quake.360.net',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://quake.360.net/quake/',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': '__guid=261090063.613249672348867000.1716045888585.0752; Qs_lvt_347988=1716045889%2C1727758734; Qs_pv_347988=232592375406089440%2C2694674839023988700; Q=u%3DMBJ_1990%26n%3DMBJ_1990%26le%3DZGxkZQD5AwH5WGDjpKRhL29g%26m%3DZGZ2WGWOWGWOWGWOWGWOWGWOZmL0%26qid%3D30236351%26im%3D1_t0179f90761614136d3%26src%3Dpcw_pinpaizhongxin%26t%3D1; __NS_Q=u%3DMBJ_1990%26n%3DMBJ_1990%26le%3DZGxkZQD5AwH5WGDjpKRhL29g%26m%3DZGZ2WGWOWGWOWGWOWGWOWGWOZmL0%26qid%3D30236351%26im%3D1_t0179f90761614136d3%26src%3Dpcw_pinpaizhongxin%26t%3D1; cert_common=e76bf9d9-bc20-4a98-9f03-cfa370f72aa6; Qs_lvt_357693=1722167193%2C1722308122%2C1722398281%2C1722586464%2C1727758821; T=s%3D29492d3a3c509a1c3dcc142fd0e674b1%26t%3D1727758879%26lm%3D2-1%26lf%3D2%26sk%3D35b1f48167d1fa49a753a56e5926741d%26mt%3D1727758879%26rc%3D%26v%3D2.0%26a%3D1; __NS_T=s%3D29492d3a3c509a1c3dcc142fd0e674b1%26t%3D1727758879%26lm%3D2-1%26lf%3D2%26sk%3D35b1f48167d1fa49a753a56e5926741d%26mt%3D1727758879%26rc%3D%26v%3D2.0%26a%3D1; Qs_pv_357693=85128068538245360%2C1354647596654044700%2C4278164041916076000%2C602192517421148700%2C2674543313704729000'
}

# 可同时处理的省份列表
provinces = ['北京', '天津', '上海', '重庆', '河北', '山西', '内蒙古', '辽宁', 
            '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', 
            '河南', '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州',
                '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']


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
    try:
        data = {
            "latest": True,
            "ignore_cache": False,
            "shortcuts": [],
            "query": f'octet-stream AND UDPXY AND province: "{province}"',
            "start": 0,
            "size": 80,
            "device": {
                "device_type": "PC",
                "os": "Windows",
                "os_version": "10.0",
                "language": "zh_CN",
                "network": "3g",
                "browser_info": "Chrome（版本: 129.0.0.0&nbsp;&nbsp;内核: Blink）",
                "fingerprint": "8bafb7e3",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
                "date": "2024/10/1 13:56:9",
                "UUID": "1e73b161-af08-599f-ba85-751613b5bb7e"
            }
        }
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # 确保请求成功
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for {province}: {e}")
        return None

# 提取host和port
def extract_urls(json_data):
    found_urls = []
    for item in json_data.get('data', []):
        # 检查 'service' 和 'http' 键是否存在
        if 'service' in item and 'http' in item['service']:
            host = item['service']['http'].get('host')  # 使用 get 方法避免 KeyError
            port = item.get('port')  # 直接获取 port
            if host and port:  # 确保 host 和 port 不为空
                found_urls.append(f"{host}:{port}")
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
        return name, url, speed
    except requests.exceptions.RequestException as e:
        #print(f"Failed to download {url}: {e}")
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
        test_url = f"http://{original_url}/status"
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
            urls.add(f"http://{original_url}{suffix}")

    # 并发测量下载速度
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
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
    output_file = "results.txt"
    
    # 清空文件内容（如果文件存在）
    open(output_file, "w").close()

    # 顺序处理每个省份的数据
    #for province in provinces:
    #    process_province(province, output_file)

    # 并发处理每个省份的数据
    with concurrent.futures.ThreadPoolExecutor() as executor:
         futures = [executor.submit(process_province, province, output_file) for province in provinces]

        
    # 等待所有任务完成
    concurrent.futures.wait(futures)

    print(f"所有省份数据处理完成，结果写入 {output_file}")

if __name__ == "__main__":
    main()

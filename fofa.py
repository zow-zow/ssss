import requests
import time
import concurrent.futures
import re


# 可同时处理的省份列表
#provinces = ['广东']

provinces = ['北京', '天津', '上海', '重庆', '河北', '山西', '内蒙古', '辽宁', 
            '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', 
            '河南', '湖北', '湖南', '广东', '广西', '海南', '四川', '贵州',
                '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']

province_urls = {
    '北京' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLljJfkuqwi',
    '天津' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlpKnmtKUi',
    '上海' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLkuIrmtbci',
    '重庆' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLph43luoYi',
    '河北' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmsrPljJci',
    '山西' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlsbHopb8i',
    '内蒙古' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlhoXokpnlj6Qi',
    '辽宁' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLovr3lroEi',
    '吉林' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlkInmnpci',
    '黑龙江' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLpu5HpvpnmsZ8i',
    '江苏' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmsZ/oi48i',
    '浙江' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmtZnmsZ8i',
    '安徽' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlronlvr0i',
    '福建' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLnpo/lu7oi',
    '江西' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmsZ/opb8i',
    '山东' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlsbHkuJwi',
    '河南' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmsrPljZci',
    '湖北' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmuZbljJci',
    '湖南' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmuZbljZci',
    '广东' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlub/kuJwi',
    '广西' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlub/opb8i',
    '海南' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmtbfljZci',
    '四川' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlm5vlt50i',
    '贵州' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLotLXlt54i',
    '云南' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLkupHljZci',
    '西藏' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLopb/ol48i',
    '陕西' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLpmZXopb8i',
    '甘肃' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLnlJjogoMi',
    '青海' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLpnZLmtbci',
    '宁夏' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLlroHlpI8i',
    '新疆' : 'https://fofa.info/result?qbase64=InVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSLmlrDnloYi',
}

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
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'cookie':'isRedirectLang=1; baseShowChange=false; viewOneHundredData=false; Hm_lvt_4275507ba9b9ea6b942c7a3f7c66da90=1730436631; HMACCOUNT=4C9C4F0659A84376; _ga=GA1.1.341229638.1730436631; __fcd=7EPAVMGOI6GKFQJB5D8A0BFEDFC068A1; befor_router=%2Fresult%3Fqbase64%3DInVkcHh5IiAmJiAiQ29udGVudC1UeXBlOmFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbSIgJiYgcmVnaW9uPSJIZWJlaSI%253D; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6NDA3NTcyLCJtaWQiOjEwMDIzNDY2MiwidXNlcm5hbWUiOiJ6b3ciLCJwYXJlbnRfaWQiOjAsImV4cCI6MTczMDY5NTkyNn0.QvGjRBjUnMy_4zSMFslzGt4TXBSL_TtmzpqaN5TNcItKsuna-6eFAXz8cNqessEAy3I7a3iRQuE0iD2kxe-v5Q; user=%7B%22id%22%3A407572%2C%22mid%22%3A100234662%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22zow%22%2C%22nickname%22%3A%22zow%22%2C%22email%22%3A%22sipetas414%40vasteron.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22595cebc16b0f6c82edc7adcf8e586d9b%22%2C%22category%22%3A%22user%22%2C%22rank_avatar%22%3A%22%22%2C%22rank_level%22%3A0%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22company_name%22%3A%22zow%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%2C%22data_limit%22%3A%7B%22web_query%22%3A300%2C%22web_data%22%3A3000%2C%22api_query%22%3A0%2C%22api_data%22%3A0%2C%22data%22%3A-1%2C%22query%22%3A-1%7D%2C%22expiration_notice%22%3Afalse%2C%22remain_giveaway%22%3A0%2C%22fpoint_upgrade%22%3Afalse%2C%22account_status%22%3A%22%22%2C%22parents_id%22%3A0%2C%22parents_email%22%3A%22%22%2C%22parents_fpoint%22%3A0%7D; is_flag_login=1; is_mobile=pc; Hm_lpvt_4275507ba9b9ea6b942c7a3f7c66da90=1730437040; pageSize=50; _ga_9GWBD260K9=GS1.1.1730436631.1.1.1730437051.0.0.0'
   }
                # 直接获取该省份的映射URL
    url = province_urls.get(province)
    if url is None:
        print(f"未定义 {province} 的映射URL")
        return None  # 或者可以选择继续处理
    print(url)
    
    response = requests.get(url, headers=headers).content.decode('utf-8')
    data = response

    #print(data)
    # if response.status_code == 200:
    #     return data  # 返回JSON格式的内容
    return data


# 提取host和port
def extract_urls(json_data):
    found_urls = []
    
    # 使用正则表达式匹配所有target="_blank"的链接内容
    pattern = r'a href="(http[^"]+)"'

    
    # 查找所有匹配的内容
    matches = re.findall(pattern, json_data)
    #print(matches)
    
    # 将匹配到的地址添加到结果列表中
    for match in matches:
        found_urls.append(match.strip())  # 去掉前后的空白

    print(found_urls)  # 打印结果列表
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
    output_file = "fofa_results.txt"
    
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

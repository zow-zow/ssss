import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJKaWF4aW5nIg%3D%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249InpoZWppYW5nIg%3D%3D&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJKaW5odWEi&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJOaW5nYm8i&page=1&page_size=20',

    ]  # 添加更多URL

html_contents = []  # 用于存储获取到的HTML源码

# 发送GET请求，获取HTML源代码
def get_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ''  # 如果请求失败返回空字符串

# 使用并发处理来同时发送多个GET请求
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 执行并发的GET请求，并获取HTML源码
    html_contents = list(executor.map(get_html_content, urls))

# 将获取到的HTML源码组合在一起
combined_html = ' '.join(html_contents)  # 将所有HTML源码组合在一起
    # 使用正则表达式提取URL
pattern = r'http://\d+\.\d+\.\d+\.\d+:\d+'
found_urls = re.findall(pattern, combined_html)

usable_urls = []
for original_url in found_urls:
    test_url = original_url + '/status'
    try:
        test_response = requests.get(test_url, timeout=2)
        if test_response.status_code == 200:
            print(f"可用URL: {original_url}")
            usable_urls.append(original_url)
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    # 使用集合来存储提取到的URL，以确保不重复
found_urls_set = set()
for original_url in usable_urls:
        for suffix in ['/rtp/233.50.201.133:5140','/rtp/233.50.201.134:5140','/rtp/233.50.201.136:5140','/rtp/233.50.201.137:5140','/rtp/233.50.201.138:5140','/rtp/233.50.201.132:5140','/rtp/233.50.201.173:5140','/rtp/233.50.201.174:5140','/rtp/233.50.201.175:5140','/rtp/233.50.201.176:5140','/rtp/233.50.201.177:5140','/rtp/233.50.201.182:5140','/rtp/233.50.201.168:5140','/rtp/233.50.201.178:5140','/rtp/233.50.201.179:5140','/rtp/233.50.201.180:5140','/rtp/233.50.201.181:5140','/rtp/233.50.201.87:5140','/rtp/233.50.201.155:5140','/rtp/233.50.201.156:5140','/rtp/233.50.201.157:5140','/rtp/233.50.201.158:5140','/rtp/233.50.201.161:5140','/rtp/233.50.201.162:5140','/rtp/233.50.201.163:5140','/rtp/233.50.201.169:5140',]:
            new_url = original_url + suffix
            found_urls_set.add(new_url)

    # 将集合转换为列表，以便后续处理
urls = list(found_urls_set)


def measure_download_speed(url, name, duration=10):
    try:
        print(f"开始测量下载速度：{url}")
        start_time = time.time()
        response = requests.get(url, stream=True, timeout=3)  # 设置超时时间

        total_downloaded = 0  # total downloaded data in bytes
        for data in response.iter_content(1024*1024):  # read 1MB at a time
            total_downloaded += len(data)
            break  # 读取完1MB的数据后立即结束循环

        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            speed = 0.0  # 如果总时间超过10秒，赋值速度为0
        else:
            speed = total_downloaded / elapsed_time / 1024 / 1024  # speed in MB/s
        return name, url, speed  # 返回name和url
    except (requests.exceptions.RequestException, ConnectionError) as e:
        print(f"Failed to download {url}: {e}")
        return url, 0.0


def main():
    print("开始处理URL和测量下载速度")
    formatted_names = {}  # 使用字典来存储每个URL对应的名称
    for original_url in urls:
        print(f"正在处理URL: {original_url}")
        if '/udp/111.111.111.111:111' in original_url:
            formatted_names[original_url] = "模板"
        elif '/rtp/233.50.201.133:5140' in original_url:
            formatted_names[original_url] = "浙江经济生活"
        elif '/rtp/233.50.201.134:5140' in original_url:
            formatted_names[original_url] = "浙江教育"
        elif '/rtp/233.50.201.136:5140' in original_url:
            formatted_names[original_url] = "浙江民生"
        elif '/rtp/233.50.201.137:5140' in original_url:
            formatted_names[original_url] = "浙江news"
        elif '/rtp/233.50.201.138:5140' in original_url:
            formatted_names[original_url] = "浙江少儿"
        elif '/rtp/233.50.201.132:5140' in original_url:
            formatted_names[original_url] = "钱江频道"
        elif '/rtp/233.50.201.173:5140' in original_url:
            formatted_names[original_url] = "杭州1综合"
        elif '/rtp/233.50.201.174:5140' in original_url:
            formatted_names[original_url] = "杭州2明珠"
        elif '/rtp/233.50.201.175:5140' in original_url:
            formatted_names[original_url] = "杭州3生活"
        elif '/rtp/233.50.201.176:5140' in original_url:
            formatted_names[original_url] = "杭州4影视"
        elif '/rtp/233.50.201.177:5140' in original_url:
            formatted_names[original_url] = "杭州5青少"
        elif '/rtp/233.50.201.182:5140' in original_url:
            formatted_names[original_url] = "杭州导视"
        elif '/rtp/233.50.201.168:5140' in original_url:
            formatted_names[original_url] = "宁波TV1"
        elif '/rtp/233.50.201.178:5140' in original_url:
            formatted_names[original_url] = "宁波TV2"
        elif '/rtp/233.50.201.179:5140' in original_url:
            formatted_names[original_url] = "宁波TV3"
        elif '/rtp/233.50.201.180:5140' in original_url:
            formatted_names[original_url] = "宁波TV4"
        elif '/rtp/233.50.201.181:5140' in original_url:
            formatted_names[original_url] = "宁波TV5"
        elif '/rtp/233.50.201.87:5140' in original_url:
            formatted_names[original_url] = "温州新闻"
        elif '/rtp/233.50.201.155:5140' in original_url:
            formatted_names[original_url] = "衢州新闻"
        elif '/rtp/233.50.201.156:5140' in original_url:
            formatted_names[original_url] = "绍兴新闻"
        elif '/rtp/233.50.201.157:5140' in original_url:
            formatted_names[original_url] = "台州-1"
        elif '/rtp/233.50.201.158:5140' in original_url:
            formatted_names[original_url] = "湖州公共"
        elif '/rtp/233.50.201.161:5140' in original_url:
            formatted_names[original_url] = "金华新闻"
        elif '/rtp/233.50.201.162:5140' in original_url:
            formatted_names[original_url] = "丽水新闻"
        elif '/rtp/233.50.201.163:5140' in original_url:
            formatted_names[original_url] = "嘉兴新闻"
        elif '/rtp/233.50.201.169:5140' in original_url:
            formatted_names[original_url] = "桐乡新闻"







    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda url: measure_download_speed(url, formatted_names.get(url, "Unknown")), urls))

    unique_urls = set()  # 存储唯一的URL
    for result in results:
        if len(result) >= 3 and result[2] > 0:  # 检查result的长度是否至少为3
          unique_urls.add(result[0])  # 将结果按相同的 result[0] 进行存储

    # 将结果按相同的 result[0] 进行排序
    sorted_results = sorted(results, key=lambda x: x[0])

    # 在插入内容前添加标签
    with open("ziyong.txt", "a") as file:
        file.write("\n#浙江,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

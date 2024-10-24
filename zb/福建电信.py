import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJ4aWFtZW4i&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiYmIHJlZ2lvbj0iRnVqaWFuIg%3D%3D&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJGdXFpbmci&page=1&page_size=20',


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
        for suffix in ['/rtp/239.61.2.132:8708','/rtp/239.61.2.3:8012','/rtp/239.61.2.4:8018','/rtp/239.61.2.5:8024','/rtp/239.61.2.6:8030','/rtp/239.61.2.7:8036','/rtp/239.61.2.160:8948','/rtp/239.61.2.9:8048','/rtp/239.61.2.151:8894','/rtp/239.61.2.173:9026','/rtp/239.61.2.11:8060','/rtp/239.61.3.55:9848','/rtp/239.61.3.56:9854','/rtp/239.61.2.146:8864','/rtp/239.61.2.149:8882','/rtp/239.61.2.1:8000',]:
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
        elif '/rtp/239.61.3.4:9542' in original_url:
            formatted_names[original_url] = "福建综合"
        elif '/rtp/239.61.2.132:8708' in original_url:
            formatted_names[original_url] = "东南卫视"
        elif '/rtp/239.61.2.3:8012' in original_url:
            formatted_names[original_url] = "福建公共频道"
        elif '/rtp/239.61.2.4:8018' in original_url:
            formatted_names[original_url] = "福建新闻"
        elif '/rtp/239.61.2.5:8024' in original_url:
            formatted_names[original_url] = "福建电视剧"
        elif '/rtp/239.61.2.6:8030' in original_url:
            formatted_names[original_url] = "福建旅游"
        elif '/rtp/239.61.2.7:8036' in original_url:
            formatted_names[original_url] = "福建经济生活"
        elif '/rtp/239.61.2.160:8948' in original_url:
            formatted_names[original_url] = "福建体育"
        elif '/rtp/239.61.2.9:8048' in original_url:
            formatted_names[original_url] = "福建少儿"
        elif '/rtp/239.61.2.151:8894' in original_url:
            formatted_names[original_url] = "海峡卫视"
        elif '/rtp/239.61.2.173:9026' in original_url:
            formatted_names[original_url] = "福建教育频道"
        elif '/rtp/239.61.2.11:8060' in original_url:
            formatted_names[original_url] = "厦门卫视"
        elif '/rtp/239.61.3.55:9848' in original_url:
            formatted_names[original_url] = "厦门1套"
        elif '/rtp/239.61.3.56:9854' in original_url:
            formatted_names[original_url] = "厦门2套"
        elif '/rtp/239.61.2.146:8864' in original_url:
            formatted_names[original_url] = "欢笑剧场"
        elif '/rtp/239.61.2.149:8882' in original_url:
            formatted_names[original_url] = "都市剧场"
        elif '/rtp/239.61.2.1:8000' in original_url:
            formatted_names[original_url] = "福建综合"















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
        file.write("\n#福建电信,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

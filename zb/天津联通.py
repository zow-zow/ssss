import requests
import re
import time
import concurrent.futures

# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249IuWkqea0pSI%3D&page=1&page_size=20',





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
        for suffix in ['/udp/225.1.1.111:5002','/udp/225.1.1.130:5002','/udp/225.1.1.131:5002','/udp/225.1.1.149:5002','/udp/225.1.1.128:5002','/udp/225.1.1.122:5002','/udp/225.1.1.129:5002','/udp/225.1.1.125:5002','/udp/225.1.1.151:5002','/udp/225.1.2.123:5002','/udp/225.1.1.171:5002','/udp/225.1.1.172:5002','/udp/225.1.1.173:5002','/udp/225.1.1.174:5002','/udp/225.1.1.175:5002','/udp/225.1.1.176:5002','/udp/225.1.1.177:5002','/udp/225.1.1.178:5002','/udp/225.1.1.179:5002','/udp/225.1.1.180:5002','/udp/225.1.2.2:5002','/udp/225.1.2.4:5002','/udp/225.1.1.82:5002','/udp/225.1.1.110:5002','/udp/225.1.2.7:5002','/udp/225.1.2.8:5002','/udp/225.1.2.14:5002','/udp/225.1.1.156:5002','/udp/225.1.2.190:5002','/udp/225.1.1.215:5002','/udp/225.1.1.214:5002','/udp/225.1.1.213:5002','/udp/225.1.2.83:5002','/udp/225.1.1.217:5002','/udp/225.1.1.222:5002',]:
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
        if '/rtp/111.11.11.111:111' in original_url:
            formatted_names[original_url] = "模板"
        elif '/udp/225.1.1.111:5002' in original_url:
            formatted_names[original_url] = "天津卫视"
        elif '/udp/225.1.1.130:5002' in original_url:
            formatted_names[original_url] = "天津新闻"
        elif '/udp/225.1.1.131:5002' in original_url:
            formatted_names[original_url] = "天津文艺"
        elif '/udp/225.1.1.149:5002' in original_url:
            formatted_names[original_url] = "天津影视"
        elif '/udp/225.1.1.128:5002' in original_url:
            formatted_names[original_url] = "天津都市"
        elif '/udp/225.1.1.122:5002' in original_url:
            formatted_names[original_url] = "天津体育"
        elif '/udp/225.1.1.129:5002' in original_url:
            formatted_names[original_url] = "天津科教"
        elif '/udp/225.1.1.125:5002' in original_url:
            formatted_names[original_url] = "天津少儿"
        elif '/udp/225.1.1.151:5002' in original_url:
            formatted_names[original_url] = "天津购物"
        elif '/udp/225.1.2.123:5002' in original_url:
            formatted_names[original_url] = "天津IPTV"
        elif '/udp/225.1.1.171:5002' in original_url:
            formatted_names[original_url] = "天津文艺广播"
        elif '/udp/225.1.1.172:5002' in original_url:
            formatted_names[original_url] = "天津经济广播"
        elif '/udp/225.1.1.173:5002' in original_url:
            formatted_names[original_url] = "天津新闻广播"
        elif '/udp/225.1.1.174:5002' in original_url:
            formatted_names[original_url] = "天津生活广播"
        elif '/udp/225.1.1.175:5002' in original_url:
            formatted_names[original_url] = "天津交通广播"
        elif '/udp/225.1.1.176:5002' in original_url:
            formatted_names[original_url] = "天津相声广播"
        elif '/udp/225.1.1.177:5002' in original_url:
            formatted_names[original_url] = "天津小说广播"
        elif '/udp/225.1.1.178:5002' in original_url:
            formatted_names[original_url] = "天津滨海广播"
        elif '/udp/225.1.1.179:5002' in original_url:
            formatted_names[original_url] = "天津音乐广播"
        elif '/udp/225.1.1.180:5002' in original_url:
            formatted_names[original_url] = "天津农村广播"
        elif '/udp/225.1.2.2:5002' in original_url:
            formatted_names[original_url] = "河东卫视"
        elif '/udp/225.1.2.4:5002' in original_url:
            formatted_names[original_url] = "河西卫视"
        elif '/udp/225.1.1.82:5002' in original_url:
            formatted_names[original_url] = "蓟州卫视"
        elif '/udp/225.1.1.110:5002' in original_url:
            formatted_names[original_url] = "静海卫视"
        elif '/udp/225.1.2.7:5002' in original_url:
            formatted_names[original_url] = "滨海1"
        elif '/udp/225.1.2.8:5002' in original_url:
            formatted_names[original_url] = "滨海2"
        elif '/udp/225.1.2.14:5002' in original_url:
            formatted_names[original_url] = "大港油田企业"
        elif '/udp/225.1.1.156:5002' in original_url:
            formatted_names[original_url] = "4K私享家"
        elif '/udp/225.1.2.190:5002' in original_url:
            formatted_names[original_url] = "4K影视"
        elif '/udp/225.1.1.215:5002' in original_url:
            formatted_names[original_url] = "CHC动作电影"
        elif '/udp/225.1.1.214:5002' in original_url:
            formatted_names[original_url] = "CHC高清电影"
        elif '/udp/225.1.1.213:5002' in original_url:
            formatted_names[original_url] = "CHC家庭影院"
        elif '/udp/225.1.2.83:5002' in original_url:
            formatted_names[original_url] = "FTV足球"
        elif '/udp/225.1.1.217:5002' in original_url:
            formatted_names[original_url] = "GTV网络棋牌"
        elif '/udp/225.1.1.222:5002' in original_url:
            formatted_names[original_url] = "GTV游戏竞技"






         

           



          

                    








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
        file.write("\n#天津,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

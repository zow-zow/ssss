import requests
import re
import time
import concurrent.futures


        
# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249InNoYW5naGFpIg%3D%3D&page=1&page_size=20',





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
        for suffix in ['/udp/239.45.3.209:5140','/udp/239.45.3.146:5140','/udp/239.45.3.236:5140','/udp/239.45.3.212:5140','/udp/239.45.3.237:5140','/udp/239.45.3.211:5140','/udp/239.45.3.210:5140','/udp/239.45.1.55:5140','/udp/239.45.1.127:5140','/udp/239.45.3.136:5140','/udp/239.45.3.196:5140','/udp/239.45.1.4:5140','/udp/239.45.3.135:5140','/udp/239.45.3.134:5140','/udp/239.45.3.132:5140','/udp/239.45.3.131:5140','/udp/239.45.3.49:5140','/udp/239.45.3.122:5140','/udp/239.45.1.119:5140','/udp/239.45.1.46:5140','/udp/239.45.3.248:5140','/udp/239.45.1.54:5140','/udp/239.45.3.185:5140','/udp/239.45.1.118:5140','/udp/239.45.3.214:5140','/udp/239.45.3.139:5140','/udp/239.45.1.42:5140','/udp/239.45.3.107:5140','/udp/239.45.0.16:5140',]:
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
        elif '/udp/239.45.3.209:5140' in original_url:
            formatted_names[original_url] = "上海新闻综合"
        elif '/udp/239.45.3.146:5140' in original_url:
            formatted_names[original_url] = "上海东方卫视"
        elif '/udp/239.45.3.236:5140' in original_url:
            formatted_names[original_url] = "上海都市频道"
        elif '/udp/239.45.3.212:5140' in original_url:
            formatted_names[original_url] = "上海纪实人文"
        elif '/udp/239.45.3.237:5140' in original_url:
            formatted_names[original_url] = "东方影视"
        elif '/udp/239.45.3.211:5140' in original_url:
            formatted_names[original_url] = "上海第一财经"
        elif '/udp/239.45.3.210:5140' in original_url:
            formatted_names[original_url] = "五星体育"
        elif '/udp/239.45.1.55:5140' in original_url:
            formatted_names[original_url] = "哈哈炫动"
        elif '/udp/239.45.1.127:5140' in original_url:
            formatted_names[original_url] = "上视外语"
        elif '/udp/239.45.3.136:5140' in original_url:
            formatted_names[original_url] = "都市剧场"
        elif '/udp/239.45.3.196:5140' in original_url:
            formatted_names[original_url] = "欢笑剧场"
        elif '/udp/239.45.1.4:5140' in original_url:
            formatted_names[original_url] = "欢笑剧场（备）"
        elif '/udp/239.45.3.135:5140' in original_url:
            formatted_names[original_url] = "全纪实"
        elif '/udp/239.45.3.134:5140' in original_url:
            formatted_names[original_url] = "动漫秀场"
        elif '/udp/239.45.3.132:5140' in original_url:
            formatted_names[original_url] = "生活时尚"
        elif '/udp/239.45.3.131:5140' in original_url:
            formatted_names[original_url] = "游戏风云"
        elif '/udp/239.45.3.49:5140' in original_url:
            formatted_names[original_url] = "MAX极速汽车"
        elif '/udp/239.45.3.122:5140' in original_url:
            formatted_names[original_url] = "教育台"
        elif '/udp/239.45.1.119:5140' in original_url:
            formatted_names[original_url] = "东方财经"
        elif '/udp/239.45.0.16:5140' in original_url:
            formatted_names[original_url] = "七彩戏剧"
        elif '/udp/239.45.1.46:5140' in original_url:
            formatted_names[original_url] = "法治天地"
        elif '/udp/239.45.3.248:5140' in original_url:
            formatted_names[original_url] = "浦东频道"
        elif '/udp/239.45.1.54:5140' in original_url:
            formatted_names[original_url] = "崇明电视"
        elif '/udp/239.45.3.185:5140' in original_url:
            formatted_names[original_url] = "嘉定频道"
        elif '/udp/239.45.1.118:5140' in original_url:
            formatted_names[original_url] = "金色频道"
        elif '/udp/239.45.3.214:5140' in original_url:
            formatted_names[original_url] = "健康人生"
        elif '/udp/239.45.3.139:5140' in original_url:
            formatted_names[original_url] = "百事通超级体育"
        elif '/udp/239.45.1.42:5140' in original_url:
            formatted_names[original_url] = "百事通4K"
        elif '/udp/239.45.3.107:5140' in original_url:
            formatted_names[original_url] = "百事通4K（备）"






         

           



          

                    








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
        file.write("\n#上海,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

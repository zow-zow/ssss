import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJ4aW56aG91Ig%3D%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249InNoYW54aSI%3D&page=1&page_size=20',

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
        for suffix in ['/rtp/226.0.2.235:9792','/rtp/226.0.2.236:9800','/rtp/226.0.2.237:9808','/rtp/226.0.2.238:9816','/rtp/226.0.2.16:8040','/rtp/226.0.2.11:8000','/rtp/226.0.2.12:8008','/rtp/226.0.2.13:8016','/rtp/226.0.2.14:8024','/rtp/226.0.2.15:8032','/rtp/226.0.2.185:9392','/rtp/226.0.2.186:9400','/rtp/226.0.2.188:9416','/rtp/226.0.2.189:9424','/rtp/226.0.2.190:9432','/rtp/226.0.2.191:9440','/rtp/226.0.2.192:9448','/rtp/226.0.2.196:9480','/rtp/226.0.2.201:9520','/rtp/226.0.2.202:9528','/rtp/226.0.2.203:9536','/rtp/226.0.2.204:9544','/rtp/226.0.2.205:9552','/rtp/226.0.2.206:9560','/rtp/226.0.2.232:9772','/rtp/226.0.2.233:9776','/rtp/226.0.2.234:9784','/rtp/239.1.1.111:8111',]:
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
        elif '/rtp/226.0.2.235:9792' in original_url:            
            formatted_names[original_url] = "山西黄河HD"
        elif '/rtp/226.0.2.236:9800' in original_url:
            formatted_names[original_url] = "山西经济与科技HD"
        elif '/rtp/226.0.2.237:9808' in original_url:
            formatted_names[original_url] = "山西影视HD"
        elif '/rtp/226.0.2.238:9816' in original_url:
            formatted_names[original_url] = "山西社会与法治HD"
        elif '/rtp/226.0.2.16:8040' in original_url:
            formatted_names[original_url] = "山西文体生活HD"
        elif '/rtp/226.0.2.11:8000' in original_url:
            formatted_names[original_url] = "山西卫视"
        elif '/rtp/226.0.2.12:8008' in original_url:
            formatted_names[original_url] = "山西黄河"
        elif '/rtp/226.0.2.13:8016' in original_url:
            formatted_names[original_url] = "山西经济与科技"
        elif '/rtp/226.0.2.14:8024' in original_url:
            formatted_names[original_url] = "山西影视"
        elif '/rtp/226.0.2.15:8032' in original_url:
            formatted_names[original_url] = "山西社会与法治"
        elif '/rtp/226.0.2.185:9392' in original_url:
            formatted_names[original_url] = "朔州-1"
        elif '/rtp/226.0.2.186:9400' in original_url:
            formatted_names[original_url] = "朔州-2"
        elif '/rtp/226.0.2.188:9416' in original_url:
            formatted_names[original_url] = "东南卫视HD"
        elif '/rtp/226.0.2.189:9424' in original_url:
            formatted_names[original_url] = "孝义电视台"
        elif '/rtp/226.0.2.190:9432' in original_url:
            formatted_names[original_url] = "山西文体生活"
        elif '/rtp/226.0.2.191:9440' in original_url:
            formatted_names[original_url] = "清徐HD"
        elif '/rtp/226.0.2.192:9448' in original_url:
            formatted_names[original_url] = "古交电视台"
        elif '/rtp/226.0.2.196:9480' in original_url:
            formatted_names[original_url] = "阳曲"
        elif '/rtp/226.0.2.201:9520' in original_url:
            formatted_names[original_url] = "太原1"
        elif '/rtp/226.0.2.202:9528' in original_url:
            formatted_names[original_url] = "太原2"
        elif '/rtp/226.0.2.203:9536' in original_url:
            formatted_names[original_url] = "太原3"
        elif '/rtp/226.0.2.204:9544' in original_url:
            formatted_names[original_url] = "太原4"
        elif '/rtp/226.0.2.205:9552' in original_url:
            formatted_names[original_url] = "太原5"
        elif '/rtp/226.0.2.206:9560' in original_url:
            formatted_names[original_url] = "太原教育"
        elif '/rtp/226.0.2.232:9772' in original_url:
            formatted_names[original_url] = "大同教育HD"
        elif '/rtp/226.0.2.233:9776' in original_url:
            formatted_names[original_url] = "阳泉-1新闻综合"
        elif '/rtp/226.0.2.234:9784' in original_url:
            formatted_names[original_url] = "阳泉-2科教" 
        elif '/rtp/239.1.1.111:8111' in original_url:
            formatted_names[original_url] = "四海钓鱼"








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
        file.write("\n#山西,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

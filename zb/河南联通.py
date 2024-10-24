import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249IkhlbmFuIg%3D%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJuYW55YW5nIg%3D%3D&page=1&page_size=20', 


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
        for suffix in ['/rtp/225.1.4.98:1127','/rtp/225.1.4.52:1081','/rtp/225.1.4.53:1082','/rtp/225.1.4.54:1083','/rtp/225.1.4.55:1084','/rtp/225.1.4.56:1085','/rtp/225.1.4.57:1086','/rtp/225.1.4.58:1087','/rtp/225.1.4.120:1149','/rtp/225.1.4.102:1131','/rtp/225.1.4.163:1203','/rtp/225.1.4.206:1254','/rtp/225.1.4.100:1129','/rtp/225.1.4.99:1128','/rtp/225.1.4.101:1130','/rtp/225.1.4.132:1168','/rtp/225.1.4.133:1169','/rtp/225.1.4.136:1172','/rtp/225.1.5.28:1340','/rtp/225.1.5.29:1341','/rtp/225.1.4.196:1311','/rtp/225.1.4.236:1282','/rtp/225.1.4.194:1244','/rtp/225.1.4.254:1300',]:
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
        if '/rtp/239.16.20.165:11650' in original_url:
            formatted_names[original_url] = "河南民生"
        elif '/rtp/225.1.4.98:1127' in original_url:
            formatted_names[original_url] = "河南卫视高清"
        elif '/rtp/225.1.4.52:1081' in original_url:
            formatted_names[original_url] = "河南都市频道高清"
        elif '/rtp/225.1.4.53:1082' in original_url:
            formatted_names[original_url] = "河南民生频道"
        elif '/rtp/225.1.4.54:1083' in original_url:
            formatted_names[original_url] = "河南法治频道"
        elif '/rtp/225.1.4.55:1084' in original_url:
            formatted_names[original_url] = "河南电视剧频道高清"
        elif '/rtp/225.1.4.56:1085' in original_url:
            formatted_names[original_url] = "河南新闻频道"
        elif '/rtp/225.1.4.57:1086' in original_url:
            formatted_names[original_url] = "河南欢腾购物"
        elif '/rtp/225.1.4.58:1087' in original_url:
            formatted_names[original_url] = "河南公共频道高清"
        elif '/rtp/225.1.4.120:1149' in original_url:
            formatted_names[original_url] = "河南乡村频道"
        elif '/rtp/225.1.4.102:1131' in original_url:
            formatted_names[original_url] = "河南国际频道"
        elif '/rtp/225.1.4.163:1203' in original_url:
            formatted_names[original_url] = "睛彩中原"
        elif '/rtp/225.1.4.206:1254' in original_url:
            formatted_names[original_url] = "移动戏曲"
        elif '/rtp/225.1.4.100:1129' in original_url:
            formatted_names[original_url] = "河南文物宝库"
        elif '/rtp/225.1.4.99:1128' in original_url:
            formatted_names[original_url] = "河南梨园频道"
        elif '/rtp/225.1.4.101:1130' in original_url:
            formatted_names[original_url] = "河南武术世界"
        elif '/rtp/225.1.4.132:1168' in original_url:
            formatted_names[original_url] = "驻马店新闻综合"
        elif '/rtp/225.1.4.133:1169' in original_url:
            formatted_names[original_url] = "驻马店科教频道"
        elif '/rtp/225.1.4.136:1172' in original_url:
            formatted_names[original_url] = "驻马店公共频道"
        elif '/rtp/225.1.5.28:1340' in original_url:
            formatted_names[original_url] = "西平电视台"
        elif '/rtp/225.1.5.29:1341' in original_url:
            formatted_names[original_url] = "新蔡电视台"
        elif '/rtp/225.1.4.196:1311' in original_url:
            formatted_names[original_url] = "国学频道"
        elif '/rtp/225.1.4.236:1282' in original_url:
            formatted_names[original_url] = "欢腾购物"
        elif '/rtp/225.1.4.194:1244' in original_url:
            formatted_names[original_url] = "河南IPTV-导视"
        elif '/rtp/225.1.4.254:1300' in original_url:
            formatted_names[original_url] = "河南卫视4K"

         

           



          

                    








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
        file.write("\n#河南,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")
if __name__ == "__main__":
    main()

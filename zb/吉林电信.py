import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249ImppbGluIg%3D%3D&page=1&page_size=20', 

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
        for suffix in ['/rtp/239.37.0.096:5540','/rtp/239.37.0.097:5540','/rtp/239.37.0.098:5540','/rtp/239.37.0.099:5540','/rtp/239.37.0.100:5540','/rtp/239.37.0.101:5540','/rtp/239.37.0.102:5540','/rtp/239.37.0.104:5540','/rtp/239.37.0.103:5540','/rtp/239.37.0.106:5540','/rtp/239.37.0.105:5540','/rtp/239.37.0.107:5540','/rtp/239.37.0.108:5540','/rtp/239.37.0.109:5540','/rtp/239.37.0.125:5540','/rtp/239.37.0.126:5540','/rtp/239.37.0.144:5540','/rtp/239.37.0.180:5540','/rtp/239.37.0.110:5540','/rtp/239.37.0.113:5540','/rtp/239.37.0.116:5540','/rtp/239.37.0.128:5540','/rtp/239.37.0.129:5540','/rtp/239.37.0.127:5540','/rtp/239.37.0.130:5540','/rtp/239.37.0.132:5540','/rtp/239.37.0.131:5540','/rtp/239.37.0.133:5540','/rtp/239.37.0.134:5540','/rtp/239.37.0.136:5540','/rtp/239.37.0.135:5540','/rtp/239.37.0.138:5540','/rtp/239.37.0.137:5540','/rtp/239.37.0.145:5540','/rtp/239.37.0.164:5540','/rtp/239.37.0.166:5540','/rtp/239.37.0.168:5540','/rtp/239.37.0.167:5540','/rtp/239.37.0.170:5540','/rtp/239.37.0.169:5540','/rtp/239.37.0.172:5540','/rtp/239.37.0.171:5540','/rtp/239.37.0.174:5540','/rtp/239.37.0.173:5540','/rtp/239.37.0.175:5540','/rtp/239.37.0.177:5540','/rtp/239.37.0.179:5540','/rtp/239.37.0.181:5540','/rtp/239.37.0.205:5540','/rtp/239.37.0.206:5540','/rtp/239.37.0.207:5540','/rtp/239.37.0.208:5540','/rtp/239.37.0.209:5540','/rtp/239.37.0.210:5540','/rtp/239.37.0.211:5540','/rtp/239.37.0.212:5540','/rtp/239.37.0.213:5540','/rtp/239.37.0.214:5540','/rtp/239.37.0.216:5540','/rtp/239.37.0.217:5540','/rtp/239.37.0.220:5540','/rtp/239.37.0.225:5540','/rtp/239.37.0.227:5540','/rtp/239.37.0.228:5540','/rtp/239.37.0.246:5540','/rtp/239.37.0.248:5540','/rtp/239.37.0.249:5540','/rtp/239.37.0.247:5540','/rtp/239.37.0.250:5540','/rtp/239.37.0.253:5540','/rtp/239.37.0.251:5540','/rtp/239.37.0.252:5540',]:
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
        elif '/rtp/239.37.0.096:5540' in original_url:
            formatted_names[original_url] = "crt综合"
        elif '/rtp/239.37.0.097:5540' in original_url:
            formatted_names[original_url] = "crt娱乐"
        elif '/rtp/239.37.0.098:5540' in original_url:
            formatted_names[original_url] = "crt市民"
        elif '/rtp/239.37.0.099:5540' in original_url:
            formatted_names[original_url] = "crt经济"
        elif '/rtp/239.37.0.100:5540' in original_url:
            formatted_names[original_url] = "crt汽车"
        elif '/rtp/239.37.0.101:5540' in original_url:
            formatted_names[original_url] = "吉林卫视"
        elif '/rtp/239.37.0.102:5540' in original_url:
            formatted_names[original_url] = "吉林都市"
        elif '/rtp/239.37.0.104:5540' in original_url:
            formatted_names[original_url] = "吉林生活"
        elif '/rtp/239.37.0.103:5540' in original_url:
            formatted_names[original_url] = "吉林影视"
        elif '/rtp/239.37.0.106:5540' in original_url:
            formatted_names[original_url] = "吉林公共新闻"
        elif '/rtp/239.37.0.105:5540' in original_url:
            formatted_names[original_url] = "吉林乡村"
        elif '/rtp/239.37.0.107:5540' in original_url:
            formatted_names[original_url] = "吉林7频道"
        elif '/rtp/239.37.0.108:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.109:5540' in original_url:
            formatted_names[original_url] = "东北戏曲"
        elif '/rtp/239.37.0.125:5540' in original_url:
            formatted_names[original_url] = "长影频道"
        elif '/rtp/239.37.0.126:5540' in original_url:
            formatted_names[original_url] = "吉林教育"
        elif '/rtp/239.37.0.144:5540' in original_url:
            formatted_names[original_url] = "农安综合"
        elif '/rtp/239.37.0.180:5540' in original_url:
            formatted_names[original_url] = "扶余"
        elif '/rtp/239.37.0.110:5540' in original_url:
            formatted_names[original_url] = "家有购物"
        elif '/rtp/239.37.0.113:5540' in original_url:
            formatted_names[original_url] = "老故事"
        elif '/rtp/239.37.0.116:5540' in original_url:
            formatted_names[original_url] = "延边卫视"
        elif '/rtp/239.37.0.128:5540' in original_url:
            formatted_names[original_url] = "公共"
        elif '/rtp/239.37.0.129:5540' in original_url:
            formatted_names[original_url] = "科教"
        elif '/rtp/239.37.0.127:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.130:5540' in original_url:
            formatted_names[original_url] = "四平1"
        elif '/rtp/239.37.0.132:5540' in original_url:
            formatted_names[original_url] = "TTV1"
        elif '/rtp/239.37.0.131:5540' in original_url:
            formatted_names[original_url] = "四平2"
        elif '/rtp/239.37.0.133:5540' in original_url:
            formatted_names[original_url] = "TTV2"
        elif '/rtp/239.37.0.134:5540' in original_url:
            formatted_names[original_url] = "TTV3"
        elif '/rtp/239.37.0.136:5540' in original_url:
            formatted_names[original_url] = "公共"
        elif '/rtp/239.37.0.135:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.138:5540' in original_url:
            formatted_names[original_url] = "白山公告2"
        elif '/rtp/239.37.0.137:5540' in original_url:
            formatted_names[original_url] = "新闻综合1"
        elif '/rtp/239.37.0.145:5540' in original_url:
            formatted_names[original_url] = "集安综合"
        elif '/rtp/239.37.0.164:5540' in original_url:
            formatted_names[original_url] = "磐石"
        elif '/rtp/239.37.0.166:5540' in original_url:
            formatted_names[original_url] = "图门1"
        elif '/rtp/239.37.0.168:5540' in original_url:
            formatted_names[original_url] = "梨树新闻"
        elif '/rtp/239.37.0.167:5540' in original_url:
            formatted_names[original_url] = "tv1"
        elif '/rtp/239.37.0.170:5540' in original_url:
            formatted_names[original_url] = "综合纪实"
        elif '/rtp/239.37.0.169:5540' in original_url:
            formatted_names[original_url] = "双辽"
        elif '/rtp/239.37.0.172:5540' in original_url:
            formatted_names[original_url] = "综合"
        elif '/rtp/239.37.0.171:5540' in original_url:
            formatted_names[original_url] = "二人转"
        elif '/rtp/239.37.0.174:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.173:5540' in original_url:
            formatted_names[original_url] = "梅河口"
        elif '/rtp/239.37.0.175:5540' in original_url:
            formatted_names[original_url] = "看不清综合"
        elif '/rtp/239.37.0.177:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.179:5540' in original_url:
            formatted_names[original_url] = "DFTV综合"
        elif '/rtp/239.37.0.181:5540' in original_url:
            formatted_names[original_url] = "乾安综合"
        elif '/rtp/239.37.0.205:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.206:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.207:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.208:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.209:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.210:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.211:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.212:5540' in original_url:
            formatted_names[original_url] = "吉智聚视"
        elif '/rtp/239.37.0.213:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.214:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.216:5540' in original_url:
            formatted_names[original_url] = "吉林篮球"
        elif '/rtp/239.37.0.217:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.220:5540' in original_url:
            formatted_names[original_url] = "星"
        elif '/rtp/239.37.0.225:5540' in original_url:
            formatted_names[original_url] = "体育"
        elif '/rtp/239.37.0.227:5540' in original_url:
            formatted_names[original_url] = "体育"
        elif '/rtp/239.37.0.228:5540' in original_url:
            formatted_names[original_url] = "体育"
        elif '/rtp/239.37.0.246:5540' in original_url:
            formatted_names[original_url] = "松原"
        elif '/rtp/239.37.0.248:5540' in original_url:
            formatted_names[original_url] = "YBTV1"
        elif '/rtp/239.37.0.249:5540' in original_url:
            formatted_names[original_url] = "YBTV2"
        elif '/rtp/239.37.0.247:5540' in original_url:
            formatted_names[original_url] = "松原公共"
        elif '/rtp/239.37.0.250:5540' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.37.0.253:5540' in original_url:
            formatted_names[original_url] = "广告购物"
        elif '/rtp/239.37.0.251:5540' in original_url:
            formatted_names[original_url] = "公共"
        elif '/rtp/239.37.0.252:5540' in original_url:
            formatted_names[original_url] = "蛟河"











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
        file.write("\n#吉林,#genre#\n")
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

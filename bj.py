import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249ImJlaWppbmci&page=1&page_size=20',





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

print(combined_html)
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
        for suffix in ['/rtp/239.3.1.241:8000','/rtp/239.3.1.159:8000','/rtp/239.3.1.158:8000','/rtp/239.3.1.242:8000','/rtp/239.3.1.116:8000','/rtp/239.3.1.117:8000','/rtp/239.3.1.118:8000','/rtp/239.3.1.115:8000','/rtp/239.3.1.189:8000','/rtp/239.3.1.120:8000','/rtp/239.3.1.121:8000','/rtp/239.3.1.243:8000','/rtp/239.3.1.235:8000','/rtp/239.3.1.236:2000','/rtp/239.3.1.249:8001','/rtp/239.3.1.250:8001','/rtp/239.3.1.111:8001','/rtp/239.3.1.94:4120','/rtp/239.3.1.212:8060','/rtp/239.3.1.58:8156','/rtp/239.3.1.114:8001','/rtp/239.3.1.71:4120','/rtp/239.3.1.95:8001','/rtp/239.3.1.112:8001','/rtp/239.3.1.100:8001','/rtp/239.3.1.113:8001','/rtp/239.3.1.238:8001','/rtp/239.3.1.102:8001','/rtp/239.3.1.163:8001','/rtp/239.3.1.221:8001','/rtp/239.3.1.154:8001','/rtp/239.3.1.187:8001','/rtp/239.3.1.96:8001','/rtp/239.3.1.125:8001','/rtp/239.3.1.126:8001','/rtp/239.3.1.127:8001','/rtp/239.3.1.128:8001','/rtp/239.3.1.75:4120','/rtp/239.3.1.76:4120','/rtp/239.3.1.68:4120','/rtp/239.3.1.80:4120','/rtp/239.3.1.69:4120','/rtp/239.3.1.85:4120','/rtp/239.3.1.147:9268','/rtp/239.3.1.77:4120','/rtp/239.3.1.67:4120','/rtp/239.3.1.83:4120','/rtp/239.3.1.81:4120','/rtp/239.3.1.79:4120','/rtp/239.3.1.90:4120','/rtp/239.3.1.87:4120','/rtp/239.3.1.86:4120','/rtp/239.3.1.73:4120','/rtp/239.3.1.72:4120','/rtp/239.3.1.78:4120',]:
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
        elif '/rtp/239.3.1.241:8000' in original_url:
            formatted_names[original_url] = "BRTV北京卫视HD"
        elif '/rtp/239.3.1.159:8000' in original_url:
            formatted_names[original_url] = "BRTV新闻HD"
        elif '/rtp/239.3.1.158:8000' in original_url:
            formatted_names[original_url] = "BRTV影视HD"
        elif '/rtp/239.3.1.242:8000' in original_url:
            formatted_names[original_url] = "BRTV文艺HD"
        elif '/rtp/239.3.1.116:8000' in original_url:
            formatted_names[original_url] = "BRTV财经HD"
        elif '/rtp/239.3.1.117:8000' in original_url:
            formatted_names[original_url] = "BRTV生活HD"
        elif '/rtp/239.3.1.118:8000' in original_url:
            formatted_names[original_url] = "BRTV青年HD"
        elif '/rtp/239.3.1.115:8000' in original_url:
            formatted_names[original_url] = "BRTV纪实科教HD"
        elif '/rtp/239.3.1.189:8000' in original_url:
            formatted_names[original_url] = "BRTV卡酷少儿HD"
        elif '/rtp/239.3.1.120:8000' in original_url:
            formatted_names[original_url] = "BRTV冬奥纪实"
        elif '/rtp/239.3.1.121:8000' in original_url:
            formatted_names[original_url] = "BRTV冬奥纪实"
        elif '/rtp/239.3.1.243:8000' in original_url:
            formatted_names[original_url] = "BRTV体育休闲"
        elif '/rtp/239.3.1.235:8000' in original_url:
            formatted_names[original_url] = "BTV国际频道"
        elif '/rtp/239.3.1.236:2000' in original_url:
            formatted_names[original_url] = "爱上4K"
        elif '/rtp/239.3.1.249:8001' in original_url:
            formatted_names[original_url] = "4K超清"
        elif '/rtp/239.3.1.250:8001' in original_url:
            formatted_names[original_url] = "淘电影HD"
        elif '/rtp/239.3.1.111:8001' in original_url:
            formatted_names[original_url] = "每日影院HD"
        elif '/rtp/239.3.1.94:4120' in original_url:
            formatted_names[original_url] = "星影"
        elif '/rtp/239.3.1.212:8060' in original_url:
            formatted_names[original_url] = "纪实人文HD"
        elif '/rtp/239.3.1.58:8156' in original_url:
            formatted_names[original_url] = "金鹰纪实HD"
        elif '/rtp/239.3.1.114:8001' in original_url:
            formatted_names[original_url] = "风尚生活HD"
        elif '/rtp/239.3.1.71:4120' in original_url:
            formatted_names[original_url] = "地理"
        elif '/rtp/239.3.1.95:8001' in original_url:
            formatted_names[original_url] = "淘剧场HD"
        elif '/rtp/239.3.1.112:8001' in original_url:
            formatted_names[original_url] = "幸福剧场HD"
        elif '/rtp/239.3.1.100:8001' in original_url:
            formatted_names[original_url] = "淘娱乐HD"
        elif '/rtp/239.3.1.113:8001' in original_url:
            formatted_names[original_url] = "幸福娱乐HD"
        elif '/rtp/239.3.1.238:8001' in original_url:
            formatted_names[original_url] = "淘BabyHD"
        elif '/rtp/239.3.1.102:8001' in original_url:
            formatted_names[original_url] = "萌宠TVHD"
        elif '/rtp/239.3.1.163:8001' in original_url:
            formatted_names[original_url] = "朝阳融媒HD"
        elif '/rtp/239.3.1.221:8001' in original_url:
            formatted_names[original_url] = "通州融媒HD"
        elif '/rtp/239.3.1.154:8001' in original_url:
            formatted_names[original_url] = "密云电视台HD"
        elif '/rtp/239.3.1.187:8001' in original_url:
            formatted_names[original_url] = "延庆电视台"
        elif '/rtp/239.3.1.96:8001' in original_url:
            formatted_names[original_url] = "房山电视台"
        elif '/rtp/239.3.1.125:8001' in original_url:
            formatted_names[original_url] = "睛彩竞技HD"
        elif '/rtp/239.3.1.126:8001' in original_url:
            formatted_names[original_url] = "睛彩篮球HD"
        elif '/rtp/239.3.1.127:8001' in original_url:
            formatted_names[original_url] = "睛彩羽毛球HD"
        elif '/rtp/239.3.1.128:8001' in original_url:
            formatted_names[original_url] = "睛彩广场舞HD"
        elif '/rtp/239.3.1.75:4120' in original_url:
            formatted_names[original_url] = "解密"
        elif '/rtp/239.3.1.76:4120' in original_url:
            formatted_names[original_url] = "军事"
        elif '/rtp/239.3.1.68:4120' in original_url:
            formatted_names[original_url] = "军旅剧场"
        elif '/rtp/239.3.1.80:4120' in original_url:
            formatted_names[original_url] = "动画"
        elif '/rtp/239.3.1.69:4120' in original_url:
            formatted_names[original_url] = "古装剧场"
        elif '/rtp/239.3.1.85:4120' in original_url:
            formatted_names[original_url] = "台球"
        elif '/rtp/239.3.1.147:9268' in original_url:
            formatted_names[original_url] = "嘉佳卡通"
        elif '/rtp/239.3.1.77:4120' in original_url:
            formatted_names[original_url] = "国学"
        elif '/rtp/239.3.1.67:4120' in original_url:
            formatted_names[original_url] = "城市剧场"
        elif '/rtp/239.3.1.83:4120' in original_url:
            formatted_names[original_url] = "墨宝"
        elif '/rtp/239.3.1.81:4120' in original_url:
            formatted_names[original_url] = "好学生"
        elif '/rtp/239.3.1.79:4120' in original_url:
            formatted_names[original_url] = "早教"
        elif '/rtp/239.3.1.90:4120' in original_url:
            formatted_names[original_url] = "武侠剧场"
        elif '/rtp/239.3.1.87:4120' in original_url:
            formatted_names[original_url] = "武术"
        elif '/rtp/239.3.1.86:4120' in original_url:
            formatted_names[original_url] = "爱生活"
        elif '/rtp/239.3.1.73:4120' in original_url:
            formatted_names[original_url] = "美人"
        elif '/rtp/239.3.1.72:4120' in original_url:
            formatted_names[original_url] = "美妆"
        elif '/rtp/239.3.1.78:4120' in original_url:
            formatted_names[original_url] = "戏曲"





         

           



          

                    








    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda url: measure_download_speed(url, formatted_names.get(url, "Unknown")), urls))

    unique_urls = set()  # 存储唯一的URL
    for result in results:
        if len(result) >= 3 and result[2] > 0:  # 检查result的长度是否至少为3
          unique_urls.add(result[0])  # 将结果按相同的 result[0] 进行存储

    # 将结果按相同的 result[0] 进行排序
    sorted_results = sorted(results, key=lambda x: x[0])

    # 在插入内容前添加标签
    with open("ziyong.txt", "w") as file:
        file.write("\n#北京,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

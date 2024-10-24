import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249IuWGheiSmeWPpCI%3D&page=1&page_size=20', 
        

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
        for suffix in ['/udp/239.29.0.208:5000','/udp/239.29.0.212:5000','/udp/239.29.0.209:5000','/udp/239.29.0.211:5000','/udp/239.29.0.207:5000','/udp/239.29.0.210:5000','/udp/239.29.0.35:5000','/udp/239.29.0.36:5000','/udp/239.29.0.37:5000','/udp/239.29.0.111:5000','/udp/239.29.0.204:5000','/udp/239.29.0.112:5000','/udp/239.29.0.11:5000','/udp/239.29.0.11:5000','/udp/239.29.0.22:5000','/udp/239.29.0.23:5000','/udp/239.29.0.24:5000','/udp/239.29.0.13:5000','/udp/239.29.0.14:5000','/udp/239.29.0.15:5000','/udp/239.29.0.16:5000','/udp/239.29.0.17:5000','/udp/239.29.0.18:5000','/udp/239.29.0.41:5000','/udp/239.29.0.42:5000','/udp/239.29.0.40:5000','/udp/239.29.0.28:5000','/udp/239.29.0.29:5000','/udp/239.29.0.19:5000','/udp/239.29.0.20:5000','/udp/239.29.0.21:5000','/udp/239.29.0.25:5000','/udp/239.29.0.26:5000','/udp/239.29.0.27:5000','/udp/239.29.0.30:5000','/udp/239.29.0.31:5000','/udp/239.29.0.33:5000','/udp/239.29.0.38:5000','/udp/239.29.0.39:5000','/udp/239.29.0.190:5000','/udp/239.29.0.191:5000','/udp/239.29.0.150:5000','','','/udp/239.29.0.174:5000','/udp/239.29.0.156:5000','/udp/239.29.0.155:5000','/udp/239.29.0.149:5000','/udp/239.29.1.101:5000','/udp/239.29.1.100:5000','/udp/239.29.1.103:5000','/udp/239.29.0.148:5000','/udp/239.29.0.182:5000','/udp/239.29.1.109:5000','/udp/239.29.1.112:5000','/udp/239.29.0.184:5000','/udp/239.29.0.186:5000','/udp/239.29.0.146:5000','/udp/239.29.0.34:5000','/udp/239.29.0.177:5000','/udp/239.29.0.181:5000','/udp/239.29.0.175:5000','/udp/239.29.0.147:5000','/udp/239.29.0.180:5000','/udp/239.29.0.188:5000','/udp/239.29.0.154:5000','/udp/239.29.0.192:5000','/udp/239.29.0.178:5000','/udp/239.29.0.153:5000','/udp/239.29.0.185:5000','/udp/239.29.1.106:5000','/udp/239.29.1.150:5000','/udp/239.29.1.132:5000','/udp/239.29.0.183:5000','/udp/239.29.1.105:5000','/udp/239.29.1.105:5000','/udp/239.125.1.66:5000','/udp/239.125.1.59:5000','/udp/239.125.1.74:4120','/udp/239.125.1.72:4120','/udp/239.125.1.73:4120','/udp/239.125.1.70:4120','/udp/239.125.1.71:4120','/udp/239.125.1.69:4120','/udp/239.125.2.162:4151','/udp/239.125.2.165:4154','/udp/239.125.2.164:4153','/udp/239.125.2.163:4152',]:
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
        elif '/udp/239.29.0.208:5000' in original_url:
            formatted_names[original_url] = "内蒙古新闻"
        elif '/udp/239.29.0.212:5000' in original_url:
            formatted_names[original_url] = "内蒙古经济"
        elif '/udp/239.29.0.209:5000' in original_url:
            formatted_names[original_url] = "内蒙古农牧"
        elif '/udp/239.29.0.211:5000' in original_url:
            formatted_names[original_url] = "内蒙古文体"
        elif '/udp/239.29.0.207:5000' in original_url:
            formatted_names[original_url] = "内蒙古少儿"
        elif '/udp/239.29.0.210:5000' in original_url:
            formatted_names[original_url] = "内蒙古蒙语"
        elif '/udp/239.29.0.35:5000' in original_url:
            formatted_names[original_url] = "呼和浩特新闻"
        elif '/udp/239.29.0.36:5000' in original_url:
            formatted_names[original_url] = "呼和浩特都市"
        elif '/udp/239.29.0.37:5000' in original_url:
            formatted_names[original_url] = "呼和浩特影视"
        elif '/udp/239.29.0.111:5000' in original_url:
            formatted_names[original_url] = "包头新闻"
        elif '/udp/239.29.0.204:5000' in original_url:
            formatted_names[original_url] = "包头经济"
        elif '/udp/239.29.0.112:5000' in original_url:
            formatted_names[original_url] = "包头生活"
        elif '/udp/239.29.0.11:5000' in original_url:
            formatted_names[original_url] = "乌海新闻"
        elif '/udp/239.29.0.11:5000' in original_url:
            formatted_names[original_url] = "乌海都市"
        elif '/udp/239.29.0.22:5000' in original_url:
            formatted_names[original_url] = "乌盟新闻"
        elif '/udp/239.29.0.23:5000' in original_url:
            formatted_names[original_url] = "乌盟经济"
        elif '/udp/239.29.0.24:5000' in original_url:
            formatted_names[original_url] = "乌盟生活"
        elif '/udp/239.29.0.13:5000' in original_url:
            formatted_names[original_url] = "赤峰新闻"
        elif '/udp/239.29.0.14:5000' in original_url:
            formatted_names[original_url] = "赤峰经济"
        elif '/udp/239.29.0.15:5000' in original_url:
            formatted_names[original_url] = "赤锋影视"
        elif '/udp/239.29.0.16:5000' in original_url:
            formatted_names[original_url] = "兴安新闻"
        elif '/udp/239.29.0.17:5000' in original_url:
            formatted_names[original_url] = "兴安文化"
        elif '/udp/239.29.0.18:5000' in original_url:
            formatted_names[original_url] = "兴安影视"
        elif '/udp/239.29.0.41:5000' in original_url:
            formatted_names[original_url] = "通辽新闻"
        elif '/udp/239.29.0.42:5000' in original_url:
            formatted_names[original_url] = "通辽城市"
        elif '/udp/239.29.0.40:5000' in original_url:
            formatted_names[original_url] = "通辽蒙语"
        elif '/udp/239.29.0.28:5000' in original_url:
            formatted_names[original_url] = "阿拉善新闻"
        elif '/udp/239.29.0.29:5000' in original_url:
            formatted_names[original_url] = "阿拉善经济"
        elif '/udp/239.29.0.19:5000' in original_url:
            formatted_names[original_url] = "呼伦贝尔新闻"
        elif '/udp/239.29.0.20:5000' in original_url:
            formatted_names[original_url] = "呼伦贝尔文化"
        elif '/udp/239.29.0.21:5000' in original_url:
            formatted_names[original_url] = "呼伦贝尔生活"
        elif '/udp/239.29.0.25:5000' in original_url:
            formatted_names[original_url] = "巴彦淖尔新闻"
        elif '/udp/239.29.0.26:5000' in original_url:
            formatted_names[original_url] = "巴彦淖尔经济"
        elif '/udp/239.29.0.27:5000' in original_url:
            formatted_names[original_url] = "巴彦淖尔影视"
        elif '/udp/239.29.0.30:5000' in original_url:
            formatted_names[original_url] = "鄂尔多斯新闻"
        elif '/udp/239.29.0.31:5000' in original_url:
            formatted_names[original_url] = "鄂尔多斯经济"
        elif '/udp/239.29.0.33:5000' in original_url:
            formatted_names[original_url] = "鄂尔多斯蒙语"
        elif '/udp/239.29.0.38:5000' in original_url:
            formatted_names[original_url] = "锡林郭勒1"
        elif '/udp/239.29.0.39:5000' in original_url:
            formatted_names[original_url] = "锡林郭勒2"
        elif '/udp/239.29.0.190:5000' in original_url:
            formatted_names[original_url] = "苏尼特左旗电视"
        elif '/udp/239.29.0.191:5000' in original_url:
            formatted_names[original_url] = "苏尼特右旗电视"
        elif '/udp/239.29.0.150:5000' in original_url:
            formatted_names[original_url] = "乌拉特前旗电视"
        elif '/udp/239.29.0.152:5000' in original_url:
            formatted_names[original_url] = "乌拉特中旗电视"
        elif '/udp/239.29.0.151:5000' in original_url:
            formatted_names[original_url] = "乌拉特后旗电视"
        elif '/udp/239.29.0.174:5000' in original_url:
            formatted_names[original_url] = "突泉电视"
        elif '/udp/239.29.0.156:5000' in original_url:
            formatted_names[original_url] = "噔口电视"
        elif '/udp/239.29.0.155:5000' in original_url:
            formatted_names[original_url] = "多伦电视"
        elif '/udp/239.29.0.149:5000' in original_url:
            formatted_names[original_url] = "杭后电视"
        elif '/udp/239.29.1.101:5000' in original_url:
            formatted_names[original_url] = "达茂电视"
        elif '/udp/239.29.1.100:5000' in original_url:
            formatted_names[original_url] = "库伦电视"
        elif '/udp/239.29.1.103:5000' in original_url:
            formatted_names[original_url] = "丰镇电视"
        elif '/udp/239.29.0.148:5000' in original_url:
            formatted_names[original_url] = "五原电视"
        elif '/udp/239.29.0.182:5000' in original_url:
            formatted_names[original_url] = "武川电视"
        elif '/udp/239.29.1.109:5000' in original_url:
            formatted_names[original_url] = "扎兰屯民视"
        elif '/udp/239.29.1.112:5000' in original_url:
            formatted_names[original_url] = "阿尔山电视"
        elif '/udp/239.29.0.184:5000' in original_url:
            formatted_names[original_url] = "阿巴嘎电视"
        elif '/udp/239.29.0.186:5000' in original_url:
            formatted_names[original_url] = "翁牛特电视"
        elif '/udp/239.29.0.146:5000' in original_url:
            formatted_names[original_url] = "托克托电视"
        elif '/udp/239.29.0.34:5000' in original_url:
            formatted_names[original_url] = "满州里电视"
        elif '/udp/239.29.0.177:5000' in original_url:
            formatted_names[original_url] = "额济纳电视"
        elif '/udp/239.29.0.181:5000' in original_url:
            formatted_names[original_url] = "西乌旗电视"
        elif '/udp/239.29.0.175:5000' in original_url:
            formatted_names[original_url] = "阿右旗电视"
        elif '/udp/239.29.0.147:5000' in original_url:
            formatted_names[original_url] = "正蓝旗电视"
        elif '/udp/239.29.0.180:5000' in original_url:
            formatted_names[original_url] = "东鸟旗电视"
        elif '/udp/239.29.0.188:5000' in original_url:
            formatted_names[original_url] = "土左旗电视"
        elif '/udp/239.29.0.154:5000' in original_url:
            formatted_names[original_url] = "太仆寺旗电视"
        elif '/udp/239.29.0.192:5000' in original_url:
            formatted_names[original_url] = "准格尔旗电视"
        elif '/udp/239.29.0.178:5000' in original_url:
            formatted_names[original_url] = "科右中旗电视"
        elif '/udp/239.29.0.153:5000' in original_url:
            formatted_names[original_url] = "正镶白旗电视"
        elif '/udp/239.29.0.185:5000' in original_url:
            formatted_names[original_url] = "扎赉特旗电视"
        elif '/udp/239.29.1.106:5000' in original_url:
            formatted_names[original_url] = "察右中旗电视"
        elif '/udp/239.29.1.150:5000' in original_url:
            formatted_names[original_url] = "喀喇沁县电视"
        elif '/udp/239.29.1.132:5000' in original_url:
            formatted_names[original_url] = "额尔古纳电视"
        elif '/udp/239.29.0.183:5000' in original_url:
            formatted_names[original_url] = "和林格尔电视"
        elif '/udp/239.29.1.105:5000' in original_url:
            formatted_names[original_url] = "伊金霍洛旗电视"
        elif '/udp/239.29.1.105:5000' in original_url:
            formatted_names[original_url] = "克什克腾旗电视"
        elif '/udp/239.125.1.66:5000' in original_url:
            formatted_names[original_url] = "内蒙古蒙古语卫视"
        elif '/udp/239.125.1.59:5000' in original_url:
            formatted_names[original_url] = "内蒙古卫视"
        elif '/udp/239.125.1.74:4120' in original_url:
            formatted_names[original_url] = "内蒙古经济"
        elif '/udp/239.125.1.72:4120' in original_url:
            formatted_names[original_url] = "内蒙古文体"
        elif '/udp/239.125.1.73:4120' in original_url:
            formatted_names[original_url] = "内蒙古农牧"
        elif '/udp/239.125.1.70:4120' in original_url:
            formatted_names[original_url] = "内蒙古新闻"
        elif '/udp/239.125.1.71:4120' in original_url:
            formatted_names[original_url] = "内蒙古蒙语文化"
        elif '/udp/239.125.1.69:4120' in original_url:
            formatted_names[original_url] = "内蒙古少儿"
        elif '/udp/239.125.2.162:4151' in original_url:
            formatted_names[original_url] = "鄂尔多斯蒙古语综合"
        elif '/udp/239.125.2.165:4154' in original_url:
            formatted_names[original_url] = "鄂尔多斯新闻"
        elif '/udp/239.125.2.164:4153' in original_url:
            formatted_names[original_url] = "鄂尔多斯经济"
        elif '/udp/239.125.2.163:4152' in original_url:
            formatted_names[original_url] = "鄂尔多斯城市"


















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
        file.write("\n#内蒙古,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()
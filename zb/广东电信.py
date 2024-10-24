import requests
import re
import time
import concurrent.futures



# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJndWFuZ3pob3Ui&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249IuW5v%2BS4nCI%3D&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJodWl6aG91Ig%3D%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJaaG9uZ3NoYW4i&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJzaGVuemhlbiI%3D&page=1&page_size=20',


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
        for suffix in ['/udp/239.77.0.217:5146','/udp/239.77.0.225:5146','/udp/239.77.0.250:5146','/udp/239.77.0.173:5146','/udp/239.77.0.179:5146','/udp/239.77.0.225:5146','/udp/239.77.0.86:5146','/udp/239.77.0.137:5146','/udp/239.77.0.138:5146','/udp/239.77.0.134:5146','/udp/239.77.0.84:5146','/udp/239.77.0.85:5146','/udp/239.77.0.112:5146','/udp/239.77.0.1:5146','/udp/239.77.0.86:5146','/udp/239.77.0.87:5146','/udp/239.77.0.137:5146','/udp/239.77.0.169:5146','/udp/239.77.0.78:5146','/udp/239.77.0.170:5146','/udp/239.77.0.171:5146','/udp/239.77.0.138:5146','/udp/239.77.0.172:5146','/udp/239.77.0.135:5146','/udp/239.77.0.134:5146','/udp/239.77.1.238:5146','/udp/239.77.0.136:5146','/udp/239.77.0.133:5146','/udp/239.77.1.239:5146','/udp/239.77.0.198:5146','/udp/239.77.0.88:5146','/udp/239.77.0.89:5146','/udp/239.77.0.90:5146','/udp/239.77.0.91:5146','/udp/239.77.0.92:5146','/udp/239.77.0.93:5146','/udp/239.77.0.95:5146','/udp/239.77.0.97:5146','/udp/239.77.0.94:5146','/udp/239.77.0.98:5146','/udp/239.77.0.123:5146','/udp/239.77.0.159:5146','/udp/239.77.0.160:5146','/udp/239.77.0.182:5146','/udp/239.77.0.183:5146','/udp/239.77.0.230:5146','/udp/239.77.0.200:5146','/udp/239.77.1.249:5146','/udp/239.77.0.146:5146','/udp/239.77.0.148:5146','/udp/239.77.0.149:5146','/udp/239.77.0.150:5146','/udp/239.77.0.139:5146','/udp/239.77.0.27:5146','/udp/239.77.0.15:5146','/udp/239.77.0.145:5146','/udp/239.77.0.166:5146','/udp/239.77.0.167:5146','/udp/239.77.0.168:5146','/udp/239.77.0.114:5146','/udp/239.77.0.117:5146','/udp/239.77.0.119:5146','/udp/239.77.0.141:5146','/udp/239.77.0.154:5146','/udp/239.77.0.155:5146','/udp/239.253.43.213:5146','/udp/239.253.43.214:5146','/udp/239.253.43.6:5146','/udp/239.253.43.5:5146','/udp/239.253.43.7:5146','/udp/239.253.43.8:5146','/udp/239.253.43.9:5146','/udp/239.253.43.10:5146','/udp/239.253.43.11:5146','/udp/239.253.43.12:5146','/udp/239.253.43.13:5146','/udp/239.253.43.14:5146','/udp/239.253.43.15:5146','/udp/239.253.43.16:5146','/udp/239.253.43.1:5146','/udp/239.253.43.2:5146','/udp/239.77.1.124:5146','/udp/239.77.1.125:5146','/udp/239.77.1.126:5146','/udp/239.77.1.242:5146','/udp/239.77.1.243:5146','/udp/239.77.1.244:5146','/udp/239.77.1.232:5146','/udp/239.77.1.233:5146','/udp/239.77.1.234:5146','/udp/239.77.1.130:5146','/udp/239.77.1.131:5146','/udp/239.77.0.119:5146','/udp/239.77.0.229:5146','/udp/239.77.0.251:5146','/udp/239.77.0.25:5146','/udp/239.77.0.187:5146','/udp/239.77.0.201:5146','/udp/239.77.0.202:5146','/udp/239.77.0.203:5146','/udp/239.253.43.33:5146','/udp/239.253.43.34:5146','/udp/239.77.0.253:5146','/udp/239.77.0.254:5146','/udp/239.77.0.206:5146','/udp/239.77.0.207:5146','/udp/239.253.43.44:5146','/udp/239.77.1.132:5146','/udp/239.253.43.47:5146','/udp/239.253.43.53:5146','/udp/239.253.43.54:5146','/udp/239.253.43.55:5146','/udp/239.253.43.56:5146','/udp/239.253.43.57:5146','/udp/239.253.43.104:5146','/udp/239.253.43.105:5146','/udp/239.253.43.62:5146','/udp/239.253.43.63:5146','/udp/239.253.43.64:5146','/udp/239.253.43.112:5146','/udp/239.253.43.71:5146','/udp/239.253.43.72:5146','/udp/239.253.43.73:5146','/udp/239.253.43.74:5146','/udp/239.253.43.75:5146','/udp/239.253.43.76:5146','/udp/239.253.43.77:5146','/udp/239.253.43.78:5146','/udp/239.253.43.79:5146','/udp/239.253.43.80:5146','/udp/239.253.43.81:5146','/udp/239.253.43.89:5146','/udp/239.253.43.90:5146','/udp/239.253.43.91:5146','/udp/239.253.43.92:5146','/udp/239.253.43.93:5146','/udp/239.77.0.9:5146','/udp/239.77.0.16:5146',]:
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
        if '/udp/239.77.0.86:5146' in original_url:
            formatted_names[original_url] = "CCTV1综合高清"
        elif '/udp/239.77.0.137:5146' in original_url:
            formatted_names[original_url] = "CCTV2财经高清"
        elif '/udp/239.77.0.138:5146' in original_url:
            formatted_names[original_url] = "CCTV7军事农业高清"            
        elif '/udp/239.77.0.134:5146' in original_url:
            formatted_names[original_url] = "CCTV10科教高清"            
        elif '/udp/239.77.0.2:5146' in original_url:
            formatted_names[original_url] = "广东卫视"
        elif '/udp/239.77.0.3:5146' in original_url:
            formatted_names[original_url] = "广东珠江"
        elif '/udp/239.77.0.4:5146' in original_url:
            formatted_names[original_url] = "广东新闻"
        elif '/udp/239.77.0.5:5146' in original_url:
            formatted_names[original_url] = "广东民生"
        elif '/udp/239.77.0.6:5146' in original_url:
            formatted_names[original_url] = "广东体育"            
        elif '/udp/239.77.0.7:5146' in original_url:
            formatted_names[original_url] = "广东国际"            
        elif '/udp/239.77.0.8:5146' in original_url:
            formatted_names[original_url] = "经济科教"
        elif '/udp/239.77.0.9:5146' in original_url:
            formatted_names[original_url] = "大湾区卫视"
        elif '/udp/239.77.0.11:5146' in original_url:
            formatted_names[original_url] = "广东影视"
        elif '/udp/239.77.0.12:5146' in original_url:
            formatted_names[original_url] = "广东少儿"
        elif '/udp/239.77.0.13:5146' in original_url:
            formatted_names[original_url] = "嘉佳卡通"            
        elif '/udp/239.77.0.244:5146' in original_url:
            formatted_names[original_url] = "广东综艺(4k)"            
        elif '/udp/239.77.0.16:5146' in original_url:
            formatted_names[original_url] = "岭南戏曲"
        elif '/udp/239.77.0.14:5146' in original_url:
            formatted_names[original_url] = "广东房产"
        elif '/udp/239.77.0.18:5146' in original_url:
            formatted_names[original_url] = "现代教育"           
        elif '/udp/239.77.0.46:5146' in original_url:
            formatted_names[original_url] = "湖南卫视" 
        elif '/udp/239.77.0.47:5146' in original_url:
            formatted_names[original_url] = "浙江卫视"            
        elif '/udp/239.77.0.48:5146' in original_url:
            formatted_names[original_url] = "江苏卫视"
        elif '/udp/239.77.0.49:5146' in original_url:
            formatted_names[original_url] = "东方卫视"
        elif '/udp/239.77.0.50:5146' in original_url:
            formatted_names[original_url] = "安徽卫视"           
        elif '/udp/239.77.0.51:5146' in original_url:
            formatted_names[original_url] = "北京卫视"
        elif '/udp/239.77.0.52:5146' in original_url:
            formatted_names[original_url] = "天津卫视"
        elif '/udp/239.77.0.53:5146' in original_url:
            formatted_names[original_url] = "山东卫视" 
        elif '/udp/239.77.0.54:5146' in original_url:
            formatted_names[original_url] = "江西卫视" 
        elif '/udp/239.77.1.3:5146' in original_url:
            formatted_names[original_url] = "深圳卫视"            
        elif '/udp/239.77.0.56:5146' in original_url:
            formatted_names[original_url] = "湖北卫视"
        elif '/udp/239.77.0.57:5146' in original_url:
            formatted_names[original_url] = "辽宁卫视"
        elif '/udp/239.77.0.58:5146' in original_url:
            formatted_names[original_url] = "黑龙江卫视"           
        elif '/udp/239.77.0.59:5146' in original_url:
            formatted_names[original_url] = "贵州卫视"
        elif '/udp/239.77.0.60:5146' in original_url:
            formatted_names[original_url] = "四川卫视"
        elif '/udp/239.77.0.61:5146' in original_url:
            formatted_names[original_url] = "河南卫视" 
        elif '/udp/239.77.0.62:5146' in original_url:
            formatted_names[original_url] = "云南卫视"            
        elif '/udp/239.77.0.63:5146' in original_url:
            formatted_names[original_url] = "重庆卫视"
        elif '/udp/239.77.0.64:5146' in original_url:
            formatted_names[original_url] = "河北卫视"
        elif '/udp/239.77.0.65:5146' in original_url:
            formatted_names[original_url] = "东南卫视"           
        elif '/udp/239.77.0.66:5146' in original_url:
            formatted_names[original_url] = "广西卫视"
        elif '/udp/239.77.0.67:5146' in original_url:
            formatted_names[original_url] = "吉林卫视" 
        elif '/udp/239.77.0.68:5146' in original_url:
            formatted_names[original_url] = "陕西卫视"            
        elif '/udp/239.77.0.69:5146' in original_url:
            formatted_names[original_url] = "山西卫视"
        elif '/udp/239.77.0.70:5146' in original_url:
            formatted_names[original_url] = "内蒙古卫视"
        elif '/udp/239.77.0.71:5146' in original_url:
            formatted_names[original_url] = "青海卫视"           
        elif '/udp/239.77.0.72:5146' in original_url:
            formatted_names[original_url] = "海南卫视"
        elif '/udp/239.77.0.73:5146' in original_url:
            formatted_names[original_url] = "宁夏卫视"
        elif '/udp/239.77.0.74:5146' in original_url:
            formatted_names[original_url] = "西藏卫视" 
        elif '/udp/239.77.0.75:5146' in original_url:
            formatted_names[original_url] = "新疆卫视"            
        elif '/udp/239.77.0.76:5146' in original_url:
            formatted_names[original_url] = "甘肃卫视"
        elif '/udp/239.77.0.77:5146' in original_url:
            formatted_names[original_url] = "兵团卫视"
        elif '/udp/239.77.0.79:5146' in original_url:
            formatted_names[original_url] = "卡酷动画"           
        elif '/udp/239.77.0.80:5146' in original_url:
            formatted_names[original_url] = "金鹰卡通"
        elif '/udp/239.77.0.81:5146' in original_url:
            formatted_names[original_url] = "炫动卡通" 
        elif '/udp/239.77.0.96:5146' in original_url:
            formatted_names[original_url] = "厦门卫视"            
        elif '/udp/239.77.0.222:5146' in original_url:
            formatted_names[original_url] = "优漫卡通"
        elif '/udp/239.77.0.152:5146' in original_url:
            formatted_names[original_url] = "三沙卫视"
        elif '/udp/239.77.0.10:5146' in original_url:
            formatted_names[original_url] = "吉林延边卫视"           
        elif '/udp/239.77.0.82:5146' in original_url:
            formatted_names[original_url] = "CETV-1"
        elif '/udp/239.77.0.28:5146' in original_url:
            formatted_names[original_url] = "CETV2"
        elif '/udp/239.77.0.29:5146' in original_url:
            formatted_names[original_url] = "CETV4" 
        elif '/udp/239.77.0.84:5146' in original_url:
            formatted_names[original_url] = "广东卫视高清"            
        elif '/udp/239.77.0.85:5146' in original_url:
            formatted_names[original_url] = "经济科教高清"
        elif '/udp/239.77.0.112:5146' in original_url:
            formatted_names[original_url] = "广东体育高清"
        elif '/udp/239.77.0.1:5146' in original_url:
            formatted_names[original_url] = "广东珠江高清"           
        elif '/udp/239.77.0.215:5146' in original_url:
            formatted_names[original_url] = "大亚湾卫视高清"
        elif '/udp/239.77.0.217:5146' in original_url:
            formatted_names[original_url] = "广东影视高清"            
        elif '/udp/239.77.0.225:5146' in original_url:
            formatted_names[original_url] = "广东民生高清"
        elif '/udp/239.77.0.250:5146' in original_url:
            formatted_names[original_url] = "广东少儿高清"
        elif '/udp/239.77.0.173:5146' in original_url:
            formatted_names[original_url] = "广东新闻高清"           
        elif '/udp/239.77.0.179:5146' in original_url:
            formatted_names[original_url] = "嘉佳卡通高清"
        elif '/udp/239.77.0.86:5146' in original_url:
            formatted_names[original_url] = "CCTV1高清"
        elif '/udp/239.77.0.87:5146' in original_url:
            formatted_names[original_url] = "CCTV5＋体育高清" 
        elif '/udp/239.77.0.137:5146' in original_url:
            formatted_names[original_url] = "CCTV2高清"            
        elif '/udp/239.77.0.169:5146' in original_url:
            formatted_names[original_url] = "CCTV3高清"
        elif '/udp/239.77.0.78:5146' in original_url:
            formatted_names[original_url] = "CCTV4高清"
        elif '/udp/239.77.0.170:5146' in original_url:
            formatted_names[original_url] = "CCTV5体育"           
        elif '/udp/239.77.0.171:5146' in original_url:
            formatted_names[original_url] = "CCTV6高清"
        elif '/udp/239.77.0.138:5146' in original_url:
            formatted_names[original_url] = "CCTV7高清"            
        elif '/udp/239.77.0.172:5146' in original_url:
            formatted_names[original_url] = "CCTV8高清"
        elif '/udp/239.77.0.135:5146' in original_url:
            formatted_names[original_url] = "CCTV9高清"
        elif '/udp/239.77.0.134:5146' in original_url:
            formatted_names[original_url] = "CCTV10高清"           
        elif '/udp/239.77.1.238:5146' in original_url:
            formatted_names[original_url] = "CCTV11高清"
        elif '/udp/239.77.0.136:5146' in original_url:
            formatted_names[original_url] = "CCTV12高清"
        elif '/udp/239.77.0.188:5146' in original_url:
            formatted_names[original_url] = "CCTV13高清" 
        elif '/udp/239.77.0.133:5146' in original_url:
            formatted_names[original_url] = "CCTV14高清"            
        elif '/udp/239.77.1.239:5146' in original_url:
            formatted_names[original_url] = "CCTV15高清"
        elif '/udp/239.77.0.198:5146' in original_url:
            formatted_names[original_url] = "CCTV17农业高清"
        elif '/udp/239.77.0.199:5146' in original_url:
            formatted_names[original_url] = "CGTN英语高清"           
        elif '/udp/239.77.0.221:5146' in original_url:
            formatted_names[original_url] = "CGTN西班牙语高清"         
        elif '/udp/239.77.0.228:5146' in original_url:
            formatted_names[original_url] = "CGTN法语高清"
        elif '/udp/239.253.43.200:5146' in original_url:
            formatted_names[original_url] = "CGTN阿拉伯语高清"            
        elif '/udp/239.253.43.201:5146' in original_url:
            formatted_names[original_url] = "CGTN俄语高清"
        elif '/udp/239.77.0.88:5146' in original_url:
            formatted_names[original_url] = "湖南卫视高清"
        elif '/udp/239.77.0.89:5146' in original_url:
            formatted_names[original_url] = "浙江卫视高清"           
        elif '/udp/239.77.0.90:5146' in original_url:
            formatted_names[original_url] = "江苏卫视高清"
        elif '/udp/239.77.0.91:5146' in original_url:
            formatted_names[original_url] = "北京卫视高清"
        elif '/udp/239.77.0.92:5146' in original_url:
            formatted_names[original_url] = "深圳卫视高清" 
        elif '/udp/239.77.0.93:5146' in original_url:
            formatted_names[original_url] = "黑龙江卫视高清"            
        elif '/udp/239.77.0.95:5146' in original_url:
            formatted_names[original_url] = "湖北卫视高清"
        elif '/udp/239.77.0.97:5146' in original_url:
            formatted_names[original_url] = "天津卫视高清"
        elif '/udp/239.77.0.94:5146' in original_url:
            formatted_names[original_url] = "山东卫视高清"           
        elif '/udp/239.77.0.98:5146' in original_url:
            formatted_names[original_url] = "东方卫视高清"           
        elif '/udp/239.77.0.123:5146' in original_url:
            formatted_names[original_url] = "辽宁卫视高清"
        elif '/udp/239.77.0.159:5146' in original_url:
            formatted_names[original_url] = "四川卫视高清"            
        elif '/udp/239.77.0.160:5146' in original_url:
            formatted_names[original_url] = "金鹰纪实高清"
        elif '/udp/239.77.0.182:5146' in original_url:
            formatted_names[original_url] = "重庆卫视高清"
        elif '/udp/239.77.0.183:5146' in original_url:
            formatted_names[original_url] = "安徽卫视高清"           
        elif '/udp/239.77.0.230:5146' in original_url:
            formatted_names[original_url] = "贵州卫视高清"
        elif '/udp/239.77.0.200:5146' in original_url:
            formatted_names[original_url] = "中国教育-1高清"
        elif '/udp/239.77.1.249:5146' in original_url:
            formatted_names[original_url] = "中国交通" 
        elif '/udp/239.77.0.146:5146' in original_url:
            formatted_names[original_url] = "东南卫视高清"            
        elif '/udp/239.77.0.148:5146' in original_url:
            formatted_names[original_url] = "河北卫视高清"
        elif '/udp/239.77.0.149:5146' in original_url:
            formatted_names[original_url] = "江西卫视高清"
        elif '/udp/239.77.0.150:5146' in original_url:
            formatted_names[original_url] = "吉林卫视高清"           
        elif '/udp/239.77.0.139:5146' in original_url:
            formatted_names[original_url] = "广西卫视高清"
        elif '/udp/239.77.0.17:5146' in original_url:
            formatted_names[original_url] = "河南卫视高清"
        elif '/udp/239.77.0.27:5146' in original_url:
            formatted_names[original_url] = "CHC高清电影"
        elif '/udp/239.77.0.15:5146' in original_url:
            formatted_names[original_url] = "茶"           
        elif '/udp/239.77.0.145:5146' in original_url:
            formatted_names[original_url] = "快乐垂钓"
        elif '/udp/239.77.0.166:5146' in original_url:
            formatted_names[original_url] = "广东卫视超清"
        elif '/udp/239.77.0.167:5146' in original_url:
            formatted_names[original_url] = "经济科教超清"
        elif '/udp/239.77.0.168:5146' in original_url:
            formatted_names[original_url] = "广东体育超清"           
        elif '/udp/239.77.0.114:5146' in original_url:
            formatted_names[original_url] = "广东珠江超清"
        elif '/udp/239.253.43.9:5146' in original_url:
            formatted_names[original_url] = "兵器科技高清"
        elif '/udp/239.253.43.10:5146' in original_url:
            formatted_names[original_url] = "电视指南高清"           
        elif '/udp/239.253.43.14:5146' in original_url:
            formatted_names[original_url] = "风云足球高清"
        elif '/udp/239.253.43.11:5146' in original_url:
            formatted_names[original_url] = "央视台球高清"
        elif '/udp/239.253.43.12:5146' in original_url:
            formatted_names[original_url] = "高尔夫网球高清"
        elif '/udp/239.253.43.8:5146' in original_url:
            formatted_names[original_url] = "女性时尚高清"           
        elif '/udp/239.253.43.7:5146' in original_url:
            formatted_names[original_url] = "世界地理高清"
        elif '/udp/239.253.43.5:5146' in original_url:
            formatted_names[original_url] = "怀旧剧场高清"
        elif '/udp/239.253.43.16:5146' in original_url:
            formatted_names[original_url] = "风云剧场高清"
        elif '/udp/239.253.43.13:5146' in original_url:
            formatted_names[original_url] = "央视文化精品高清"           
        elif '/udp/239.253.43.15:5146' in original_url:
            formatted_names[original_url] = "第一剧场高清"
        elif '/udp/239.253.43.213:5146' in original_url:
            formatted_names[original_url] = "河源新闻综合高清"
        elif '/udp/239.253.43.214:5146' in original_url:
            formatted_names[original_url] = "河源公共"           
        elif '/udp/239.253.43.1:5146' in original_url:
            formatted_names[original_url] = "肇庆综合"
        elif '/udp/239.253.43.2:5146' in original_url:
            formatted_names[original_url] = "肇庆公共"
        elif '/udp/239.77.1.126:5146' in original_url:
            formatted_names[original_url] = "深圳公共频道"
        elif '/udp/239.77.1.124:5146' in original_url:
            formatted_names[original_url] = "深圳都市频道"           
        elif '/udp/239.77.1.232:5146' in original_url:
            formatted_names[original_url] = "HZTV1"
        elif '/udp/239.77.1.233:5146' in original_url:
            formatted_names[original_url] = "HZTV2"
        elif '/udp/239.77.1.244:5146' in original_url:
            formatted_names[original_url] = "深圳少儿频道"
        elif '/udp/239.77.1.243:5146' in original_url:
            formatted_names[original_url] = "深圳娱乐频道"           
        elif '/udp/239.77.1.242:5146' in original_url:
            formatted_names[original_url] = "深圳财经生活"
        elif '/udp/239.77.0.155:5146' in original_url:
            formatted_names[original_url] = "珠海1"            
        elif '/udp/239.77.0.154:5146' in original_url:
            formatted_names[original_url] = "珠海2"           
        elif '/udp/239.77.1.189:5146' in original_url:
            formatted_names[original_url] = "汕尾1"
        elif '/udp/239.77.1.190:5146' in original_url:
            formatted_names[original_url] = "汕尾2"
        elif '/udp/239.77.1.130:5146' in original_url:
            formatted_names[original_url] = "汕头综合"
        elif '/udp/239.77.1.131:5146' in original_url:
            formatted_names[original_url] = "汕头经济生活"           
        elif '/udp/239.77.0.121:5146' in original_url:
            formatted_names[original_url] = "湛江公共"
        elif '/udp/239.77.0.119:5146' in original_url:
            formatted_names[original_url] = "韶关公共"
        elif '/udp/239.77.0.117:5146' in original_url:
            formatted_names[original_url] = "韶关综合"
        elif '/udp/239.253.43.6:5146' in original_url:
            formatted_names[original_url] = "风云音乐高清" 
        elif '/udp/239.77.1.234:5146' in original_url:
            formatted_names[original_url] = "九屏同播"                      
        elif '/udp/239.77.1.125:5146' in original_url:
            formatted_names[original_url] = "深圳电视剧" 
        elif '/udp/239.77.0.141:5146' in original_url:
            formatted_names[original_url] = "湛江新闻综合"
        elif '/udp/239.77.0.119:5146' in original_url:
            formatted_names[original_url] = "韶关绿色生活"
        elif '/udp/239.77.0.229:5146' in original_url:
            formatted_names[original_url] = "揭阳综合"
        elif '/udp/239.77.0.251:5146' in original_url:
            formatted_names[original_url] = "揭阳生活"
        elif '/udp/239.77.0.25:5146' in original_url:
            formatted_names[original_url] = "汕尾新闻综合"
        elif '/udp/239.77.0.187:5146' in original_url:
            formatted_names[original_url] = "汕尾文化生活"
        elif '/udp/239.77.0.201:5146' in original_url:
            formatted_names[original_url] = "江门综合"
        elif '/udp/239.77.0.202:5146' in original_url:
            formatted_names[original_url] = "江门侨乡生活"
        elif '/udp/239.77.0.203:5146' in original_url:
            formatted_names[original_url] = "江门教育"
        elif '/udp/239.253.43.33:5146' in original_url:
            formatted_names[original_url] = "清远新闻综合"
        elif '/udp/239.253.43.34:5146' in original_url:
            formatted_names[original_url] = "清远文旅生活"
        elif '/udp/239.77.0.253:5146' in original_url:
            formatted_names[original_url] = "云浮综合"
        elif '/udp/239.77.0.254:5146' in original_url:
            formatted_names[original_url] = "云浮文旅"
        elif '/udp/239.77.0.206:5146' in original_url:
            formatted_names[original_url] = "茂名综合"
        elif '/udp/239.77.0.207:5146' in original_url:
            formatted_names[original_url] = "茂名公共"
        elif '/udp/239.253.43.44:5146' in original_url:
            formatted_names[original_url] = "汕头文旅体育"
        elif '/udp/239.77.1.132:5146' in original_url:
            formatted_names[original_url] = "汕头文旅体育"
        elif '/udp/239.253.43.47:5146' in original_url:
            formatted_names[original_url] = "汕头文旅体育"
        elif '/udp/239.253.43.53:5146' in original_url:
            formatted_names[original_url] = "佛山公共"
        elif '/udp/239.253.43.54:5146' in original_url:
            formatted_names[original_url] = "佛山南海"
        elif '/udp/239.253.43.55:5146' in original_url:
            formatted_names[original_url] = "佛山顺德"
        elif '/udp/239.253.43.56:5146' in original_url:
            formatted_names[original_url] = "佛山影视"
        elif '/udp/239.253.43.57:5146' in original_url:
            formatted_names[original_url] = "佛山综合"
        elif '/udp/239.253.43.104:5146' in original_url:
            formatted_names[original_url] = "东莞新闻综合"
        elif '/udp/239.253.43.105:5146' in original_url:
            formatted_names[original_url] = "东莞生活资讯"
        elif '/udp/239.253.43.62:5146' in original_url:
            formatted_names[original_url] = "中山综合"
        elif '/udp/239.253.43.63:5146' in original_url:
            formatted_names[original_url] = "香山文化"
        elif '/udp/239.253.43.64:5146' in original_url:
            formatted_names[original_url] = "中山教育"
        elif '/udp/239.253.43.112:5146' in original_url:
            formatted_names[original_url] = "徐闻综合"
        elif '/udp/239.253.43.71:5146' in original_url:
            formatted_names[original_url] = "广州综合高清"
        elif '/udp/239.253.43.72:5146' in original_url:
            formatted_names[original_url] = "广州新闻高清"
        elif '/udp/239.253.43.73:5146' in original_url:
            formatted_names[original_url] = "广州影视高清"
        elif '/udp/239.253.43.74:5146' in original_url:
            formatted_names[original_url] = "广州法治高清"
        elif '/udp/239.253.43.75:5146' in original_url:
            formatted_names[original_url] = "广州竞赛高清"
        elif '/udp/239.253.43.76:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学一"
        elif '/udp/239.253.43.77:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学二"
        elif '/udp/239.253.43.78:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学三"
        elif '/udp/239.253.43.79:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学四"
        elif '/udp/239.253.43.80:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学五"
        elif '/udp/239.253.43.81:5146' in original_url:
            formatted_names[original_url] = "广视课堂 小学六"
        elif '/udp/239.253.43.89:5146' in original_url:
            formatted_names[original_url] = "广视课堂 初一"
        elif '/udp/239.253.43.90:5146' in original_url:
            formatted_names[original_url] = "广视课堂 初二"
        elif '/udp/239.253.43.91:5146' in original_url:
            formatted_names[original_url] = "广视课堂 初三"
        elif '/udp/239.253.43.92:5146' in original_url:
            formatted_names[original_url] = "广视课堂 高一"
        elif '/udp/239.253.43.93:5146' in original_url:
            formatted_names[original_url] = "广视课堂 高二"
            
            






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
        file.write("\n#广东,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJqaW5hbiI%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249InNoYW5kb25nIg%3D%3D&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJxaW5nZGFvIg%3D%3D&page=1&page_size=20', 
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJMaW55aSI%3D&page=1&page_size=20',
        


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
        for suffix in ['/rtp/239.21.1.216:5002','/rtp/239.21.1.246:5002','/rtp/239.21.1.82:5002','/rtp/239.21.1.81:5002','/rtp/239.21.1.115:5002','/rtp/239.21.1.220:5002','/rtp/239.21.1.249:5002','/rtp/239.21.1.131:5002','/rtp/239.21.1.224:5002','/rtp/239.21.1.237:5002','/rtp/239.21.1.235:5002','/rtp/239.21.1.250:5002','/rtp/239.21.1.172:5002','/rtp/239.21.2.21:5002','/rtp/239.21.1.130:5002','/rtp/239.21.1.102:5002','/rtp/239.21.1.106:5002','/rtp/239.21.2.50:5002','/rtp/239.21.1.143:5002','/rtp/239.21.1.144:5002','/rtp/239.21.2.13:5002','/rtp/239.21.1.244:5002','/rtp/239.21.1.218:5002','/rtp/239.21.1.141:5002','/rtp/239.21.1.58:5002','/rtp/239.21.1.183:5002','/rtp/239.21.1.59:5002','/rtp/239.21.1.61:5002','/rtp/239.21.1.208:5002','/rtp/239.21.1.60:5002','/rtp/239.21.1.112:5002','/rtp/239.21.1.101:5002','/rtp/239.21.1.169:5002','/rtp/239.21.1.176:5002','/rtp/239.21.1.57:5002','/rtp/239.21.1.140:5002','/rtp/239.21.1.54:5002','/rtp/239.21.1.175:5002','/rtp/239.21.1.56:5002','/rtp/239.21.1.177:5002','/rtp/239.21.1.55:5002','/rtp/239.21.1.134:5002','/rtp/239.21.1.53:5002','/rtp/239.21.1.215:5002','/rtp/239.21.1.243:5002','/rtp/239.21.1.228:5002','/rtp/239.21.1.221:5002','/rtp/239.21.1.76:5002','/rtp/239.21.1.75:5002','/rtp/239.21.1.181:5002','/rtp/239.21.1.174:5002','/rtp/239.21.1.248:5002','/rtp/239.21.1.210:5002','/rtp/239.21.1.193:5002','/rtp/239.21.1.214:5002','/rtp/239.21.1.209:5002','/rtp/239.21.1.79:5002','/rtp/239.21.1.80:5002','/rtp/239.21.1.236:5002','/rtp/239.21.1.245:5002','/rtp/239.21.2.27:5002','/rtp/239.21.1.225:5002','/rtp/239.21.1.229:5002','/rtp/239.21.1.105:5002','/rtp/239.21.2.12:5002','/rtp/239.21.1.240:5002','/rtp/239.21.1.239:5002','/rtp/239.21.1.226:5002','/rtp/239.21.1.66:5002','/rtp/239.21.1.68:5002','/rtp/239.21.1.65:5002','/rtp/239.21.1.133:5002','/rtp/239.21.1.62:5002','/rtp/239.21.1.94:5002','/rtp/239.21.1.64:5002','/rtp/239.21.1.63:5002','/rtp/239.21.1.149:5002','/rtp/239.21.2.20:5002','/rtp/239.21.1.139:5002','/rtp/239.21.1.138:5002','/rtp/239.21.2.19:5002','/rtp/239.21.1.187:5002','/rtp/239.21.1.98:5002','/rtp/239.21.1.100:5002','/rtp/239.21.1.182:5002','/rtp/239.21.1.84:5002','/rtp/239.21.1.114:5002','/rtp/239.21.1.109:5002','/rtp/239.21.1.83:5002','/rtp/239.21.1.178:5002','/rtp/239.21.1.119:5002','/rtp/239.21.1.238:5002','/rtp/239.21.1.118:5002','/rtp/239.21.1.77:5002','/rtp/239.21.1.78:5002','/rtp/239.21.1.180:5002','/rtp/239.21.1.117:5002','/rtp/239.21.1.204:5002','/rtp/239.21.1.116:5002','/rtp/239.21.1.205:5002','/rtp/239.21.2.10:5002','/rtp/239.21.2.11:5002','/rtp/239.21.1.241:5002','/rtp/239.21.1.242:5002','/rtp/239.21.1.132:5002','/rtp/239.21.1.254:5002','/rtp/239.21.1.253:5002','/rtp/239.21.1.219:5002','/rtp/239.21.1.227:5002','/rtp/239.21.1.211:5002','/rtp/239.21.1.247:5002','/rtp/239.21.1.103:5002','/rtp/239.21.2.18:5002','/rtp/239.21.2.23:5002','/rtp/239.21.1.217:5002','/rtp/239.21.1.162:5002','/rtp/239.21.1.185:5002','/rtp/239.21.1.251:5002','/rtp/239.21.1.170:5002','/rtp/239.21.1.107:5002','/rtp/239.21.1.252:5002','/rtp/239.21.2.24:5002','/rtp/239.21.1.69:5002','/rtp/239.21.1.70:5002','/rtp/239.21.1.71:5002','/rtp/239.21.1.72:5002','/rtp/239.21.1.73:5002','/rtp/239.21.1.74:5002','/rtp/239.21.1.231:5002','/rtp/239.21.1.232:5002','/rtp/239.21.1.230:5002','/udp/239.253.254.23:8000','/udp/239.253.254.151:8000','/udp/239.253.254.159:8000','/udp/239.253.254.114:8000','/udp/239.253.254.24:8000','/udp/239.253.254.22:8000','/udp/239.253.254.160:8000','/udp/239.253.254.59:8000','/udp/239.253.254.25:8000','/udp/239.253.254.67:8000','/udp/239.253.254.249:8000','/udp/239.253.254.250:8000','/udp/239.253.254.251:8000','/udp/239.253.254.252:8000','/udp/239.253.254.253:8000','/udp/239.253.254.243:8000','/udp/239.253.254.244:8000','/udp/239.253.254.246:8000','/udp/239.253.254.248:8000','/udp/239.253.254.247:8000','/udp/239.253.254.242:8000',]:
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
        elif '/rtp/239.21.1.216:5002' in original_url:
            formatted_names[original_url] = "东平新闻"
        elif '/rtp/239.21.1.246:5002' in original_url:
            formatted_names[original_url] = "东明"
        elif '/rtp/239.21.1.82:5002' in original_url:
            formatted_names[original_url] = "东营公共"
        elif '/rtp/239.21.1.81:5002' in original_url:
            formatted_names[original_url] = "东营新闻"
        elif '/rtp/239.21.1.115:5002' in original_url:
            formatted_names[original_url] = "中国交通"
        elif '/rtp/239.21.1.220:5002' in original_url:
            formatted_names[original_url] = "乳山"
        elif '/rtp/239.21.1.249:5002' in original_url:
            formatted_names[original_url] = "五莲新闻"
        elif '/rtp/239.21.1.131:5002' in original_url:
            formatted_names[original_url] = "光影"
        elif '/rtp/239.21.1.224:5002' in original_url:
            formatted_names[original_url] = "兖州新闻"
        elif '/rtp/239.21.1.237:5002' in original_url:
            formatted_names[original_url] = "兰陵综合"
        elif '/rtp/239.21.1.235:5002' in original_url:
            formatted_names[original_url] = "农林卫视"
        elif '/rtp/239.21.1.250:5002' in original_url:
            formatted_names[original_url] = "冠县综合"
        elif '/rtp/239.21.1.172:5002' in original_url:
            formatted_names[original_url] = "北京纪实"
        elif '/rtp/239.21.2.21:5002' in original_url:
            formatted_names[original_url] = "单县综合"
        elif '/rtp/239.21.1.130:5002' in original_url:
            formatted_names[original_url] = "墨宝"
        elif '/rtp/239.21.1.102:5002' in original_url:
            formatted_names[original_url] = "夏津公共"
        elif '/rtp/239.21.1.106:5002' in original_url:
            formatted_names[original_url] = "夏津综合"
        elif '/rtp/239.21.2.50:5002' in original_url:
            formatted_names[original_url] = "宁津新闻"
        elif '/rtp/239.21.1.143:5002' in original_url:
            formatted_names[original_url] = "宁阳1"
        elif '/rtp/239.21.1.144:5002' in original_url:
            formatted_names[original_url] = "宁阳2"
        elif '/rtp/239.21.2.13:5002' in original_url:
            formatted_names[original_url] = "安丘新闻"
        elif '/rtp/239.21.1.244:5002' in original_url:
            formatted_names[original_url] = "定陶"
        elif '/rtp/239.21.1.218:5002' in original_url:
            formatted_names[original_url] = "寿光蔬菜"
        elif '/rtp/239.21.1.141:5002' in original_url:
            formatted_names[original_url] = "山东体育"
        elif '/rtp/239.21.1.58:5002' in original_url:
            formatted_names[original_url] = "山东体育"
        elif '/rtp/239.21.1.183:5002' in original_url:
            formatted_names[original_url] = "山东农科"
        elif '/rtp/239.21.1.59:5002' in original_url:
            formatted_names[original_url] = "山东农科"
        elif '/rtp/239.21.1.61:5002' in original_url:
            formatted_names[original_url] = "山东国际"
        elif '/rtp/239.21.1.208:5002' in original_url:
            formatted_names[original_url] = "山东少儿"
        elif '/rtp/239.21.1.60:5002' in original_url:
            formatted_names[original_url] = "山东少儿"
        elif '/rtp/239.21.1.112:5002' in original_url:
            formatted_names[original_url] = "山东居家购物"
        elif '/rtp/239.21.1.101:5002' in original_url:
            formatted_names[original_url] = "山东教育"
        elif '/rtp/239.21.1.169:5002' in original_url:
            formatted_names[original_url] = "山东教育"
        elif '/rtp/239.21.1.176:5002' in original_url:
            formatted_names[original_url] = "山东文旅"
        elif '/rtp/239.21.1.57:5002' in original_url:
            formatted_names[original_url] = "山东文旅"
        elif '/rtp/239.21.1.140:5002' in original_url:
            formatted_names[original_url] = "山东新闻"
        elif '/rtp/239.21.1.54:5002' in original_url:
            formatted_names[original_url] = "山东新闻"
        elif '/rtp/239.21.1.175:5002' in original_url:
            formatted_names[original_url] = "山东生活"
        elif '/rtp/239.21.1.56:5002' in original_url:
            formatted_names[original_url] = "山东生活"
        elif '/rtp/239.21.1.177:5002' in original_url:
            formatted_names[original_url] = "山东综艺"
        elif '/rtp/239.21.1.55:5002' in original_url:
            formatted_names[original_url] = "山东综艺"
        elif '/rtp/239.21.1.134:5002' in original_url:
            formatted_names[original_url] = "山东齐鲁"
        elif '/rtp/239.21.1.53:5002' in original_url:
            formatted_names[original_url] = "山东齐鲁"
        elif '/rtp/239.21.1.215:5002' in original_url:
            formatted_names[original_url] = "巨野新闻"
        elif '/rtp/239.21.1.243:5002' in original_url:
            formatted_names[original_url] = "平原新闻"
        elif '/rtp/239.21.1.228:5002' in original_url:
            formatted_names[original_url] = "平度新闻"
        elif '/rtp/239.21.1.221:5002' in original_url:
            formatted_names[original_url] = "平阴综合"
        elif '/rtp/239.21.1.76:5002' in original_url:
            formatted_names[original_url] = "德州公共"
        elif '/rtp/239.21.1.75:5002' in original_url:
            formatted_names[original_url] = "德州新闻"
        elif '/rtp/239.21.1.181:5002' in original_url:
            formatted_names[original_url] = "惠民综合"
        elif '/rtp/239.21.1.174:5002' in original_url:
            formatted_names[original_url] = "文登"
        elif '/rtp/239.21.1.248:5002' in original_url:
            formatted_names[original_url] = "新泰乡村"
        elif '/rtp/239.21.1.210:5002' in original_url:
            formatted_names[original_url] = "新泰新闻"
        elif '/rtp/239.21.1.193:5002' in original_url:
            formatted_names[original_url] = "新闻综合"
        elif '/rtp/239.21.1.214:5002' in original_url:
            formatted_names[original_url] = "无棣综合"
        elif '/rtp/239.21.1.209:5002' in original_url:
            formatted_names[original_url] = "日照岚山"
        elif '/rtp/239.21.1.79:5002' in original_url:
            formatted_names[original_url] = "日照新闻"
        elif '/rtp/239.21.1.80:5002' in original_url:
            formatted_names[original_url] = "日照科教"
        elif '/rtp/239.21.1.236:5002' in original_url:
            formatted_names[original_url] = "日照莒县TV-1"
        elif '/rtp/239.21.1.245:5002' in original_url:
            formatted_names[original_url] = "昌乐新闻"
        elif '/rtp/239.21.2.27:5002' in original_url:
            formatted_names[original_url] = "昌邑新闻"
        elif '/rtp/239.21.1.225:5002' in original_url:
            formatted_names[original_url] = "曲阜新闻"
        elif '/rtp/239.21.1.229:5002' in original_url:
            formatted_names[original_url] = "栖霞综合"
        elif '/rtp/239.21.1.105:5002' in original_url:
            formatted_names[original_url] = "桓台"
        elif '/rtp/239.21.2.12:5002' in original_url:
            formatted_names[original_url] = "梁山新闻"
        elif '/rtp/239.21.1.240:5002' in original_url:
            formatted_names[original_url] = "武城影视"
        elif '/rtp/239.21.1.239:5002' in original_url:
            formatted_names[original_url] = "武城新闻"
        elif '/rtp/239.21.1.226:5002' in original_url:
            formatted_names[original_url] = "沾化综合"
        elif '/rtp/239.21.1.66:5002' in original_url:
            formatted_names[original_url] = "济南娱乐"
        elif '/rtp/239.21.1.68:5002' in original_url:
            formatted_names[original_url] = "济南少儿"
        elif '/rtp/239.21.1.65:5002' in original_url:
            formatted_names[original_url] = "济南影视"
        elif '/rtp/239.21.1.133:5002' in original_url:
            formatted_names[original_url] = "济南教育"
        elif '/rtp/239.21.1.62:5002' in original_url:
            formatted_names[original_url] = "济南新闻"
        elif '/rtp/239.21.1.94:5002' in original_url:
            formatted_names[original_url] = "济南新闻"
        elif '/rtp/239.21.1.64:5002' in original_url:
            formatted_names[original_url] = "济南生活"
        elif '/rtp/239.21.1.63:5002' in original_url:
            formatted_names[original_url] = "济南都市"
        elif '/rtp/239.21.1.149:5002' in original_url:
            formatted_names[original_url] = "济南鲁中"
        elif '/rtp/239.21.2.20:5002' in original_url:
            formatted_names[original_url] = "济宁公共"
        elif '/rtp/239.21.1.139:5002' in original_url:
            formatted_names[original_url] = "济宁教育"
        elif '/rtp/239.21.1.138:5002' in original_url:
            formatted_names[original_url] = "济宁综合"
        elif '/rtp/239.21.2.19:5002' in original_url:
            formatted_names[original_url] = "济宁综合"
        elif '/rtp/239.21.1.187:5002' in original_url:
            formatted_names[original_url] = "济阳综合"
        elif '/rtp/239.21.1.98:5002' in original_url:
            formatted_names[original_url] = "海看剧场"
        elif '/rtp/239.21.1.100:5002' in original_url:
            formatted_names[original_url] = "海看热播"
        elif '/rtp/239.21.1.182:5002' in original_url:
            formatted_names[original_url] = "淄博公共"
        elif '/rtp/239.21.1.84:5002' in original_url:
            formatted_names[original_url] = "淄博新闻"
        elif '/rtp/239.21.1.114:5002' in original_url:
            formatted_names[original_url] = "淄博沂源新闻"
        elif '/rtp/239.21.1.109:5002' in original_url:
            formatted_names[original_url] = "淄博生活"
        elif '/rtp/239.21.1.83:5002' in original_url:
            formatted_names[original_url] = "淄博都市"
        elif '/rtp/239.21.1.178:5002' in original_url:
            formatted_names[original_url] = "滕州综合"
        elif '/rtp/239.21.1.119:5002' in original_url:
            formatted_names[original_url] = "滨州公共"
        elif '/rtp/239.21.1.238:5002' in original_url:
            formatted_names[original_url] = "滨州好生新闻"
        elif '/rtp/239.21.1.118:5002' in original_url:
            formatted_names[original_url] = "滨州新闻"
        elif '/rtp/239.21.1.77:5002' in original_url:
            formatted_names[original_url] = "潍坊1"
        elif '/rtp/239.21.1.78:5002' in original_url:
            formatted_names[original_url] = "潍坊2"
        elif '/rtp/239.21.1.180:5002' in original_url:
            formatted_names[original_url] = "潍坊寿光新闻"
        elif '/rtp/239.21.1.117:5002' in original_url:
            formatted_names[original_url] = "烟台公共"
        elif '/rtp/239.21.1.204:5002' in original_url:
            formatted_names[original_url] = "烟台影视"
        elif '/rtp/239.21.1.116:5002' in original_url:
            formatted_names[original_url] = "烟台新闻"
        elif '/rtp/239.21.1.205:5002' in original_url:
            formatted_names[original_url] = "烟台经济"
        elif '/rtp/239.21.2.10:5002' in original_url:
            formatted_names[original_url] = "牟平新闻"
        elif '/rtp/239.21.2.11:5002' in original_url:
            formatted_names[original_url] = "牟平生活"
        elif '/rtp/239.21.1.241:5002' in original_url:
            formatted_names[original_url] = "禹城综合"
        elif '/rtp/239.21.1.242:5002' in original_url:
            formatted_names[original_url] = "禹城综艺"
        elif '/rtp/239.21.1.132:5002' in original_url:
            formatted_names[original_url] = "美人"
        elif '/rtp/239.21.1.254:5002' in original_url:
            formatted_names[original_url] = "聊城公共"
        elif '/rtp/239.21.1.253:5002' in original_url:
            formatted_names[original_url] = "聊城综合"
        elif '/rtp/239.21.1.219:5002' in original_url:
            formatted_names[original_url] = "茌平综合"
        elif '/rtp/239.21.1.227:5002' in original_url:
            formatted_names[original_url] = "荣成综合"
        elif '/rtp/239.21.1.211:5002' in original_url:
            formatted_names[original_url] = "莘县"
        elif '/rtp/239.21.1.247:5002' in original_url:
            formatted_names[original_url] = "莱西综合"
        elif '/rtp/239.21.1.103:5002' in original_url:
            formatted_names[original_url] = "菏泽"
        elif '/rtp/239.21.2.18:5002' in original_url:
            formatted_names[original_url] = "菏泽2"
        elif '/rtp/239.21.2.23:5002' in original_url:
            formatted_names[original_url] = "蒙阴"
        elif '/rtp/239.21.1.217:5002' in original_url:
            formatted_names[original_url] = "诸城新闻"
        elif '/rtp/239.21.1.162:5002' in original_url:
            formatted_names[original_url] = "足球"
        elif '/rtp/239.21.1.185:5002' in original_url:
            formatted_names[original_url] = "邹城新闻"
        elif '/rtp/239.21.1.251:5002' in original_url:
            formatted_names[original_url] = "郓城新闻"
        elif '/rtp/239.21.1.170:5002' in original_url:
            formatted_names[original_url] = "金鹰纪实"
        elif '/rtp/239.21.1.107:5002' in original_url:
            formatted_names[original_url] = "长清新闻"
        elif '/rtp/239.21.1.252:5002' in original_url:
            formatted_names[original_url] = "阳信新闻"
        elif '/rtp/239.21.2.24:5002' in original_url:
            formatted_names[original_url] = "陵城新闻"
        elif '/rtp/239.21.1.69:5002' in original_url:
            formatted_names[original_url] = "青岛1"
        elif '/rtp/239.21.1.70:5002' in original_url:
            formatted_names[original_url] = "青岛2"
        elif '/rtp/239.21.1.71:5002' in original_url:
            formatted_names[original_url] = "青岛3"
        elif '/rtp/239.21.1.72:5002' in original_url:
            formatted_names[original_url] = "青岛4"
        elif '/rtp/239.21.1.73:5002' in original_url:
            formatted_names[original_url] = "青岛5"
        elif '/rtp/239.21.1.74:5002' in original_url:
            formatted_names[original_url] = "青岛6"
        elif '/rtp/239.21.1.231:5002' in original_url:
            formatted_names[original_url] = "青州文化旅游"
        elif '/rtp/239.21.1.232:5002' in original_url:
            formatted_names[original_url] = "青州综合"
        elif '/rtp/239.21.1.230:5002' in original_url:
            formatted_names[original_url] = "齐河新闻"
        elif '/udp/239.253.254.23:8000' in original_url:
            formatted_names[original_url] = "山东新闻"
        elif '/udp/239.253.254.151:8000' in original_url:
            formatted_names[original_url] = "山东生活"
        elif '/udp/239.253.254.159:8000' in original_url:
            formatted_names[original_url] = "山东综艺"
        elif '/udp/239.253.254.114:8000' in original_url:
            formatted_names[original_url] = "山东齐鲁"
        elif '/udp/239.253.254.24:8000' in original_url:
            formatted_names[original_url] = "山东农科"
        elif '/udp/239.253.254.22:8000' in original_url:
            formatted_names[original_url] = "山东体育"
        elif '/udp/239.253.254.160:8000' in original_url:
            formatted_names[original_url] = "山东文旅"
        elif '/udp/239.253.254.59:8000' in original_url:
            formatted_names[original_url] = "山东教育"
        elif '/udp/239.253.254.25:8000' in original_url:
            formatted_names[original_url] = "山东少儿"
        elif '/udp/239.253.254.67:8000' in original_url:
            formatted_names[original_url] = "海洋频道"
        elif '/udp/239.253.254.249:8000' in original_url:
            formatted_names[original_url] = "青岛1"
        elif '/udp/239.253.254.250:8000' in original_url:
            formatted_names[original_url] = "青岛2"
        elif '/udp/239.253.254.251:8000' in original_url:
            formatted_names[original_url] = "青岛3"
        elif '/udp/239.253.254.252:8000' in original_url:
            formatted_names[original_url] = "青岛4"
        elif '/udp/239.253.254.253:8000' in original_url:
            formatted_names[original_url] = "青岛5"
        elif '/udp/239.253.254.243:8000' in original_url:
            formatted_names[original_url] = "黄岛综合"
        elif '/udp/239.253.254.244:8000' in original_url:
            formatted_names[original_url] = "黄岛生活"
        elif '/udp/239.253.254.246:8000' in original_url:
            formatted_names[original_url] = "胶州综合"
        elif '/udp/239.253.254.248:8000' in original_url:
            formatted_names[original_url] = "平度电视"
        elif '/udp/239.253.254.247:8000' in original_url:
            formatted_names[original_url] = "莱西综合"
        elif '/udp/239.253.254.242:8000' in original_url:
            formatted_names[original_url] = "崂山电视"    


















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
        file.write("\n#山东,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

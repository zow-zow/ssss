import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSIgbmFuY2hvbmci&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249InNpY2h1YW4i&page=1&page_size=20', 



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
        for suffix in ['/udp/239.93.1.188:5140','/udp/239.93.0.41:5140','/udp/239.93.0.52:5140','/udp/239.93.0.219:5140','/udp/239.93.1.195:5140','/udp/239.93.1.101:5140','/udp/239.93.1.20:5140','/udp/239.93.0.47:5140','/udp/239.93.1.102:5140','/udp/239.93.1.16:5140','/udp/239.93.1.54:5140','/udp/239.93.1.18:5140','/udp/239.93.0.162:2192','/udp/239.93.1.4:2191','/udp/239.93.1.10:2193','/udp/239.93.0.157:2194','/udp/239.93.1.101:5140','/udp/239.93.1.102:5140','/udp/239.93.0.47:5140','/udp/239.93.0.166:5140','/udp/239.93.1.144:5140','/udp/239.93.0.219:5140','/udp/239.93.42.44:5140','/udp/239.93.0.52:5140','/udp/239.93.0.252:5140','/udp/239.93.0.17:1239','/udp/239.93.0.18:1238','/udp/239.93.0.19:1250','/udp/239.93.1.231:5140','/udp/239.93.0.21:1251','/udp/239.93.0.22:1252','/udp/239.93.1.112:5140','/udp/239.93.0.94:5140','/udp/239.93.1.189:5140','/udp/239.93.0.214:5140','/udp/239.93.0.126:5140','/udp/239.93.0.224:1281','/udp/239.93.0.211:9148','/udp/239.93.1.172:5140','/udp/239.93.1.190:5140','/udp/239.93.1.110:5140','/udp/239.93.42.70:5140','/udp/239.93.42.71:5140','/udp/239.93.42.72:5140','/udp/239.93.42.47:5140','/udp/239.93.0.138:5140','/udp/239.93.0.139:5140','/udp/239.93.0.105:5140','/udp/239.93.0.56:9020','/udp/239.93.0.140:5140','/udp/239.93.0.143:5140','/udp/239.93.0.95:5140','/udp/239.93.0.208:5140','/udp/239.93.0.108:5140','/udp/239.93.0.251:5140','/udp/239.93.0.147:5140','/udp/239.93.0.193:9000','/udp/239.93.0.146:5140','/udp/239.93.0.151:5140','/udp/239.93.0.198:9044','/udp/239.93.0.144:5140','/udp/239.93.1.191:5140','/udp/239.93.1.197:5140','/udp/239.93.1.177:5140','/udp/239.93.1.188:5140','/udp/239.93.1.178:5140','/udp/239.93.1.175:5140','/udp/239.93.1.156:5140','/udp/239.93.0.43:5140','/udp/239.93.1.104:1234','/udp/239.93.0.206:8028','/udp/239.93.42.21:5140','/udp/239.93.42.9:5140','/udp/239.93.42.22:5140','/udp/239.93.42.10:5140','/udp/239.93.42.11:5140','/udp/239.93.42.30:5140','/udp/239.93.42.14:5140','/udp/239.93.42.13:5140','/udp/239.93.42.12:5140','/udp/239.93.42.16:5140','/udp/239.93.42.15:5140','/udp/239.93.42.17:5140','/udp/239.93.42.18:5140','/udp/239.93.42.23:5140','/udp/239.93.42.19:5140','/udp/239.93.42.20:5140','/udp/239.93.42.32:5140','/udp/239.93.0.57:9024','/udp/239.93.0.138:5140','/udp/239.93.0.139:5140','/udp/239.93.0.105:5140','/udp/239.93.0.56:9020','/udp/239.93.0.140:5140','/udp/239.93.0.143:5140','/udp/239.93.0.95:5140','/udp/239.93.0.208:5140','/udp/239.93.0.108:5140','/udp/239.93.0.251:5140','/udp/239.93.0.147:5140','/udp/239.93.0.193:9000','/udp/239.93.0.146:5140','/udp/239.93.0.151:5140','/udp/239.93.0.198:9044','/udp/239.93.0.144:5140','/udp/239.93.42.48:5140','/udp/239.93.42.47:5140','/udp/239.93.0.217:9208','/udp/239.93.0.190:9012','/udp/239.93.0.106:5140','/udp/239.93.0.206:8028','/udp/239.93.0.62:5140','/udp/239.93.0.116:9136','/udp/239.93.0.141:5140','/udp/239.93.0.135:9008','/udp/239.93.1.135:5140','/udp/239.93.0.136:5140','/udp/239.93.0.117:1292','/udp/239.93.0.197:9040','/udp/239.93.0.202:9068','/udp/239.93.0.203:9072','/udp/239.93.1.154:5140','/udp/239.93.0.215:9132','/udp/239.93.0.204:9076','/udp/239.93.0.199:9048','/udp/239.93.0.200:9052','/udp/239.93.0.235:1282','/udp/239.93.0.195:8012','/udp/239.93.0.236:1283','/udp/239.93.0.91:2101','/udp/239.93.1.171:5140','/udp/239.93.42.35:5140','/udp/239.93.42.31:5140','/udp/239.93.42.8:5140','/udp/239.93.42.2:5140','/udp/239.93.42.33:5140','/udp/239.93.42.56:5140','/udp/239.93.42.55:5140','/udp/239.93.1.151:5140','/udp/239.93.0.114:5140','/udp/239.93.1.198:5140','/udp/239.93.1.179:5140','/udp/239.93.1.191:5140','/udp/239.93.1.197:5140','/udp/239.93.1.177:5140','/udp/239.93.1.188:5140','/udp/239.93.1.178:5140','/udp/239.93.1.175:5140','/udp/239.93.1.176:5140',

]:
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
        elif '/udp/239.93.0.169:5140' in original_url:
            formatted_names[original_url] = "四川卫视"
        elif '/udp/239.93.1.188:5140' in original_url:
            formatted_names[original_url] = "四川卫视"
        elif '/udp/239.93.0.41:5140' in original_url:
            formatted_names[original_url] = "四川康巴卫视"
        elif '/udp/239.93.0.52:5140' in original_url:
            formatted_names[original_url] = "四川公共乡村"
        elif '/udp/239.93.0.219:5140' in original_url:
            formatted_names[original_url] = "四川妇女儿童"
        elif '/udp/239.93.0.166:5140' in original_url:
            formatted_names[original_url] = "四川影视文艺"
        elif '/udp/239.93.1.195:5140' in original_url:
            formatted_names[original_url] = "梨园"
        elif '/udp/239.93.1.101:5140' in original_url:
            formatted_names[original_url] = "四川文化旅游"
        elif '/udp/239.93.1.20:5140' in original_url:
            formatted_names[original_url] = "四川文化旅游"
        elif '/udp/239.93.0.47:5140' in original_url:
            formatted_names[original_url] = "四川新闻"
        elif '/udp/239.93.1.102:5140' in original_url:
            formatted_names[original_url] = "四川经济"
        elif '/udp/239.93.1.16:5140' in original_url:
            formatted_names[original_url] = "四川经济"
        elif '/udp/239.93.1.54:5140' in original_url:
            formatted_names[original_url] = "峨眉电影"
        elif '/udp/239.93.1.18:5140' in original_url:
            formatted_names[original_url] = "峨眉电影"
        elif '/udp/239.93.0.162:2192' in original_url:
            formatted_names[original_url] = "凤凰中文"
        elif '/udp/239.93.1.9:2192' in original_url:
            formatted_names[original_url] = "凤凰中文"
        elif '/udp/239.93.0.118:2191' in original_url:
            formatted_names[original_url] = "凤凰资讯"
        elif '/udp/239.93.1.4:2191' in original_url:
            formatted_names[original_url] = "凤凰资讯"
        elif '/udp/239.93.0.156:2193' in original_url:
            formatted_names[original_url] = "星空"
        elif '/udp/239.93.1.10:2193' in original_url:
            formatted_names[original_url] = "星空"
        elif '/udp/239.93.0.157:2194' in original_url:
            formatted_names[original_url] = "CHANNEL-V"
        elif '/udp/239.93.1.7:2194' in original_url:
            formatted_names[original_url] = "CHANNEL-V"
        elif '/udp/239.93.1.101:5140' in original_url:
            formatted_names[original_url] = "SCTV-2高清"
        elif '/udp/239.93.1.102:5140' in original_url:
            formatted_names[original_url] = "SCTV-3高清"
        elif '/udp/239.93.0.47:5140' in original_url:
            formatted_names[original_url] = "SCTV-4高清"
        elif '/udp/239.93.0.166:5140' in original_url:
            formatted_names[original_url] = "SCTV-5高清"
        elif '/udp/239.93.1.144:5140' in original_url:
            formatted_names[original_url] = "SCTV-6高清"
        elif '/udp/239.93.0.219:5140' in original_url:
            formatted_names[original_url] = "SCTV-7高清"
        elif '/udp/239.93.42.44:5140' in original_url:
            formatted_names[original_url] = "SCTV-科教高清"
        elif '/udp/239.93.0.52:5140' in original_url:
            formatted_names[original_url] = "四川乡村高清"
        elif '/udp/239.93.0.252:5140' in original_url:
            formatted_names[original_url] = "峨眉电影高清"
        elif '/udp/239.93.0.17:1239' in original_url:
            formatted_names[original_url] = "CDTV-2"
        elif '/udp/239.93.0.18:1238' in original_url:
            formatted_names[original_url] = "CDTV-3"
        elif '/udp/239.93.0.19:1250' in original_url:
            formatted_names[original_url] = "CDTV-4"
        elif '/udp/239.93.1.231:5140' in original_url:
            formatted_names[original_url] = "CDTV-5"
        elif '/udp/239.93.0.21:1251' in original_url:
            formatted_names[original_url] = "CDTV-6"
        elif '/udp/239.93.0.22:1252' in original_url:
            formatted_names[original_url] = "CDTV-8"
        elif '/udp/239.93.1.112:5140' in original_url:
            formatted_names[original_url] = "熊猫新闻高清"
        elif '/udp/239.93.0.94:5140' in original_url:
            formatted_names[original_url] = "熊猫体娱高清"
        elif '/udp/239.93.1.189:5140' in original_url:
            formatted_names[original_url] = "熊猫少儿高清"
        elif '/udp/239.93.0.214:5140' in original_url:
            formatted_names[original_url] = "熊猫影院高清"
        elif '/udp/239.93.0.126:5140' in original_url:
            formatted_names[original_url] = "睛彩四川"
        elif '/udp/239.93.0.224:1281' in original_url:
            formatted_names[original_url] = "成都体育高清"
        elif '/udp/239.93.0.211:9148' in original_url:
            formatted_names[original_url] = "熊猫频道高清"
        elif '/udp/239.93.1.172:5140' in original_url:
            formatted_names[original_url] = "金熊猫卡通高清"
        elif '/udp/239.93.1.190:5140' in original_url:
            formatted_names[original_url] = "熊猫爱生活高清"
        elif '/udp/239.93.1.110:5140' in original_url:
            formatted_names[original_url] = "大爱四川高清"
        elif '/udp/239.93.42.70:5140' in original_url:
            formatted_names[original_url] = "大爱旅游高清"
        elif '/udp/239.93.42.71:5140' in original_url:
            formatted_names[original_url] = "大爱生活高清"
        elif '/udp/239.93.42.72:5140' in original_url:
            formatted_names[original_url] = "大爱时尚高清"
        elif '/udp/239.93.42.47:5140' in original_url:
            formatted_names[original_url] = "HD看电影"
        elif '/udp/239.93.0.138:5140' in original_url:
            formatted_names[original_url] = "华语影院"
        elif '/udp/239.93.0.139:5140' in original_url:
            formatted_names[original_url] = "星光院线"
        elif '/udp/239.93.0.105:5140' in original_url:
            formatted_names[original_url] = "全球大片"
        elif '/udp/239.93.0.56:9020' in original_url:
            formatted_names[original_url] = "热播剧场"
        elif '/udp/239.93.0.140:5140' in original_url:
            formatted_names[original_url] = "热门剧场"
        elif '/udp/239.93.0.143:5140' in original_url:
            formatted_names[original_url] = "港剧风云"
        elif '/udp/239.93.0.95:5140' in original_url:
            formatted_names[original_url] = "谍战剧场"
        elif '/udp/239.93.0.208:5140' in original_url:
            formatted_names[original_url] = "卡酷动画"
        elif '/udp/239.93.0.108:5140' in original_url:
            formatted_names[original_url] = "金鹰卡通"
        elif '/udp/239.93.0.251:5140' in original_url:
            formatted_names[original_url] = "优漫卡通"
        elif '/udp/239.93.0.147:5140' in original_url:
            formatted_names[original_url] = "宝宝动画高清"
        elif '/udp/239.93.0.193:9000' in original_url:
            formatted_names[original_url] = "少儿动画高清"
        elif '/udp/239.93.0.146:5140' in original_url:
            formatted_names[original_url] = "青春动漫"
        elif '/udp/239.93.0.151:5140' in original_url:
            formatted_names[original_url] = "热门综艺高清"
        elif '/udp/239.93.0.198:9044' in original_url:
            formatted_names[original_url] = "音乐现场高清"
        elif '/udp/239.93.0.144:5140' in original_url:
            formatted_names[original_url] = "戏曲精选"
        elif '/udp/239.93.1.191:5140' in original_url:
            formatted_names[original_url] = "亲子趣学4K"
        elif '/udp/239.93.1.197:5140' in original_url:
            formatted_names[original_url] = "津津悦读4K"
        elif '/udp/239.93.1.177:5140' in original_url:
            formatted_names[original_url] = "动画番剧"
        elif '/udp/239.93.1.188:5140' in original_url:
            formatted_names[original_url] = "中录动漫4K"
        elif '/udp/239.93.1.178:5140' in original_url:
            formatted_names[original_url] = "熊猫24小时"
        elif '/udp/239.93.1.175:5140' in original_url:
            formatted_names[original_url] = "综艺咖秀"
        elif '/udp/239.93.1.156:5140' in original_url:
            formatted_names[original_url] = "4K超高清电影"
        elif '/udp/239.93.0.43:5140' in original_url:
            formatted_names[original_url] = "4K乐享超清"
        elif '/udp/239.93.1.104:1234' in original_url:
            formatted_names[original_url] = "i成都"
        elif '/udp/239.93.0.206:8028' in original_url:
            formatted_names[original_url] = "爱生活"
        elif '/udp/239.93.42.21:5140' in original_url:
            formatted_names[original_url] = "爱怀旧"
        elif '/udp/239.93.42.9:5140' in original_url:
            formatted_names[original_url] = "爱喜剧"
        elif '/udp/239.93.42.22:5140' in original_url:
            formatted_names[original_url] = "爱奇谈"
        elif '/udp/239.93.42.10:5140' in original_url:
            formatted_names[original_url] = "爱科幻"
        elif '/udp/239.93.42.11:5140' in original_url:
            formatted_names[original_url] = "爱院线"
        elif '/udp/239.93.42.30:5140' in original_url:
            formatted_names[original_url] = "都剧场"
        elif '/udp/239.93.42.14:5140' in original_url:
            formatted_names[original_url] = "爱谍战"
        elif '/udp/239.93.42.13:5140' in original_url:
            formatted_names[original_url] = "爱经典"
        elif '/udp/239.93.42.12:5140' in original_url:
            formatted_names[original_url] = "爱悬疑"
        elif '/udp/239.93.42.16:5140' in original_url:
            formatted_names[original_url] = "爱青春"
        elif '/udp/239.93.42.15:5140' in original_url:
            formatted_names[original_url] = "爱都市"
        elif '/udp/239.93.42.17:5140' in original_url:
            formatted_names[original_url] = "爱幼教"
        elif '/udp/239.93.42.18:5140' in original_url:
            formatted_names[original_url] = "爱玩具"
        elif '/udp/239.93.42.23:5140' in original_url:
            formatted_names[original_url] = "爱动漫"
        elif '/udp/239.93.42.19:5140' in original_url:
            formatted_names[original_url] = "爱电竞"
        elif '/udp/239.93.42.20:5140' in original_url:
            formatted_names[original_url] = "爱赛车"
        elif '/udp/239.93.42.32:5140' in original_url:
            formatted_names[original_url] = "爱宠物"
        elif '/udp/239.93.0.57:9024' in original_url:
            formatted_names[original_url] = "经典电影"
        elif '/udp/239.93.0.138:5140' in original_url:
            formatted_names[original_url] = "华语影院"
        elif '/udp/239.93.0.139:5140' in original_url:
            formatted_names[original_url] = "星光院线"
        elif '/udp/239.93.0.105:5140' in original_url:
            formatted_names[original_url] = "全球大片"
        elif '/udp/239.93.0.56:9020' in original_url:
            formatted_names[original_url] = "热播剧场"
        elif '/udp/239.93.0.140:5140' in original_url:
            formatted_names[original_url] = "热门剧场"
        elif '/udp/239.93.0.143:5140' in original_url:
            formatted_names[original_url] = "港剧风云"
        elif '/udp/239.93.0.95:5140' in original_url:
            formatted_names[original_url] = "谍战剧场"
        elif '/udp/239.93.0.208:5140' in original_url:
            formatted_names[original_url] = "卡酷动画"
        elif '/udp/239.93.0.108:5140' in original_url:
            formatted_names[original_url] = "金鹰卡通"
        elif '/udp/239.93.0.251:5140' in original_url:
            formatted_names[original_url] = "优漫卡通"
        elif '/udp/239.93.0.147:5140' in original_url:
            formatted_names[original_url] = "宝宝动画"
        elif '/udp/239.93.0.193:9000' in original_url:
            formatted_names[original_url] = "少儿动画"
        elif '/udp/239.93.0.146:5140' in original_url:
            formatted_names[original_url] = "青春动漫"
        elif '/udp/239.93.0.151:5140' in original_url:
            formatted_names[original_url] = "热门综艺"
        elif '/udp/239.93.0.198:9044' in original_url:
            formatted_names[original_url] = "音乐现场"
        elif '/udp/239.93.0.144:5140' in original_url:
            formatted_names[original_url] = "戏曲精选"
        elif '/udp/239.93.42.48:5140' in original_url:
            formatted_names[original_url] = "家政频道"
        elif '/udp/239.93.42.47:5140' in original_url:
            formatted_names[original_url] = "HD看电影"
        elif '/udp/239.93.0.217:9208' in original_url:
            formatted_names[original_url] = "戏曲"
        elif '/udp/239.93.0.190:9012' in original_url:
            formatted_names[original_url] = "魅力时尚"
        elif '/udp/239.93.0.106:5140' in original_url:
            formatted_names[original_url] = "生活时尚"
        elif '/udp/239.93.0.206:8028' in original_url:
            formatted_names[original_url] = "爱生活"
        elif '/udp/239.93.0.62:5140' in original_url:
            formatted_names[original_url] = "汽摩"
        elif '/udp/239.93.0.116:9136' in original_url:
            formatted_names[original_url] = "财富天下"
        elif '/udp/239.93.0.141:5140' in original_url:
            formatted_names[original_url] = "股评汇"
        elif '/udp/239.93.0.135:9008' in original_url:
            formatted_names[original_url] = "爱体育"
        elif '/udp/239.93.1.135:5140' in original_url:
            formatted_names[original_url] = "电竞天堂"
        elif '/udp/239.93.0.136:5140' in original_url:
            formatted_names[original_url] = "游戏风云"
        elif '/udp/239.93.0.117:1292' in original_url:
            formatted_names[original_url] = "汽车频道"
        elif '/udp/239.93.0.197:9040' in original_url:
            formatted_names[original_url] = "足球"
        elif '/udp/239.93.0.202:9068' in original_url:
            formatted_names[original_url] = "高网"
        elif '/udp/239.93.0.203:9072' in original_url:
            formatted_names[original_url] = "台球"
        elif '/udp/239.93.1.154:5140' in original_url:
            formatted_names[original_url] = "纪实人文"
        elif '/udp/239.93.0.215:9132' in original_url:
            formatted_names[original_url] = "墨宝"
        elif '/udp/239.93.0.204:9076' in original_url:
            formatted_names[original_url] = "军事"
        elif '/udp/239.93.0.199:9048' in original_url:
            formatted_names[original_url] = "解密"
        elif '/udp/239.93.0.200:9052' in original_url:
            formatted_names[original_url] = "地理"
        elif '/udp/239.93.0.235:1282' in original_url:
            formatted_names[original_url] = "传奇"
        elif '/udp/239.93.0.195:8012' in original_url:
            formatted_names[original_url] = "收视指南"
        elif '/udp/239.93.0.236:1283' in original_url:
            formatted_names[original_url] = "资讯新干线"
        elif '/udp/239.93.0.91:2101' in original_url:
            formatted_names[original_url] = "蓉城先锋"
        elif '/udp/239.93.1.171:5140' in original_url:
            formatted_names[original_url] = "星空精选"
        elif '/udp/239.93.42.35:5140' in original_url:
            formatted_names[original_url] = "百姓健康"
        elif '/udp/239.93.42.31:5140' in original_url:
            formatted_names[original_url] = "环球旅游"
        elif '/udp/239.93.42.8:5140' in original_url:
            formatted_names[original_url] = "来钓鱼吧"
        elif '/udp/239.93.42.2:5140' in original_url:
            formatted_names[original_url] = "麻辣体育"
        elif '/udp/239.93.42.33:5140' in original_url:
            formatted_names[original_url] = "绚影4K"
        elif '/udp/239.93.42.56:5140' in original_url:
            formatted_names[original_url] = "先锋乒羽"
        elif '/udp/239.93.42.55:5140' in original_url:
            formatted_names[original_url] = "天元围棋"
        elif '/udp/239.93.1.151:5140' in original_url:
            formatted_names[original_url] = "快乐垂钓"
        elif '/udp/239.93.0.114:5140' in original_url:
            formatted_names[original_url] = "茶频道"
        elif '/udp/239.93.1.198:5140' in original_url:
            formatted_names[original_url] = "热血剧场"
        elif '/udp/239.93.1.179:5140' in original_url:
            formatted_names[original_url] = "乐龄学堂"
        elif '/udp/239.93.1.191:5140' in original_url:
            formatted_names[original_url] = "亲子趣学4K"
        elif '/udp/239.93.1.197:5140' in original_url:
            formatted_names[original_url] = "津津悦读4K"
        elif '/udp/239.93.1.177:5140' in original_url:
            formatted_names[original_url] = "动画番剧"
        elif '/udp/239.93.1.188:5140' in original_url:
            formatted_names[original_url] = "中录动漫4K"
        elif '/udp/239.93.1.178:5140' in original_url:
            formatted_names[original_url] = "熊猫24小时"
        elif '/udp/239.93.1.175:5140' in original_url:
            formatted_names[original_url] = "综艺咖秀"
        elif '/udp/239.93.1.176:5140' in original_url:
            formatted_names[original_url] = "红色经典"
            
            

         

           



          

                    








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
        file.write("\n#四川,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

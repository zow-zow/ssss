import requests
import re
import time
import concurrent.futures


# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSJoZWZlaSI%3D&page=1&page_size=20', 
         'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249ImFuaHVpIg%3D%3D&page=1&page_size=20',


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
        for suffix in ['/rtp/238.1.79.27:4328','/rtp/238.1.79.44:4464','/rtp/238.1.79.42:4448','/rtp/238.1.79.43:4456','/rtp/238.1.79.41:4440','/rtp/238.1.79.40:4432','/rtp/238.1.79.45:4472','/rtp/238.1.78.61:6360','/rtp/238.1.79.66:4664','/rtp/238.1.79.50:4512','/rtp/238.1.79.32:4368','/rtp/238.1.79.33:4376','/rtp/238.1.79.34:4384','/rtp/238.1.78.74:6464','/rtp/238.1.78.76:6480','/rtp/238.1.78.81:6520','/rtp/238.1.78.84:6544','/rtp/238.1.78.85:6552','/rtp/238.1.78.111:6760','/rtp/238.1.78.183:7336','/rtp/238.1.78.184:7344','/rtp/238.1.78.185:7352','/rtp/238.1.78.182:7328','/rtp/238.1.78.132:6928','/rtp/238.1.78.133:6936','/rtp/238.1.78.134:6944','/rtp/238.1.78.203:7496','/rtp/238.1.78.204:7504','/rtp/238.1.78.205:7512','/rtp/238.1.78.207:7528','/rtp/238.1.78.208:7536','/rtp/238.1.78.112:6768','/rtp/238.1.78.80:6512','/rtp/238.1.78.152:7088','/rtp/238.1.78.167:7208','/rtp/238.1.78.187:7368','/rtp/238.1.78.190:7392','/rtp/238.1.78.188:7376','/rtp/238.1.78.189:7384','/rtp/238.1.79.15:4232','/rtp/238.1.78.77:6488','/rtp/238.1.78.117:6808','/rtp/238.1.78.118:6816','/rtp/238.1.78.120:6832','/rtp/238.1.78.192:7408','/rtp/238.1.78.28:6152','/rtp/238.1.79.12:4208','/rtp/238.1.78.130:6912','/rtp/238.1.78.131:6920','/rtp/238.1.78.138:6976','/rtp/238.1.78.199:7464','/rtp/238.1.78.200:7472','/rtp/238.1.79.20:4272','/rtp/238.1.79.14:4224','/rtp/238.1.78.149:7064','/rtp/238.1.78.142:7008','/rtp/238.1.78.143:7016','/rtp/238.1.78.212:7568','/rtp/238.1.78.213:7576','/rtp/238.1.78.214:7584','/rtp/238.1.78.215:7592','/rtp/238.1.78.216:7600','/rtp/238.1.78.218:7616','/rtp/238.1.78.147:7048','/rtp/238.1.78.148:7056','/rtp/238.1.78.221:7640','/rtp/238.1.79.13:4216','/rtp/238.1.78.139:6984','/rtp/238.1.78.140:6992','/rtp/238.1.78.141:7000','/rtp/238.1.78.211:7560','/rtp/238.1.78.210:7552','/rtp/238.1.78.144:7024','/rtp/238.1.78.145:7032','/rtp/238.1.78.220:7632','/rtp/238.1.78.119:6824','/rtp/238.1.79.21:4280','/rtp/238.1.78.113:6776','/rtp/238.1.78.114:6784','/rtp/238.1.78.146:7040','/rtp/238.1.78.135:6952','/rtp/238.1.78.136:6960','/rtp/238.1.78.137:6968','/rtp/238.1.78.209:7544','/rtp/238.1.78.121:6840','/rtp/238.1.78.122:6848','/rtp/238.1.78.123:6856','/rtp/238.1.79.46:4480','/rtp/238.1.78.193:7416','/rtp/238.1.78.180:7312','/rtp/238.1.78.181:7320','/rtp/238.1.79.52:4528','/rtp/238.1.79.47:4488','/rtp/238.1.78.124:6864','/rtp/238.1.78.125:6872','/rtp/238.1.78.126:6880','/rtp/238.1.78.127:6888','/rtp/238.1.78.194:7424','/rtp/238.1.78.195:7432','/rtp/238.1.78.29:6160','/rtp/238.1.79.11:4200','/rtp/238.1.78.128:6896','/rtp/238.1.78.129:6904','/rtp/238.1.78.196:7440','/rtp/238.1.78.197:7448','/rtp/238.1.79.19:4264',]:
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
        elif '/rtp/238.1.79.27:4328' in original_url:
            formatted_names[original_url] = "安徽卫视HD"
        elif '/rtp/238.1.79.44:4464' in original_url:
            formatted_names[original_url] = "安徽经济生活HD"
        elif '/rtp/238.1.79.42:4448' in original_url:
            formatted_names[original_url] = "安徽影视频道HD"
        elif '/rtp/238.1.79.43:4456' in original_url:
            formatted_names[original_url] = "安徽公共频道HD"
        elif '/rtp/238.1.79.41:4440' in original_url:
            formatted_names[original_url] = "安徽综艺体育HD"
        elif '/rtp/238.1.79.40:4432' in original_url:
            formatted_names[original_url] = "安徽农业科教HD"
        elif '/rtp/238.1.79.45:4472' in original_url:
            formatted_names[original_url] = "安徽人物频道HD"
        elif '/rtp/238.1.78.61:6360' in original_url:
            formatted_names[original_url] = "安徽国际频道"
        elif '/rtp/238.1.79.66:4664' in original_url:
            formatted_names[original_url] = "安徽导视频道"
        elif '/rtp/238.1.79.50:4512' in original_url:
            formatted_names[original_url] = "海豚生活HD"
        elif '/rtp/238.1.79.32:4368' in original_url:
            formatted_names[original_url] = "海豚少儿HD"
        elif '/rtp/238.1.79.33:4376' in original_url:
            formatted_names[original_url] = "海豚健康HD"
        elif '/rtp/238.1.79.34:4384' in original_url:
            formatted_names[original_url] = "海豚影视HD"
        elif '/rtp/238.1.78.74:6464' in original_url:
            formatted_names[original_url] = "都市剧场"
        elif '/rtp/238.1.78.76:6480' in original_url:
            formatted_names[original_url] = "金色频道"
        elif '/rtp/238.1.78.81:6520' in original_url:
            formatted_names[original_url] = "游戏风云"
        elif '/rtp/238.1.78.84:6544' in original_url:
            formatted_names[original_url] = "法治天地"
        elif '/rtp/238.1.78.85:6552' in original_url:
            formatted_names[original_url] = "七彩戏剧"
        elif '/rtp/238.1.78.111:6760' in original_url:
            formatted_names[original_url] = "合肥新闻频道"
        elif '/rtp/238.1.78.183:7336' in original_url:
            formatted_names[original_url] = "肥东新闻综合"
        elif '/rtp/238.1.78.184:7344' in original_url:
            formatted_names[original_url] = "肥东经济生活"
        elif '/rtp/238.1.78.185:7352' in original_url:
            formatted_names[original_url] = "肥西新闻综合"
        elif '/rtp/238.1.78.182:7328' in original_url:
            formatted_names[original_url] = "长丰电视台"
        elif '/rtp/238.1.78.132:6928' in original_url:
            formatted_names[original_url] = "滁州新闻综合"
        elif '/rtp/238.1.78.133:6936' in original_url:
            formatted_names[original_url] = "滁州公共频道"
        elif '/rtp/238.1.78.134:6944' in original_url:
            formatted_names[original_url] = "滁州科教频道"
        elif '/rtp/238.1.78.203:7496' in original_url:
            formatted_names[original_url] = "全椒综合频道"
        elif '/rtp/238.1.78.204:7504' in original_url:
            formatted_names[original_url] = "来安新闻综合"
        elif '/rtp/238.1.78.205:7512' in original_url:
            formatted_names[original_url] = "定远新闻综合"
        elif '/rtp/238.1.78.207:7528' in original_url:
            formatted_names[original_url] = "凤阳新闻频道"
        elif '/rtp/238.1.78.208:7536' in original_url:
            formatted_names[original_url] = "明光综合频道"
        elif '/rtp/238.1.78.112:6768' in original_url:
            formatted_names[original_url] = "芜湖新闻综合"
        elif '/rtp/238.1.78.80:6512' in original_url:
            formatted_names[original_url] = "芜湖公共频道"
        elif '/rtp/238.1.78.152:7088' in original_url:
            formatted_names[original_url] = "芜湖生活频道"
        elif '/rtp/238.1.78.167:7208' in original_url:
            formatted_names[original_url] = "芜湖教育频道"
        elif '/rtp/238.1.78.187:7368' in original_url:
            formatted_names[original_url] = "湾沚新闻综合"
        elif '/rtp/238.1.78.190:7392' in original_url:
            formatted_names[original_url] = "繁昌新闻综合"
        elif '/rtp/238.1.78.188:7376' in original_url:
            formatted_names[original_url] = "无为新闻频道"
        elif '/rtp/238.1.78.189:7384' in original_url:
            formatted_names[original_url] = "南陵新闻综合"
        elif '/rtp/238.1.79.15:4232' in original_url:
            formatted_names[original_url] = "马鞍山新闻综合"
        elif '/rtp/238.1.78.77:6488' in original_url:
            formatted_names[original_url] = "马鞍山公共频道"
        elif '/rtp/238.1.78.117:6808' in original_url:
            formatted_names[original_url] = "安庆新闻综合"
        elif '/rtp/238.1.78.118:6816' in original_url:
            formatted_names[original_url] = "安庆公共频道"
        elif '/rtp/238.1.78.120:6832' in original_url:
            formatted_names[original_url] = "安庆教育频道"
        elif '/rtp/238.1.78.192:7408' in original_url:
            formatted_names[original_url] = "潜山综合频道"
        elif '/rtp/238.1.78.28:6152' in original_url:
            formatted_names[original_url] = "桐城综合频道"
        elif '/rtp/238.1.79.12:4208' in original_url:
            formatted_names[original_url] = "太湖新闻综合"
        elif '/rtp/238.1.78.130:6912' in original_url:
            formatted_names[original_url] = "黄山新闻综合"
        elif '/rtp/238.1.78.131:6920' in original_url:
            formatted_names[original_url] = "黄山公共频道"
        elif '/rtp/238.1.78.138:6976' in original_url:
            formatted_names[original_url] = "徽州新闻频道"
        elif '/rtp/238.1.78.199:7464' in original_url:
            formatted_names[original_url] = "太平电视台"
        elif '/rtp/238.1.78.200:7472' in original_url:
            formatted_names[original_url] = "歙县综合频道"
        elif '/rtp/238.1.79.20:4272' in original_url:
            formatted_names[original_url] = "休宁新闻综合"
        elif '/rtp/238.1.79.14:4224' in original_url:
            formatted_names[original_url] = "祁门综合频道"
        elif '/rtp/238.1.78.149:7064' in original_url:
            formatted_names[original_url] = "黟县新闻综合"
        elif '/rtp/238.1.78.142:7008' in original_url:
            formatted_names[original_url] = "宣城综合频道"
        elif '/rtp/238.1.78.143:7016' in original_url:
            formatted_names[original_url] = "宣城公共频道"
        elif '/rtp/238.1.78.212:7568' in original_url:
            formatted_names[original_url] = "广德新闻综合"
        elif '/rtp/238.1.78.213:7576' in original_url:
            formatted_names[original_url] = "广德生活频道"
        elif '/rtp/238.1.78.214:7584' in original_url:
            formatted_names[original_url] = "郎溪新闻频道"
        elif '/rtp/238.1.78.215:7592' in original_url:
            formatted_names[original_url] = "旌德新闻综合"
        elif '/rtp/238.1.78.216:7600' in original_url:
            formatted_names[original_url] = "宁国新闻综合"
        elif '/rtp/238.1.78.218:7616' in original_url:
            formatted_names[original_url] = "绩溪新闻频道"
        elif '/rtp/238.1.78.147:7048' in original_url:
            formatted_names[original_url] = "池州新闻综合"
        elif '/rtp/238.1.78.148:7056' in original_url:
            formatted_names[original_url] = "池州公共频道"
        elif '/rtp/238.1.78.221:7640' in original_url:
            formatted_names[original_url] = "石台综合频道"
        elif '/rtp/238.1.79.13:4216' in original_url:
            formatted_names[original_url] = "东至综合频道"
        elif '/rtp/238.1.78.139:6984' in original_url:
            formatted_names[original_url] = "铜陵新闻综合"
        elif '/rtp/238.1.78.140:6992' in original_url:
            formatted_names[original_url] = "铜陵公共频道"
        elif '/rtp/238.1.78.141:7000' in original_url:
            formatted_names[original_url] = "铜陵科教频道"
        elif '/rtp/238.1.78.211:7560' in original_url:
            formatted_names[original_url] = "义安新闻综合"
        elif '/rtp/238.1.78.210:7552' in original_url:
            formatted_names[original_url] = "枞阳电视台"
        elif '/rtp/238.1.78.144:7024' in original_url:
            formatted_names[original_url] = "六安综合频道"
        elif '/rtp/238.1.78.145:7032' in original_url:
            formatted_names[original_url] = "六安公共频道"
        elif '/rtp/238.1.78.220:7632' in original_url:
            formatted_names[original_url] = "霍山综合频道"
        elif '/rtp/238.1.78.119:6824' in original_url:
            formatted_names[original_url] = "霍邱新闻综合"
        elif '/rtp/238.1.79.21:4280' in original_url:
            formatted_names[original_url] = "金寨综合频道"
        elif '/rtp/238.1.78.113:6776' in original_url:
            formatted_names[original_url] = "淮南新闻综合"
        elif '/rtp/238.1.78.114:6784' in original_url:
            formatted_names[original_url] = "淮南公共频道"
        elif '/rtp/238.1.78.146:7040' in original_url:
            formatted_names[original_url] = "寿县新闻综合"
        elif '/rtp/238.1.78.135:6952' in original_url:
            formatted_names[original_url] = "淮北新闻综合"
        elif '/rtp/238.1.78.136:6960' in original_url:
            formatted_names[original_url] = "淮北公共频道"
        elif '/rtp/238.1.78.137:6968' in original_url:
            formatted_names[original_url] = "淮北教育频道"
        elif '/rtp/238.1.78.209:7544' in original_url:
            formatted_names[original_url] = "濉溪新闻频道"
        elif '/rtp/238.1.78.121:6840' in original_url:
            formatted_names[original_url] = "宿州新闻综合"
        elif '/rtp/238.1.78.122:6848' in original_url:
            formatted_names[original_url] = "宿州公共频道"
        elif '/rtp/238.1.78.123:6856' in original_url:
            formatted_names[original_url] = "宿州科教频道"
        elif '/rtp/238.1.79.46:4480' in original_url:
            formatted_names[original_url] = "萧县新闻综合"
        elif '/rtp/238.1.78.193:7416' in original_url:
            formatted_names[original_url] = "泗县新闻频道"
        elif '/rtp/238.1.78.180:7312' in original_url:
            formatted_names[original_url] = "蚌埠新闻综合"
        elif '/rtp/238.1.78.181:7320' in original_url:
            formatted_names[original_url] = "蚌埠公共频道"
        elif '/rtp/238.1.79.52:4528' in original_url:
            formatted_names[original_url] = "五河新闻综合"
        elif '/rtp/238.1.79.47:4488' in original_url:
            formatted_names[original_url] = "固镇新闻综合"
        elif '/rtp/238.1.78.124:6864' in original_url:
            formatted_names[original_url] = "阜阳新闻综合"
        elif '/rtp/238.1.78.125:6872' in original_url:
            formatted_names[original_url] = "阜阳公共频道"
        elif '/rtp/238.1.78.126:6880' in original_url:
            formatted_names[original_url] = "阜阳教育频道"
        elif '/rtp/238.1.78.127:6888' in original_url:
            formatted_names[original_url] = "阜阳都市频道"
        elif '/rtp/238.1.78.194:7424' in original_url:
            formatted_names[original_url] = "颍上新闻综合"
        elif '/rtp/238.1.78.195:7432' in original_url:
            formatted_names[original_url] = "界首综合频道"
        elif '/rtp/238.1.78.29:6160' in original_url:
            formatted_names[original_url] = "临泉新闻频道"
        elif '/rtp/238.1.79.11:4200' in original_url:
            formatted_names[original_url] = "阜南新闻综合"
        elif '/rtp/238.1.78.128:6896' in original_url:
            formatted_names[original_url] = "亳州综合频道"
        elif '/rtp/238.1.78.129:6904' in original_url:
            formatted_names[original_url] = "亳州农村频道"
        elif '/rtp/238.1.78.196:7440' in original_url:
            formatted_names[original_url] = "利辛新闻综合"
        elif '/rtp/238.1.78.197:7448' in original_url:
            formatted_names[original_url] = "涡阳新闻综合"
        elif '/rtp/238.1.79.19:4264' in original_url:
            formatted_names[original_url] = "蒙城新闻频道"














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
        file.write("\n#安徽,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()

import requests
import re
import time
import concurrent.futures

# 定义初始URL列表
urls = ['https://fofa.info/result?qbase64=InVkcHh5IiAmJiBjaXR5PSIgVGFuZ3NoYW4i&page=1&page_size=20',
        'https://fofa.info/result?qbase64=InVkcHh5IiAmJiByZWdpb249ImhlYmVpIg%3D%3D&page=1&page_size=20',





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
        for suffix in ['/rtp/239.253.92.172:6002','/rtp/239.253.92.175:6005','/rtp/239.253.92.171:6001','/rtp/239.253.92.176:6006','/rtp/239.253.92.173:6003','/rtp/239.253.92.174:6004','/rtp/239.253.92.128:6028','/rtp/239.253.92.127:6027','/rtp/239.253.92.245:6089','/rtp/239.253.92.126:6026','/rtp/239.253.93.4:6157','/rtp/239.253.93.2:6153','/rtp/239.253.93.5:6158','/rtp/239.253.92.93:8120','/rtp/239.253.92.149:6035','/rtp/239.253.92.94:8121','/rtp/239.253.92.95:8122','/rtp/239.253.92.52:6021','/rtp/239.253.92.53:6022','/rtp/239.253.92.54:6023','/rtp/239.253.93.12:6165','/rtp/239.253.93.146:6314','/rtp/239.253.93.143:6311','/rtp/239.253.93.96:6262','/rtp/239.253.92.231:6070','/rtp/239.253.93.210:6388','/rtp/239.253.92.252:6156','/rtp/239.253.93.167:6335','/rtp/239.253.94.29:6628','/rtp/239.253.93.250:6290','/rtp/239.253.93.205:6383','/rtp/239.253.93.145:6313','/rtp/239.253.92.142:6040','/rtp/239.253.93.104:6271','/rtp/239.253.93.102:6268','/rtp/239.253.93.80:6246','/rtp/239.253.93.48:6201','/rtp/239.253.93.206:6384','/rtp/239.253.92.147:6224','/rtp/239.253.93.169:6337','/rtp/239.253.93.30:6183','/rtp/239.253.93.109:6276','/rtp/239.253.92.253:6244','/rtp/239.253.93.186:6354','/rtp/239.253.92.230:6068','/rtp/239.253.93.51:6204','/rtp/239.253.93.36:6189','/rtp/239.253.93.107:6274','/rtp/239.253.93.14:6167','/rtp/239.253.93.95:6260','/rtp/239.253.93.117:6019','/rtp/239.253.93.163:6331','/rtp/239.253.93.147:6315','/rtp/239.253.92.254:6449','/rtp/239.253.93.53:6206','/rtp/239.253.92.156:6012','/rtp/239.253.93.50:6203','/rtp/239.253.93.66:6231','/rtp/239.253.93.165:6333','/rtp/239.253.92.121:6015','/rtp/239.253.92.164:6036','/rtp/239.253.93.159:6327','/rtp/239.253.92.226:8116','/rtp/239.253.92.225:8115','/rtp/239.253.93.182:6350','/rtp/239.253.93.178:6346','/rtp/239.253.92.223:8113','/rtp/239.253.92.222:8112','/rtp/239.253.94.28:6627','/rtp/239.253.93.201:6379','/rtp/239.253.93.161:6329','/rtp/239.253.93.111:6278','/rtp/239.253.92.138:6222','/rtp/239.253.92.109:6217','/rtp/239.253.93.156:6324','/rtp/239.253.93.38:6191','/rtp/239.253.93.54:6207','/rtp/239.253.93.31:6184','/rtp/239.253.93.32:6185','/rtp/239.253.93.166:6334','/rtp/239.253.93.171:6339','/rtp/239.253.92.187:6051','/rtp/239.253.93.62:6215','/rtp/239.253.93.79:6245','/rtp/239.253.93.172:6340','/rtp/239.253.93.179:6347','/rtp/239.253.92.122:6016','/rtp/239.253.92.123:6017','/rtp/239.253.92.121:6015','/rtp/239.253.93.106:6273','/rtp/239.253.93.16:6169','/rtp/239.253.93.17:6170','/rtp/239.253.93.22:6175','/rtp/239.253.93.27:6180','/rtp/239.253.93.181:6349','/rtp/239.253.93.42:6195','/rtp/239.253.94.31:6630','/rtp/239.253.93.19:6172','/rtp/239.253.92.218:6100','/rtp/239.253.92.97:6138','/rtp/239.253.92.100:6142','/rtp/239.253.92.118:6133','/rtp/239.253.93.144:6312','/rtp/239.253.92.215:6067','/rtp/239.253.93.34:6187','/rtp/239.253.93.152:6320','/rtp/239.253.93.7:6160','/rtp/239.253.93.3:6154','/rtp/239.253.92.12:6042','/rtp/239.253.93.160:6328','/rtp/239.253.93.140:6308','/rtp/239.253.92.247:6091','/rtp/239.253.93.113:6280','/rtp/239.253.93.177:6345','/rtp/239.253.93.10:6163','/rtp/239.253.93.8:6161','/rtp/239.253.93.13:6166','/rtp/239.253.93.11:6164','/rtp/239.253.93.158:6326','/rtp/239.253.93.168:6336','/rtp/239.253.93.16:6169','/rtp/239.253.93.174:6342','/rtp/239.253.93.65:6230','/rtp/239.253.93.209:6387','/rtp/239.253.93.139:6307','/rtp/239.253.93.44:6197','/rtp/239.253.93.24:6177','/rtp/239.253.93.148:6316','/rtp/239.253.93.40:6193','/rtp/239.253.93.115:6282','/rtp/239.253.92.185:6049','/rtp/239.253.93.23:6176','/rtp/239.253.92.160:6041','/rtp/239.253.93.105:6272','/rtp/239.253.93.185:6353','/rtp/239.253.93.64:6219','/rtp/239.253.92.183:6047','/rtp/239.254.200.18:6000','/rtp/239.254.200.19:6000','/rtp/239.254.200.20:6000','/rtp/239.254.200.21:6000','/rtp/239.254.200.22:6000','/rtp/239.254.200.23:6000','/rtp/239.254.200.27:6000','/rtp/239.254.201.139:7203','/rtp/239.254.200.157:6000','/rtp/239.254.200.29:6000','/rtp/239.254.200.30:6000','/rtp/239.254.200.31:6000','/rtp/239.254.200.32:6000','/rtp/239.254.200.33:6000','/rtp/239.254.200.35:6000','/rtp/239.254.200.36:6000','/rtp/239.254.200.39:6000','/rtp/239.254.200.40:6000','/rtp/239.254.200.41:6000','/rtp/239.254.200.166:6000','/rtp/239.254.200.167:6000','/rtp/239.254.200.168:6000','/rtp/239.254.200.169:6000','/rtp/239.254.200.183:6000','/rtp/239.254.200.184:6000','/rtp/239.254.200.42:6000','/rtp/239.254.200.43:6000','/rtp/239.254.200.44:6000','/rtp/239.254.200.144:6000','/rtp/239.254.200.145:6000','/rtp/239.254.200.146:6000','/rtp/239.254.200.147:6000','/rtp/239.254.200.149:6000','/rtp/239.254.200.150:6000','/rtp/239.254.200.152:6000','/rtp/239.254.200.153:6000','/rtp/239.254.200.154:6000','/rtp/239.254.200.155:6000','/rtp/239.254.200.191:5169','/rtp/239.254.200.220:5167','/rtp/239.254.201.24:5170','/rtp/239.254.200.215:5173','/rtp/239.254.201.14:5175','/rtp/239.254.200.244:5177','/rtp/239.254.201.108:5180','/rtp/239.254.201.111:5183','/rtp/239.254.201.127:5184','/rtp/239.254.201.215:6167','/rtp/239.254.200.177:5286','/rtp/239.254.201.4:5291','/rtp/239.254.201.63:5293','/rtp/239.254.201.95:5295','/rtp/239.254.201.142:5296','/rtp/239.254.201.204:6166','/rtp/239.254.201.115:5381','/rtp/239.254.201.116:5225','/rtp/239.254.201.117:5267','/rtp/239.254.201.118:6257','/rtp/239.254.201.130:5271','/rtp/239.254.201.129:6209','/rtp/239.254.201.131:5269','/rtp/239.254.201.135:5270','/rtp/239.254.201.146:5202','/rtp/239.254.201.61:5230','/rtp/239.254.201.213:5232','/rtp/239.254.201.216:5233','/rtp/239.254.200.218:5186','/rtp/239.254.201.26:5188','/rtp/239.254.201.22:5191','/rtp/239.254.201.28:5194','/rtp/239.254.201.30:5196','/rtp/239.254.201.32:5306','/rtp/239.254.201.34:5308','/rtp/239.254.201.71:5310','/rtp/239.254.201.101:5312','/rtp/239.254.201.103:5314','/rtp/239.254.201.113:5315','/rtp/239.254.201.141:5316','/rtp/239.254.201.143:6210','/rtp/239.254.201.148:6211','/rtp/239.254.200.4:5313','/rtp/239.254.201.35:5327','/rtp/239.254.201.36:5325','/rtp/239.254.201.38:5329','/rtp/239.254.201.76:5331','/rtp/239.254.201.112:5333','/rtp/239.254.201.114:5334','/rtp/239.254.201.119:5335','/rtp/239.254.201.122:5336','/rtp/239.254.201.138:5337','/rtp/239.254.200.5:5290','/rtp/239.254.200.172:5246','/rtp/239.254.201.40:5248','/rtp/239.254.201.10:5250','/rtp/239.254.200.222:5252','/rtp/239.254.200.213:5260','/rtp/239.254.200.210:5254','/rtp/239.254.201.17:5261','/rtp/239.254.201.41:5264','/rtp/239.254.200.242:5265','/rtp/239.254.201.56:6246','/rtp/239.254.201.74:6251','/rtp/239.254.201.94:6254','/rtp/239.254.201.96:6253','/rtp/239.254.201.99:6255','/rtp/239.254.201.102:6256','/rtp/239.254.201.140:5383','/rtp/239.254.201.145:5272','/rtp/239.254.201.147:6260','/rtp/239.254.201.149:6212','/rtp/239.254.200.179:5346','/rtp/239.254.201.42:5348','/rtp/239.254.200.240:5350','/rtp/239.254.201.44:5353','/rtp/239.254.201.46:5357','/rtp/239.254.201.8:5355','/rtp/239.254.201.98:5361','/rtp/239.254.201.126:5362','/rtp/239.254.201.136:5363','/rtp/239.254.200.170:5366','/rtp/239.254.201.50:5373','/rtp/239.254.201.6:5216','/rtp/239.254.201.51:5375','/rtp/239.254.201.53:5378','/rtp/239.254.201.60:5218','/rtp/239.254.201.69:5379','/rtp/239.254.201.70:5220','/rtp/239.254.201.72:6000','/rtp/239.254.201.73:5221','/rtp/239.254.201.77:5380','/rtp/239.254.201.97:5222','/rtp/239.254.201.109:5199','/rtp/239.254.201.105:5223','/rtp/239.254.201.106:5224','/rtp/239.254.201.107:5200','/rtp/239.254.200.181:5369','/rtp/239.254.200.236:5210','/rtp/239.254.201.48:5371','/rtp/239.254.201.58:5197',]:
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
        elif '/rtp/239.253.92.172:6002' in original_url:
            formatted_names[original_url] = "河北都市"
        elif '/rtp/239.253.92.175:6005' in original_url:
            formatted_names[original_url] = "河北公共"
        elif '/rtp/239.253.92.171:6001' in original_url:
            formatted_names[original_url] = "河北经济"
        elif '/rtp/239.253.92.176:6006' in original_url:
            formatted_names[original_url] = "河北农民"
        elif '/rtp/239.253.92.173:6003' in original_url:
            formatted_names[original_url] = "河北影视"
        elif '/rtp/239.253.92.174:6004' in original_url:
            formatted_names[original_url] = "河北少儿"
        elif '/rtp/239.253.92.128:6028' in original_url:
            formatted_names[original_url] = "唐山公共"
        elif '/rtp/239.253.92.127:6027' in original_url:
            formatted_names[original_url] = "唐山影视"
        elif '/rtp/239.253.92.245:6089' in original_url:
            formatted_names[original_url] = "唐山新闻"
        elif '/rtp/239.253.92.126:6026' in original_url:
            formatted_names[original_url] = "唐山生活"
        elif '/rtp/239.253.93.4:6157' in original_url:
            formatted_names[original_url] = "保定公共"
        elif '/rtp/239.253.93.2:6153' in original_url:
            formatted_names[original_url] = "保定新闻"
        elif '/rtp/239.253.93.5:6158' in original_url:
            formatted_names[original_url] = "保定生活"
        elif '/rtp/239.253.92.93:8120' in original_url:
            formatted_names[original_url] = "石家庄娱乐"
        elif '/rtp/239.253.92.149:6035' in original_url:
            formatted_names[original_url] = "石家庄新闻"
        elif '/rtp/239.253.92.94:8121' in original_url:
            formatted_names[original_url] = "石家庄生活"
        elif '/rtp/239.253.92.95:8122' in original_url:
            formatted_names[original_url] = "石家庄都市"
        elif '/rtp/239.253.92.52:6021' in original_url:
            formatted_names[original_url] = "秦皇岛新闻"
        elif '/rtp/239.253.92.53:6022' in original_url:
            formatted_names[original_url] = "秦皇岛公共"
        elif '/rtp/239.253.92.54:6023' in original_url:
            formatted_names[original_url] = "秦皇岛影视"
        elif '/rtp/239.253.93.12:6165' in original_url:
            formatted_names[original_url] = "邯郸公共"
        elif '/rtp/239.253.93.146:6314' in original_url:
            formatted_names[original_url] = "邯山综合"
        elif '/rtp/239.253.93.143:6311' in original_url:
            formatted_names[original_url] = "三河综合"
        elif '/rtp/239.253.93.96:6262' in original_url:
            formatted_names[original_url] = "东光综合"
        elif '/rtp/239.253.92.231:6070' in original_url:
            formatted_names[original_url] = "丰南电视"
        elif '/rtp/239.253.93.210:6388' in original_url:
            formatted_names[original_url] = "丰宁综合"
        elif '/rtp/239.253.92.252:6156' in original_url:
            formatted_names[original_url] = "丰润新闻"
        elif '/rtp/239.253.93.167:6335' in original_url:
            formatted_names[original_url] = "临城新闻"
        elif '/rtp/239.253.94.29:6628' in original_url:
            formatted_names[original_url] = "临西综合"
        elif '/rtp/239.253.93.250:6290' in original_url:
            formatted_names[original_url] = "乐亭融媒"
        elif '/rtp/239.253.93.205:6383' in original_url:
            formatted_names[original_url] = "井陉综合"
        elif '/rtp/239.253.93.145:6313' in original_url:
            formatted_names[original_url] = "任泽电视"
        elif '/rtp/239.253.92.142:6040' in original_url:
            formatted_names[original_url] = "元氏电视"
        elif '/rtp/239.253.93.104:6271' in original_url:
            formatted_names[original_url] = "兴隆综合"
        elif '/rtp/239.253.93.102:6268' in original_url:
            formatted_names[original_url] = "内丘电视"
        elif '/rtp/239.253.93.80:6246' in original_url:
            formatted_names[original_url] = "南和综合"
        elif '/rtp/239.253.93.48:6201' in original_url:
            formatted_names[original_url] = "南宫电视"
        elif '/rtp/239.253.93.206:6384' in original_url:
            formatted_names[original_url] = "卢龙电视"
        elif '/rtp/239.253.92.147:6224' in original_url:
            formatted_names[original_url] = "双滦新闻"
        elif '/rtp/239.253.93.169:6337' in original_url:
            formatted_names[original_url] = "吴桥综合"
        elif '/rtp/239.253.93.30:6183' in original_url:
            formatted_names[original_url] = "唐县综合"
        elif '/rtp/239.253.93.109:6276' in original_url:
            formatted_names[original_url] = "固安综合"
        elif '/rtp/239.253.92.253:6244' in original_url:
            formatted_names[original_url] = "大厂融媒"
        elif '/rtp/239.253.93.186:6354' in original_url:
            formatted_names[original_url] = "大名新闻"
        elif '/rtp/239.253.92.230:6068' in original_url:
            formatted_names[original_url] = "大成电视"
        elif '/rtp/239.253.93.51:6204' in original_url:
            formatted_names[original_url] = "宁普电视"
        elif '/rtp/239.253.93.36:6189' in original_url:
            formatted_names[original_url] = "安平综合"
        elif '/rtp/239.253.93.107:6274' in original_url:
            formatted_names[original_url] = "安新综合"
        elif '/rtp/239.253.93.14:6167' in original_url:
            formatted_names[original_url] = "定兴电视"
        elif '/rtp/239.253.93.95:6260' in original_url:
            formatted_names[original_url] = "定州新闻"
        elif '/rtp/239.253.93.117:6019' in original_url:
            formatted_names[original_url] = "宽城综合"
        elif '/rtp/239.253.93.163:6331' in original_url:
            formatted_names[original_url] = "尚义电视"
        elif '/rtp/239.253.93.147:6315' in original_url:
            formatted_names[original_url] = "崇礼融媒"
        elif '/rtp/239.253.92.254:6449' in original_url:
            formatted_names[original_url] = "巨鹿新闻"
        elif '/rtp/239.253.93.53:6206' in original_url:
            formatted_names[original_url] = "平乡电视"
        elif '/rtp/239.253.92.156:6012' in original_url:
            formatted_names[original_url] = "平泉综合"
        elif '/rtp/239.253.93.50:6203' in original_url:
            formatted_names[original_url] = "广宗电视"
        elif '/rtp/239.253.93.66:6231' in original_url:
            formatted_names[original_url] = "广平新闻"
        elif '/rtp/239.253.93.165:6333' in original_url:
            formatted_names[original_url] = "康保综合"
        elif '/rtp/239.253.92.121:6015' in original_url:
            formatted_names[original_url] = "廊坊公共"
        elif '/rtp/239.253.92.164:6036' in original_url:
            formatted_names[original_url] = "廊坊新闻"
        elif '/rtp/239.253.93.159:6327' in original_url:
            formatted_names[original_url] = "张北电视"
        elif '/rtp/239.253.92.226:8116' in original_url:
            formatted_names[original_url] = "张家口公共"
        elif '/rtp/239.253.92.225:8115' in original_url:
            formatted_names[original_url] = "张家口新闻"
        elif '/rtp/239.253.93.182:6350' in original_url:
            formatted_names[original_url] = "徐水电视"
        elif '/rtp/239.253.93.178:6346' in original_url:
            formatted_names[original_url] = "成安综合"
        elif '/rtp/239.253.92.223:8113' in original_url:
            formatted_names[original_url] = "承德公共"
        elif '/rtp/239.253.92.222:8112' in original_url:
            formatted_names[original_url] = "承德新闻"
        elif '/rtp/239.253.94.28:6627' in original_url:
            formatted_names[original_url] = "承德电视"
        elif '/rtp/239.253.93.201:6379' in original_url:
            formatted_names[original_url] = "抚宁电视"
        elif '/rtp/239.253.93.161:6329' in original_url:
            formatted_names[original_url] = "故城电视"
        elif '/rtp/239.253.93.111:6278' in original_url:
            formatted_names[original_url] = "文安电视"
        elif '/rtp/239.253.92.138:6222' in original_url:
            formatted_names[original_url] = "无极新闻"
        elif '/rtp/239.253.92.109:6217' in original_url:
            formatted_names[original_url] = "昌黎电视"
        elif '/rtp/239.253.93.156:6324' in original_url:
            formatted_names[original_url] = "晋州综合"
        elif '/rtp/239.253.93.38:6191' in original_url:
            formatted_names[original_url] = "景县综合"
        elif '/rtp/239.253.93.54:6207' in original_url:
            formatted_names[original_url] = "曲周新闻"
        elif '/rtp/239.253.93.31:6184' in original_url:
            formatted_names[original_url] = "曲阳电视"
        elif '/rtp/239.253.93.32:6185' in original_url:
            formatted_names[original_url] = "望都电视"
        elif '/rtp/239.253.93.166:6334' in original_url:
            formatted_names[original_url] = "枣强综合"
        elif '/rtp/239.253.93.171:6339' in original_url:
            formatted_names[original_url] = "柏乡综合"
        elif '/rtp/239.253.92.187:6051' in original_url:
            formatted_names[original_url] = "栾城电视"
        elif '/rtp/239.253.93.62:6215' in original_url:
            formatted_names[original_url] = "武安新闻"
        elif '/rtp/239.253.93.79:6245' in original_url:
            formatted_names[original_url] = "武强融媒"
        elif '/rtp/239.253.93.172:6340' in original_url:
            formatted_names[original_url] = "永清电视"
        elif '/rtp/239.253.93.179:6347' in original_url:
            formatted_names[original_url] = "沙河综合"
        elif '/rtp/239.253.92.122:6016' in original_url:
            formatted_names[original_url] = "沧州公共"
        elif '/rtp/239.253.92.123:6017' in original_url:
            formatted_names[original_url] = "沧州影视"
        elif '/rtp/239.253.92.121:6015' in original_url:
            formatted_names[original_url] = "沧州新闻"
        elif '/rtp/239.253.93.106:6273' in original_url:
            formatted_names[original_url] = "涉县综合"
        elif '/rtp/239.253.93.16:6169' in original_url:
            formatted_names[original_url] = "涞水电视"
        elif '/rtp/239.253.93.17:6170' in original_url:
            formatted_names[original_url] = "涞水电视"
        elif '/rtp/239.253.93.22:6175' in original_url:
            formatted_names[original_url] = "涞源综合"
        elif '/rtp/239.253.93.27:6180' in original_url:
            formatted_names[original_url] = "涿州电视"
        elif '/rtp/239.253.93.181:6349' in original_url:
            formatted_names[original_url] = "涿鹿电视"
        elif '/rtp/239.253.93.42:6195' in original_url:
            formatted_names[original_url] = "深州综合"
        elif '/rtp/239.253.94.31:6630' in original_url:
            formatted_names[original_url] = "深泽综合"
        elif '/rtp/239.253.93.19:6172' in original_url:
            formatted_names[original_url] = "满城新闻"
        elif '/rtp/239.253.92.218:6100' in original_url:
            formatted_names[original_url] = "滦南综合"
        elif '/rtp/239.253.92.97:6138' in original_url:
            formatted_names[original_url] = "滦州综合"
        elif '/rtp/239.253.92.100:6142' in original_url:
            formatted_names[original_url] = "滦平新闻"
        elif '/rtp/239.253.92.118:6133' in original_url:
            formatted_names[original_url] = "玉田综合"
        elif '/rtp/239.253.93.144:6312' in original_url:
            formatted_names[original_url] = "盐山综合"
        elif '/rtp/239.253.92.215:6067' in original_url:
            formatted_names[original_url] = "矿区电视"
        elif '/rtp/239.253.93.34:6187' in original_url:
            formatted_names[original_url] = "翼州综合"
        elif '/rtp/239.253.93.152:6320' in original_url:
            formatted_names[original_url] = "肃宁电视"
        elif '/rtp/239.253.93.7:6160' in original_url:
            formatted_names[original_url] = "衡水公共"
        elif '/rtp/239.253.93.3:6154' in original_url:
            formatted_names[original_url] = "衡水新闻"
        elif '/rtp/239.253.92.12:6042' in original_url:
            formatted_names[original_url] = "赞皇电视"
        elif '/rtp/239.253.93.160:6328' in original_url:
            formatted_names[original_url] = "赤城电视"
        elif '/rtp/239.253.93.140:6308' in original_url:
            formatted_names[original_url] = "赵县电视"
        elif '/rtp/239.253.92.247:6091' in original_url:
            formatted_names[original_url] = "辽西综合"
        elif '/rtp/239.253.93.113:6280' in original_url:
            formatted_names[original_url] = "迁安综合"
        elif '/rtp/239.253.93.177:6345' in original_url:
            formatted_names[original_url] = "遵化综合"
        elif '/rtp/239.253.93.10:6163' in original_url:
            formatted_names[original_url] = "邢台城市"
        elif '/rtp/239.253.93.8:6161' in original_url:
            formatted_names[original_url] = "邢台综合"
        elif '/rtp/239.253.93.13:6166' in original_url:
            formatted_names[original_url] = "邯郸科技"
        elif '/rtp/239.253.93.11:6164' in original_url:
            formatted_names[original_url] = "邯鄣新闻"
        elif '/rtp/239.253.93.158:6326' in original_url:
            formatted_names[original_url] = "邱县电视"
        elif '/rtp/239.253.93.168:6336' in original_url:
            formatted_names[original_url] = "阜城综合"
        elif '/rtp/239.253.93.16:6169' in original_url:
            formatted_names[original_url] = "阜平电视"
        elif '/rtp/239.253.93.174:6342' in original_url:
            formatted_names[original_url] = "隆化综合"
        elif '/rtp/239.253.93.65:6230' in original_url:
            formatted_names[original_url] = "隆尧电视"
        elif '/rtp/239.253.93.209:6387' in original_url:
            formatted_names[original_url] = "霸州电视"
        elif '/rtp/239.253.93.139:6307' in original_url:
            formatted_names[original_url] = "青县综合"
        elif '/rtp/239.253.93.44:6197' in original_url:
            formatted_names[original_url] = "青河电视"
        elif '/rtp/239.253.93.24:6177' in original_url:
            formatted_names[original_url] = "青苑新闻"
        elif '/rtp/239.253.93.148:6316' in original_url:
            formatted_names[original_url] = "顺平电视"
        elif '/rtp/239.253.93.40:6193' in original_url:
            formatted_names[original_url] = "饶阳电视"
        elif '/rtp/239.253.93.115:6282' in original_url:
            formatted_names[original_url] = "馆陶综合"
        elif '/rtp/239.253.92.185:6049' in original_url:
            formatted_names[original_url] = "香河综合"
        elif '/rtp/239.253.93.23:6176' in original_url:
            formatted_names[original_url] = "高碑店综合"
        elif '/rtp/239.253.92.160:6041' in original_url:
            formatted_names[original_url] = "高邑融媒"
        elif '/rtp/239.253.93.105:6272' in original_url:
            formatted_names[original_url] = "高阳新闻"
        elif '/rtp/239.253.93.185:6353' in original_url:
            formatted_names[original_url] = "魏县综合"
        elif '/rtp/239.253.93.64:6219' in original_url:
            formatted_names[original_url] = "鸡泽新闻"
        elif '/rtp/239.253.92.183:6047' in original_url:
            formatted_names[original_url] = "黄骅电视"
        elif '/rtp/239.254.200.18:6000' in original_url:
            formatted_names[original_url] = "河北经济生活"
        elif '/rtp/239.254.200.19:6000' in original_url:
            formatted_names[original_url] = "河北都市"
        elif '/rtp/239.254.200.20:6000' in original_url:
            formatted_names[original_url] = "河北影视剧"
        elif '/rtp/239.254.200.21:6000' in original_url:
            formatted_names[original_url] = "河北少儿科教"
        elif '/rtp/239.254.200.22:6000' in original_url:
            formatted_names[original_url] = "河北公共"
        elif '/rtp/239.254.200.23:6000' in original_url:
            formatted_names[original_url] = "河北农民"
        elif '/rtp/239.254.200.27:6000' in original_url:
            formatted_names[original_url] = "睛彩河北"
        elif '/rtp/239.254.201.139:7203' in original_url:
            formatted_names[original_url] = "河北杂技频道"
        elif '/rtp/239.254.200.157:6000' in original_url:
            formatted_names[original_url] = "石家庄新闻综合"
        elif '/rtp/239.254.200.29:6000' in original_url:
            formatted_names[original_url] = "石家庄娱乐"
        elif '/rtp/239.254.200.30:6000' in original_url:
            formatted_names[original_url] = "石家庄生活"
        elif '/rtp/239.254.200.31:6000' in original_url:
            formatted_names[original_url] = "石家庄都市"
        elif '/rtp/239.254.200.32:6000' in original_url:
            formatted_names[original_url] = "承德新闻综合"
        elif '/rtp/239.254.200.33:6000' in original_url:
            formatted_names[original_url] = "承德公共"
        elif '/rtp/239.254.200.35:6000' in original_url:
            formatted_names[original_url] = "张家口新闻综合"
        elif '/rtp/239.254.200.36:6000' in original_url:
            formatted_names[original_url] = "张家口公共"
        elif '/rtp/239.254.200.39:6000' in original_url:
            formatted_names[original_url] = "秦皇岛新闻综合"
        elif '/rtp/239.254.200.40:6000' in original_url:
            formatted_names[original_url] = "秦皇岛公共"
        elif '/rtp/239.254.200.41:6000' in original_url:
            formatted_names[original_url] = "秦皇岛影视"
        elif '/rtp/239.254.200.166:6000' in original_url:
            formatted_names[original_url] = "唐山新闻综合"
        elif '/rtp/239.254.200.167:6000' in original_url:
            formatted_names[original_url] = "唐山生活服务"
        elif '/rtp/239.254.200.168:6000' in original_url:
            formatted_names[original_url] = "唐山影视"
        elif '/rtp/239.254.200.169:6000' in original_url:
            formatted_names[original_url] = "唐山公共"
        elif '/rtp/239.254.200.183:6000' in original_url:
            formatted_names[original_url] = "廊坊新闻"
        elif '/rtp/239.254.200.184:6000' in original_url:
            formatted_names[original_url] = "廊坊公共"
        elif '/rtp/239.254.200.42:6000' in original_url:
            formatted_names[original_url] = "沧州新闻综合"
        elif '/rtp/239.254.200.43:6000' in original_url:
            formatted_names[original_url] = "沧州公共"
        elif '/rtp/239.254.200.44:6000' in original_url:
            formatted_names[original_url] = "沧州影视娱乐"
        elif '/rtp/239.254.200.144:6000' in original_url:
            formatted_names[original_url] = "保定新闻综合"
        elif '/rtp/239.254.200.145:6000' in original_url:
            formatted_names[original_url] = "保定公共频道"
        elif '/rtp/239.254.200.146:6000' in original_url:
            formatted_names[original_url] = "保定生活健康"
        elif '/rtp/239.254.200.147:6000' in original_url:
            formatted_names[original_url] = "衡水新闻综合"
        elif '/rtp/239.254.200.149:6000' in original_url:
            formatted_names[original_url] = "衡水公共"
        elif '/rtp/239.254.200.150:6000' in original_url:
            formatted_names[original_url] = "邢台综合"
        elif '/rtp/239.254.200.152:6000' in original_url:
            formatted_names[original_url] = "邢台城市生活"
        elif '/rtp/239.254.200.153:6000' in original_url:
            formatted_names[original_url] = "邯郸新闻综合"
        elif '/rtp/239.254.200.154:6000' in original_url:
            formatted_names[original_url] = "邯郸公共"
        elif '/rtp/239.254.200.155:6000' in original_url:
            formatted_names[original_url] = "邯郸科技教育"
        elif '/rtp/239.254.200.191:5169' in original_url:
            formatted_names[original_url] = "元氏电视"
        elif '/rtp/239.254.200.220:5167' in original_url:
            formatted_names[original_url] = "无极电视"
        elif '/rtp/239.254.201.24:5170' in original_url:
            formatted_names[original_url] = "高邑电视"
        elif '/rtp/239.254.200.215:5173' in original_url:
            formatted_names[original_url] = "栾城电视"
        elif '/rtp/239.254.201.14:5175' in original_url:
            formatted_names[original_url] = "井陉矿区电视"
        elif '/rtp/239.254.200.244:5177' in original_url:
            formatted_names[original_url] = "赞皇电视"
        elif '/rtp/239.254.201.108:5180' in original_url:
            formatted_names[original_url] = "深泽电视"
        elif '/rtp/239.254.201.111:5183' in original_url:
            formatted_names[original_url] = "赵县电视"
        elif '/rtp/239.254.201.127:5184' in original_url:
            formatted_names[original_url] = "晋州电视"
        elif '/rtp/239.254.201.215:6167' in original_url:
            formatted_names[original_url] = "井陉电视"
        elif '/rtp/239.254.200.177:5286' in original_url:
            formatted_names[original_url] = "平泉电视"
        elif '/rtp/239.254.201.4:5291' in original_url:
            formatted_names[original_url] = "滦平电视"
        elif '/rtp/239.254.201.63:5293' in original_url:
            formatted_names[original_url] = "双滦电视"
        elif '/rtp/239.254.201.95:5295' in original_url:
            formatted_names[original_url] = "兴隆电视"
        elif '/rtp/239.254.201.142:5296' in original_url:
            formatted_names[original_url] = "隆化电视"
        elif '/rtp/239.254.201.204:6166' in original_url:
            formatted_names[original_url] = "鹿泉电视"
        elif '/rtp/239.254.201.115:5381' in original_url:
            formatted_names[original_url] = "任县电视"
        elif '/rtp/239.254.201.116:5225' in original_url:
            formatted_names[original_url] = "邯山电视"
        elif '/rtp/239.254.201.117:5267' in original_url:
            formatted_names[original_url] = "崇礼电视"
        elif '/rtp/239.254.201.118:6257' in original_url:
            formatted_names[original_url] = "顺平电视"
        elif '/rtp/239.254.201.130:5271' in original_url:
            formatted_names[original_url] = "张北电视"
        elif '/rtp/239.254.201.129:6209' in original_url:
            formatted_names[original_url] = "邱县电视"
        elif '/rtp/239.254.201.131:5269' in original_url:
            formatted_names[original_url] = "赤城电视"
        elif '/rtp/239.254.201.135:5270' in original_url:
            formatted_names[original_url] = "康保电视"
        elif '/rtp/239.254.201.146:5202' in original_url:
            formatted_names[original_url] = "遵化电视"
        elif '/rtp/239.254.201.61:5230' in original_url:
            formatted_names[original_url] = "昌黎电视"
        elif '/rtp/239.254.201.213:5232' in original_url:
            formatted_names[original_url] = "抚宁电视"
        elif '/rtp/239.254.201.216:5233' in original_url:
            formatted_names[original_url] = "卢龙电视"
        elif '/rtp/239.254.200.218:5186' in original_url:
            formatted_names[original_url] = "丰南电视"
        elif '/rtp/239.254.201.26:5188' in original_url:
            formatted_names[original_url] = "迁西电视"
        elif '/rtp/239.254.201.22:5191' in original_url:
            formatted_names[original_url] = "滦南电视"
        elif '/rtp/239.254.201.28:5194' in original_url:
            formatted_names[original_url] = "玉田电视"
        elif '/rtp/239.254.201.30:5196' in original_url:
            formatted_names[original_url] = "滦州电视"
        elif '/rtp/239.254.201.32:5306' in original_url:
            formatted_names[original_url] = "香河电视"
        elif '/rtp/239.254.201.34:5308' in original_url:
            formatted_names[original_url] = "大城电视"
        elif '/rtp/239.254.201.71:5310' in original_url:
            formatted_names[original_url] = "大厂电视"
        elif '/rtp/239.254.201.101:5312' in original_url:
            formatted_names[original_url] = "固安电视"
        elif '/rtp/239.254.201.103:5314' in original_url:
            formatted_names[original_url] = "文安电视"
        elif '/rtp/239.254.201.113:5315' in original_url:
            formatted_names[original_url] = "三河电视"
        elif '/rtp/239.254.201.141:5316' in original_url:
            formatted_names[original_url] = "永清电视"
        elif '/rtp/239.254.201.143:6210' in original_url:
            formatted_names[original_url] = "成安电视"
        elif '/rtp/239.254.201.148:6211' in original_url:
            formatted_names[original_url] = "魏县电视"
        elif '/rtp/239.254.200.4:5313' in original_url:
            formatted_names[original_url] = "霸州电视"
        elif '/rtp/239.254.201.35:5327' in original_url:
            formatted_names[original_url] = "渤海电视"
        elif '/rtp/239.254.201.36:5325' in original_url:
            formatted_names[original_url] = "黄骅电视"
        elif '/rtp/239.254.201.38:5329' in original_url:
            formatted_names[original_url] = "孟村电视"
        elif '/rtp/239.254.201.76:5331' in original_url:
            formatted_names[original_url] = "东光电视"
        elif '/rtp/239.254.201.112:5333' in original_url:
            formatted_names[original_url] = "青县电视"
        elif '/rtp/239.254.201.114:5334' in original_url:
            formatted_names[original_url] = "盐山电视"
        elif '/rtp/239.254.201.119:5335' in original_url:
            formatted_names[original_url] = "南皮电视"
        elif '/rtp/239.254.201.122:5336' in original_url:
            formatted_names[original_url] = "肃宁电视"
        elif '/rtp/239.254.201.138:5337' in original_url:
            formatted_names[original_url] = "吴桥电视"
        elif '/rtp/239.254.200.5:5290' in original_url:
            formatted_names[original_url] = "丰宁电视"
        elif '/rtp/239.254.200.172:5246' in original_url:
            formatted_names[original_url] = "定兴电视"
        elif '/rtp/239.254.201.40:5248' in original_url:
            formatted_names[original_url] = "阜平电视"
        elif '/rtp/239.254.201.10:5250' in original_url:
            formatted_names[original_url] = "涞水电视"
        elif '/rtp/239.254.200.222:5252' in original_url:
            formatted_names[original_url] = "满城电视"
        elif '/rtp/239.254.200.213:5260' in original_url:
            formatted_names[original_url] = "涞源电视"
        elif '/rtp/239.254.200.210:5254' in original_url:
            formatted_names[original_url] = "高碑店电视"
        elif '/rtp/239.254.201.17:5261' in original_url:
            formatted_names[original_url] = "涿州电视"
        elif '/rtp/239.254.201.41:5264' in original_url:
            formatted_names[original_url] = "唐县电视"
        elif '/rtp/239.254.200.242:5265' in original_url:
            formatted_names[original_url] = "曲阳电视"
        elif '/rtp/239.254.201.56:6246' in original_url:
            formatted_names[original_url] = "望都电视"
        elif '/rtp/239.254.201.74:6251' in original_url:
            formatted_names[original_url] = "定州电视"
        elif '/rtp/239.254.201.94:6254' in original_url:
            formatted_names[original_url] = "雄县电视"
        elif '/rtp/239.254.201.96:6253' in original_url:
            formatted_names[original_url] = "高阳电视"
        elif '/rtp/239.254.201.99:6255' in original_url:
            formatted_names[original_url] = "安新电视"
        elif '/rtp/239.254.201.102:6256' in original_url:
            formatted_names[original_url] = "容城电视"
        elif '/rtp/239.254.201.140:5383' in original_url:
            formatted_names[original_url] = "柏乡电视"
        elif '/rtp/239.254.201.145:5272' in original_url:
            formatted_names[original_url] = "涿鹿电视"
        elif '/rtp/239.254.201.147:6260' in original_url:
            formatted_names[original_url] = "徐水电视"
        elif '/rtp/239.254.201.149:6212' in original_url:
            formatted_names[original_url] = "大名电视"
        elif '/rtp/239.254.200.179:5346' in original_url:
            formatted_names[original_url] = "冀州电视"
        elif '/rtp/239.254.201.42:5348' in original_url:
            formatted_names[original_url] = "安平电视"
        elif '/rtp/239.254.200.240:5350' in original_url:
            formatted_names[original_url] = "景县电视"
        elif '/rtp/239.254.201.44:5353' in original_url:
            formatted_names[original_url] = "饶阳电视"
        elif '/rtp/239.254.201.46:5357' in original_url:
            formatted_names[original_url] = "深州电视"
        elif '/rtp/239.254.201.8:5355' in original_url:
            formatted_names[original_url] = "武邑电视"
        elif '/rtp/239.254.201.98:5361' in original_url:
            formatted_names[original_url] = "阜城电视"
        elif '/rtp/239.254.201.126:5362' in original_url:
            formatted_names[original_url] = "故城电视"
        elif '/rtp/239.254.201.136:5363' in original_url:
            formatted_names[original_url] = "枣强电视"
        elif '/rtp/239.254.200.170:5366' in original_url:
            formatted_names[original_url] = "清河电视"
        elif '/rtp/239.254.201.50:5373' in original_url:
            formatted_names[original_url] = "广宗电视"
        elif '/rtp/239.254.201.6:5216' in original_url:
            formatted_names[original_url] = "武安电视"
        elif '/rtp/239.254.201.51:5375' in original_url:
            formatted_names[original_url] = "宁晋电视"
        elif '/rtp/239.254.201.53:5378' in original_url:
            formatted_names[original_url] = "平乡电视"
        elif '/rtp/239.254.201.60:5218' in original_url:
            formatted_names[original_url] = "鸡泽电视"
        elif '/rtp/239.254.201.69:5379' in original_url:
            formatted_names[original_url] = "隆尧电视"
        elif '/rtp/239.254.201.70:5220' in original_url:
            formatted_names[original_url] = "广平电视"
        elif '/rtp/239.254.201.72:6000' in original_url:
            formatted_names[original_url] = "南和电视"
        elif '/rtp/239.254.201.73:5221' in original_url:
            formatted_names[original_url] = "临漳电视"
        elif '/rtp/239.254.201.77:5380' in original_url:
            formatted_names[original_url] = "内丘电视"
        elif '/rtp/239.254.201.97:5222' in original_url:
            formatted_names[original_url] = "涉县电视"
        elif '/rtp/239.254.201.109:5199' in original_url:
            formatted_names[original_url] = "迁安电视"
        elif '/rtp/239.254.201.105:5223' in original_url:
            formatted_names[original_url] = "肥乡电视"
        elif '/rtp/239.254.201.106:5224' in original_url:
            formatted_names[original_url] = "馆陶电视"
        elif '/rtp/239.254.201.107:5200' in original_url:
            formatted_names[original_url] = "乐亭电视"
        elif '/rtp/239.254.200.181:5369' in original_url:
            formatted_names[original_url] = "沙河电视"
        elif '/rtp/239.254.200.236:5210' in original_url:
            formatted_names[original_url] = "曲周电视"
        elif '/rtp/239.254.201.48:5371' in original_url:
            formatted_names[original_url] = "南宫电视"
        elif '/rtp/239.254.201.58:5197' in original_url:
            formatted_names[original_url] = "丰润电视"







         

           



          

                    








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
        file.write("\n#河北,#genre#\n")
        
    # 输出结果到文件 ztv.txt
    with open("ziyong.txt", "a") as file:
        for result in sorted_results:
            if len(result) >= 3 and result[2] > 0:  # 同样在这里检查
                file.write(f"{result[0]},{result[1]} -- {result[2]:.2f} MB/s\n")
    print("处理完成，结果已写入 ziyong.txt 文件")

if __name__ == "__main__":
    main()
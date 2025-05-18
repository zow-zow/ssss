import requests
import time
import concurrent.futures
import re


# 从本地文本文件读取URL列表
def read_urls_from_local_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            urls = file.readlines()
        return [url.strip() for url in urls if url.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return []

# 获取网址响应内容
urls = requests.get('http://php.5261314.xyz/源/汇总源.txt', timeout=3,headers={'User-Agent': '3ZTV3.1'})  # 设置超时时间
urls.encoding = 'utf-8'
#去除每一行的前后空白，并过滤掉空白行
urls = [url.strip() for url in urls.text.split('\n') if url.strip()]
pattern = r'(.*?),(http://\d+\.\d+\.\d+\.\d+:\d+/\w+/\d+\.\d+\.\d+\.\d+:\d+)'
test_urls = []
for url in urls:
    match = re.match(pattern, url)
    if match:
        description = match.group(1)
        real_url = match.group(2)
        test_urls.append((description, real_url))

# print(test_urls)

# 去重处理
unique_test_urls = list(set(test_urls))

def measure_download_speed(description, url, duration=10):
    try:
        #print(f"开始测量下载速度：{url}")
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
            print(f"{description},{url}下载速度：{speed:.2f} MB/s")

        return f"{description},{url}", speed
    except (requests.exceptions.RequestException, ConnectionError) as e:
        print(f"Failed to download {url}: {e}")
        return f"{description},{url}", 0.0

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda desc_url: measure_download_speed(desc_url[0], desc_url[1]), unique_test_urls))
        #按相同的描述排序
        results.sort(key=lambda x: x[0])
    with open("oldlinkstest.txt", "w") as file:
        file.write("\n#还有效的源,#genre#\n")
    for result in results:
        if result[1] > 0:  # 过滤下载速度为0的结果
            with open("oldlinkstest.txt", "a") as file:
                file.write(f"{result[0]} -- {result[1]:.2f} MB/s\n")

if __name__ == "__main__":
    main()

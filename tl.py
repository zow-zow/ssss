import subprocess
import threading
import requests
import time
from datetime import datetime, timedelta
import pytz

# 定义中国时区
china_tz = pytz.timezone('Asia/Shanghai')

# 定义一个函数来启动FFmpeg进程
def start_ffmpeg(input_url, output_url, processes):
    ffmpeg_command = [
        'ffmpeg',
        '-re',
        '-stream_loop', '-1',
        '-i', input_url,
        '-bsf:a', 'aac_adtstoasc',
        '-vcodec', 'copy',
        '-acodec', 'copy',
        '-f', 'flv',
        '-y',
        '-reconnect', '1',
        '-reconnect_at_eof', '1',
        '-reconnect_streamed', '1',
        output_url
    ]

    try:
        process = subprocess.Popen(ffmpeg_command, stderr=subprocess.PIPE)
        processes.append(process)
        while True:
            line = process.stderr.readline().decode('utf-8').strip()
            if not line:
                break
            print(line)
        process.wait()
    except Exception as e:
        print(f"An error occurred while streaming {input_url}: {e}")

# 从指定URL读取输入流和推流地址
def get_streams(url):
    response = requests.get(url)
    lines = response.text.strip().splitlines()
    streams = []
    for line in lines:
        input_url, output_url = line.split(',')
        streams.append((input_url.strip(), output_url.strip()))
    return streams

# 启动推流线程
def start_streaming_threads(streams, processes):
    threads = []
    for input_url, output_url in streams:
        thread = threading.Thread(target=start_ffmpeg, args=(input_url, output_url, processes))
        thread.start()
        threads.append(thread)
    return threads

# 停止所有正在运行的推流
def stop_streaming_threads(processes):
    for process in processes:
        if process.poll() is None:  # 检查进程是否仍在运行
            process.terminate()  # 终止进程
            process.wait()  # 等待进程完全结束

# 计算下一次整点时间（中国北京时间）
def get_next_hour():
    now = datetime.now(china_tz)
    next_hour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    return next_hour

# 主循环：每整点更新推流地址
def main(url):
    processes = []

    # 启动脚本时立即执行一次推流
    streams = get_streams(url)
    start_streaming_threads(streams, processes)

    while True:
        # 获取当前中国北京时间
        now = datetime.now(china_tz)

        # 等待直到下一个整点
        next_hour = get_next_hour()
        time_to_wait = (next_hour - now).total_seconds()
        print(f"Waiting until {next_hour.strftime('%H:%M:%S CST')} to update streams...")
        time.sleep(time_to_wait)

        # 停止当前的推流进程
        stop_streaming_threads(processes)

        # 清空进程列表
        processes.clear()

        # 读取流地址并启动新的推流线程
        streams = get_streams(url)
        start_streaming_threads(streams, processes)

# 设置URL
url = 'http://8.138.87.43:2020/源/tl.txt'

# 启动主循环
main(url)

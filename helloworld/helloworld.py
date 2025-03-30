import multiprocessing
import math
import time
from datetime import datetime

def is_prime(n):
    """判断是否为质数（高强度计算）"""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cpu_intensive_task(worker_id):
    """带回显的计算任务，显示进程ID、当前计算数值和时间戳"""
    try:
        start_num = 1_000_000 + worker_id * 1000  # 不同进程计算不同区间的数值
        count = 0
        while True:
            for num in range(start_num, start_num + 1000):
                if is_prime(num):
                    # 回显发现的质数（时间戳 + 进程ID + 数值）
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    print(f"[{timestamp}] 进程{worker_id}: 发现质数 -> {num}")
                    count += 1
            # 每5秒输出一次统计信息（避免刷屏）
            print(f"进程{worker_id}: 已计算区间 [{start_num}, {start_num+1000})，累计发现质数 {count} 个")
            start_num += 1000  # 切换到下一个区间
    except KeyboardInterrupt:
        pass

def run(max_workers=None):
    """启动多进程任务并管理回显"""
    num_cores = max_workers or multiprocessing.cpu_count()
    print(f"启动 {num_cores} 个进程，开始高强度计算...")

    processes = []
    for i in range(num_cores):
        # 传递进程ID参数区分不同任务
        p = multiprocessing.Process(target=cpu_intensive_task, args=(i,))
        p.start()
        processes.append(p)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n终止所有进程...")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    run()
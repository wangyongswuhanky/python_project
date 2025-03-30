import subprocess

def read_ips(file_path):
    """读取文本文件中的 IP 地址"""
    with open(file_path, 'r') as f:
        # 读取文件内容，移除每行的换行符
        ips = [line.strip() for line in f.readlines()]
    return ips

def block_ip(ip):
    """使用 iptables 封禁指定的 IP"""
    try:
        # 使用 iptables 命令封禁 IP 地址
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], check=True)
        print(f"IP {ip} has been blocked.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to block IP {ip}: {e}")

def main():
    # 指定包含 IP 地址的文本文件路径
    file_path = 'ips.txt'

    # 读取文本中的 IP 地址
    ips = read_ips(file_path)

    # 对每个 IP 执行封禁操作
    for ip in ips:
        block_ip(ip)

if __name__ == "__main__":
    main()

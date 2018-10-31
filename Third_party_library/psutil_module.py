import psutil # process and system utilities
print(psutil.cpu_count()) # cpu逻辑数量
print(psutil.cpu_count(logical=False)) # cpu物理核心
print(psutil.cpu_times()) # 统计CPU的用户／系统／空闲时间
print(psutil.net_connections()) # 获取当前网络连接信息

# 获取进程信息
print(psutil.pids())
print(psutil.test())
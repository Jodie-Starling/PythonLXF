import psutil

print(psutil.cpu_percent(interval = 0.1))
print(psutil.virtual_memory())

print(psutil.Process(8996))
print(psutil.pids()[:3])

print(len(psutil.net_connections()))
print(u.name for u in psutil.users())
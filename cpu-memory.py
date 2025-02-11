import psutil

# Get CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")

# Get memory usage
memory_info = psutil.virtual_memory()
print(f"Memory Usage: {memory_info.percent}%")

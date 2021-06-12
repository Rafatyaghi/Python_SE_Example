import psutil

print (dict(psutil.virtual_memory()._asdict()))
print (psutil.cpu_percent())
print(psutil.cpu_freq())
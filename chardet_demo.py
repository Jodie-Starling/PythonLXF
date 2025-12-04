import chardet
import os

# 流式检测
detector = chardet.UniversalDetector()

with open('temp/example1.txt', 'rb') as f:
    for line in f:
        detector.feed(line)
        if detector.done:
            break

detector.close()
result = detector.result
print(result)

# 批量检测
files = ['temp/example1.txt', 'temp/example2.txt']
for file in files:
    with open(file, 'rb') as f:
        raw = f.read()
        encoding = chardet.detect(raw)['encoding']
        # 字典值取出，encoding是键
        print(f'{file}: {encoding}')

# 简单检测
result2 = chardet.detect(b'Hello, world!')   # 只能读取字节
print(result2)

data = '一个向上的灵魂不应该有一个向下的躯体'.encode('utf-8')
result3 = chardet.detect(data)
print(result3)


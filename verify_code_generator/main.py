from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
from datetime import datetime

def rdmChar():
    # 生成随机大写字母
    return chr(random.randint(65, 90)) 

def rdmColor1():
    # 生成随机浅色
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)) 

def rdmColor2():
    # 生成随机深色
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)) 

width = 60 * 4
height = 60
img = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)

draw = ImageDraw.Draw(img)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rdmColor1())

for t in range(4):
    draw.text((60 * t + 10, 10), rdmChar(), font=font, fill=rdmColor2())

img = img.filter(ImageFilter.BLUR)
img.show()

# strftime 格式化时间函数
img.save(f'verify_code_generator/verify_code{datetime.now().strftime("%Y%m%d_%H%M%S")}.png', 'png')
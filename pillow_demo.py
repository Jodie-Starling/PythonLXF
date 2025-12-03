# pillow 图片处理库
'''
show() 会调用你操作系统默认的图片查看器（在 Windows 上通常是“照片”应用）。当你连续快速调用 5 次 show() 时，程序运行速度非常快，会在一瞬间向系统发送 5 个打开图片的请求。

大多数图片查看器无法在这么短的时间内响应这么多请求，或者它们是“单实例”程序（即一次只能打开一个窗口），导致后面的请求被忽略，或者新窗口覆盖了旧窗口，让你感觉只加载了前几张。

'''

from PIL import Image, ImageFilter, ImageDraw

img1 = Image.open('temp/test.jpg')
img1.show()
print(img1.format, img1.size, img1.mode)

img2 = img1.filter(ImageFilter.BLUR)
img2.show()

img3 = img1.copy() # thumbnail 是原地修改图片，所以要先复制一份
img3.thumbnail((100, 100))
img3.save('temp/img3.jpg')
img3.show()

box = (50, 50, 200, 200)
img4 = img1.crop(box)
img4.show()

img5 = img1.rotate(90)
img5.show()

img6 = img1.transpose(Image.Transpose.FLIP_LEFT_RIGHT) # FLIP_LEFT_RIGHT 和 FLIP_TOP_BOTTOM 等顶层常量被移除，必须通过 Image.Transpose 枚举类来访问。
img7 = img1.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
img6.show()
img7.show()

img8 = Image.new('RGB', (200, 200), 'blue')
draw = ImageDraw.Draw(img8)
draw.text((50, 90), 'Hello, PIL!', fill='white')
img8.show()
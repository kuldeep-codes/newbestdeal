from os import listdir
from os.path import isfile, join
from PIL import Image

def Reformat_Image(ImageFilePath):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height

        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        background = background.convert('RGB')
        background.save(ImageFilePath)
        background.close()
    else:
        image.close()
        

mypath = './product-image/'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for ele in onlyfiles:
    img_path = './product-image/'+ele
    !mv $img_path './product-image/tem.jpg'
    Reformat_Image('./product-image/tem.jpg')
    !mv './product-image/tem.jpg' $img_path
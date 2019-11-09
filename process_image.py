from PIL import Image, ImageStat
from io import BytesIO


def get_brightness(data):
    image = Image.open(BytesIO(data))
    greyscale_image = image.convert('L')
    stat = ImageStat.Stat(greyscale_image)

    return stat.mean[0]

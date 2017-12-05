import requests
from io import BytesIO
import PIL
from PIL import Image
hat = Image.open("hat.png")
position = (-70, -40, 230, 85)
hat = hat.resize((position[2]-position[0],position[3]-position[1]), Image.ANTIALIAS).rotate(-10, Image.BICUBIC)
print("Width:" + str(position[2]-position[0]+1))
print("Height:" + str(position[3]-position[1]+1))
avatars = [
    "PURPLE.png",
    "GREY.png",
    "GREEN.png",
    "YELLOW.png",
    "RED.png"
]


def hatme(user):
    print("TP1")
    avatar_url = user.avatar_url()
    print(user.avatar_url())
    print("TP2")
    if not user.avatar_url() is "":
        avatar_url = user.avatar_url()
        response = requests.get(avatar_url)
        img = Image.open(BytesIO(response.content))
    else:
        index = int(user.discriminator) % len(avatars)
        img = Image.open(avatars[index]).resize((128,128), Image.ANTIALIAS)
    img.save("blah.jpg")
    img.paste(hat, position, hat)
    return img

'''
def hatme(user):
    print("TP1")
    avatar_url = user.avatar_url()
    print(user.avatar_url())
    print("TP2")
    if not user.avatar_url() is "":
        avatar_url = user.avatar_url()
        response = requests.get(avatar_url)
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open("hat.png")
    img.save("blah.jpg")
    img.paste(hat, position, hat)
    return img
'''
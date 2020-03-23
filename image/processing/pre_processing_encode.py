import base64
import json
import cv2

img = cv2.imread('C:/Users/andre/OneDrive/Desktop/HigiaLab/image/00001/001/0001.png')
string = base64.b64encode(cv2.imencode('.png', img)[1]).decode()
dict = {
    'img': string
}
with open('./0.json', 'w') as outfile:
    data = json.dump(dict, outfile, ensure_ascii=False, indent=4)
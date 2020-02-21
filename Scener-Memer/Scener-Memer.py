
from clarifai.rest import ClarifaiApp
import json
import urllib.request
import base64
import os
import cv2
from tkinter.filedialog import askopenfilename

message = input("From a URL ?(Y/N)")
message1 = ""
message2 = ""
dir_path = ""

if message == "Y":
    message = input("Enter a Image URL:")
    urllib.request.urlretrieve(message, "/home/jj/test.jpg")
    dir_path = "/home/jj/test.jpg"
elif message == "N":
    message1 = input("From some folder ?(Y/N)")
    if message1 == "Y":
        filename = askopenfilename()
        #os.system(filename)
        dir_path = filename
        print(filename)
    elif message1 == "N":
        camera = cv2.VideoCapture(0)
        while True:
            return_value, image = camera.read()
            color = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
            cv2.imshow('image', color)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite('test.jpg', image)
                break
        camera.release()
        cv2.destroyAllWindows()

        dir_path = os.path.dirname(os.path.realpath('test.jpg'))
        print(dir_path)
        dir_path = dir_path + dir_path[0] + 'test.jpg'
        os.system(r'test.jpg')
        print(dir_path)

app = ClarifaiApp(api_key='ddd50a327ab54d66943183ac765c733a')

model = app.models.get('general-v1.3')
response = model.predict_by_filename(dir_path)

l = list(response.values())

x = list(l[1][0]['data']['concepts'])
s=x[0]['name']
for i in range(1,15):
    s+="+"+x[i]['name']
s = s.replace(" ","+")
print(s.replace(" ","+"))

for i in range(len(x)):
    print(x[i]['name'])

data=json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q="+s+"&api_key=bX8vbnlEYt9tm7yOe7oeka1QxO9GRrTO&limit=1&rating:g&lang:en").read())

import webbrowser
webbrowser.open(data['data'][0]['embed_url'])
print(data['data'][0]['embed_url'])





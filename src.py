import os
from PIL import Image
import ctypes
import pathlib
from shutil import copy2

path = (os.getenv('USERPROFILE')+'\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\')
files = os.listdir(path)
install_path = os.path.dirname(os.path.realpath('__file__')) + '\\images'
print(install_path)
pathlib.Path(install_path).mkdir(parents=True, exist_ok='True')
i = 1
for f in files:
    
    img = Image.open(path+'\\'+f)
    w,h = img.size
    if(w==1920 and h == 1080):
        copy2(path + '\\' + f, install_path + '\\' + str(i) + '.jpg')
        i = i+1
print("There are " + str(i-1) +" images found in your spotlight", end = "............................................. \n")
m = 0
while(m==0):
    
    print("Enter which image you want to see as background")
    k = int(input())

    ctypes.windll.user32.SystemParametersInfoW(20, 0, install_path +"\\" + str(k) + ".jpg" , 0)
    print("Are you satisfied ? press 0 for no, 1 for yes")
    m = int(input())








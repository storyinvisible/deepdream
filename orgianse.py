from os import listdir
from os.path import isfile,join
from shutil import move
import os
onlyfiles= [f for f in listdir("trainA/") if isfile(join('trainA/',f))]
for i in range(len(onlyfiles)):
    src= "trainA/"+onlyfiles[i]
    dis= str(i//16+1)+'/'
    if not os.path.exists(dis):
        os.makedirs(dis)
        move(src,dis)
    else:
        move(src,dis)
    
    
    

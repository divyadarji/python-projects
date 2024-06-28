import sys
import os
from PIL import Image

# grab first and second argumenet
image_folder= sys.argv[1]
output_folder=sys.argv[2]


# check is new existes if not then creat one
if not os.path.exists(output_folder) :
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name=os.path.splitext(filename)[0]
    
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')

# print(image_folder,output_folder)
# loop through pokedex,
# convert images to png
# save to thee new folder
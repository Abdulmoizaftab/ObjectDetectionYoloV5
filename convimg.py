# from PIL import Image 
# import os 

# # path = r'C:\Users\david.han\Desktop\COPY_images_files'
# path = r'D:\Online\Selected2'


# for file in os.listdir(path): 
#     if file.endswith(".jfif"): 
#         img = Image.open(file)
#         file_name, file_ext = os.path.splitext(file)
#         img.save('/SelectedJPG/{}.jpg'.format(file_name))




from PIL import Image
import os

root = r'D:\Online\Selected2'
print(root)
count = 0
for dirs, subdir, files in os.walk(root):
    for file in files:
        lastChar = file[-4:]
        if(lastChar == 'jfif'):
            img = Image.open(root+'\\'+file)
            #file ends in .jfif, remove 4 characters
            fileName = file[:-4]
            print(fileName)
            #add jpg and save
            img.save(root+'\\'+"SelectedJPG" +'\\'+fileName + "jpg")
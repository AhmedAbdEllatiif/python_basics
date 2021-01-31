import cv2.cv2 as cv2
import glob

# glob is to get all files with .jpg
images = glob.glob("*.jpg")

imgs = ['galaxy.jpg','kangaroos-rain-australia_71370_990x742.jpg','Lighthouse.jpg','Moon sinking, sun rising.jpg']

resized_images = []
for img in images:
    img = img = cv2.imread(img,flags =1)
    resized_img = cv2.resize(img,(100,100))
    resized_images.append(resized_img)
    
    

for r_img,img in  zip(resized_images,images):
    cv2.imwrite(f"resized_{img}",r_img)


#img = cv2.imread('galaxy.jpg',flags = cv2.IMREAD_GRAYSCALE)

#print(type(img))
#print(img)
#print(img.shape)
#print(img.ndim)

#resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#cv2.imshow("Galaxy",resized_img)

#cv2.imwrite("galaxy_resized.jpg",resized_img)

# 0 >>> To close when any button pressed
#cv2.waitKey(0) 
#cv2.waitKey(0) 
#cv2.destroyAllWindows() # To close window
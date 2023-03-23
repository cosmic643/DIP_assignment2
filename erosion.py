import cv2
import numpy as np
mat = cv2.imread("E:\\DIP\\input_image.jpg")
#print(mat)
if mat is None:
    print("Error: Image cannot be loaded")
    exit(0);
else:
    print("Image read successfully")

mat = cv2.cvtColor(mat,cv2.COLOR_BGR2HSV)

height,breadth,channel = mat.shape
img = np.zeros((height,breadth),dtype = np.uint8)
print(img.shape)
for j in range(height):
    for k in range(breadth):
        pixel = mat[j,k];
        if((pixel[0] >= 0 and pixel[0] <= 28) and (pixel[1] >= 60 and pixel[1] <= 75) and (pixel[2] >= 0 and pixel[2] <= 200)):
            img[j,k] = 255

def add_padding(img):
    height,breadth = img.shape
    new_img = np.zeros((height + 2,breadth + 2))
    h,b = new_img.shape
    for i in range(height):
        for j in range(breadth):
            new_img[i+1][j+1] = img[i][j]
    #print(new_img.shape)
    new_img[0][0] = img[0][0]
    new_img[h-1][b-1] = img[height-1][breadth-1]
    new_img[0][b-1] = img[0][breadth-1]
    new_img[h-1][0] = img[height-1][0]
    for i in range(1,h-1):
        new_img[i][0] = img[i-1][0]
        new_img[i][h-1] = img[i-1][height-1]
    for j in range(1,b-1):
        new_img[0][j] = img[0][j-1]
        new_img[0][b-1] = img[0][breadth-1]
    return new_img
#kernel = np.array(((255,255),(255,255)))
kernel = np.array(((0,255,0),(255,255,255),(0,255,0)))
print(kernel)
#img = add_padding(img)
center = (0,0)
def erosion(temp_img,kernel):
    height,breadth = temp_img.shape
    eroded_image = np.zeros((height,breadth))
    #print(eroded_image)
    k_height,k_breadth = kernel.shape
    for i in range(1,height-2):
        for j in range(1,breadth-2):
            flag = True
            for k in range(k_height):
                for l in range(k_breadth):
                    if(temp_img[i+k][j+l] != 255 or kernel[k][l] != 255):
                        flag = False;
                        break
                if(not(flag)):
                    break
            if(flag): 
                eroded_image[i+center[0]][j+center[1]] = 255
                    
    return eroded_image

temp = erosion(img,kernel)
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("original_image", cv2.WINDOW_AUTOSIZE)
#WINDOW_NORMAL let you resize the window

cv2.imshow("image",temp)
cv2.imshow("original_image",img)
cv2.waitKey(0);

cv2.destroyAllWindows()
import cv2
import numpy as np
import pytesseract
from PIL import Image
import keras
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
def invertImage(image):
    h=image.shape[0]
    w=image.shape[1]
    c=image.shape[2]
    size=(h,w,c)
    newImage=np.zeros(size,np.uint8)
    for x in range(h):
        for y in range(w):
            for z in range(c):
                newImage[x,y,z]=255-image[x,y,z]
    return newImage
def getFiltered(imgpath):
    imgpath=str(imgpath)
    cnn=keras.models.load_model('finalMode.h5')
    from keras.preprocessing import image
    folder='media/'+imgpath
    test_image = image.load_img(folder, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = cnn.predict(test_image)
    if result[0][0] == 1:
        prediction = 'light'
    else:
        prediction = 'dark'
    pil_image=Image.open(folder)
    img=np.array(pil_image)  
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    if prediction=='dark':
        img=invertImage(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _,img=cv2.threshold(img,200,140,cv2.THRESH_BINARY)
    cv2.imwrite(folder, img)
    result = pytesseract.image_to_string(Image.open(folder))
    return result
import cv2 as cv
import numpy as np 
import urllib.request

def load_image_from_url(url):
    req=urllib.request.urlopen(url)
    img=np.asanyarray(bytearray(req.read()),dtype=np.uint8)
    img=cv.imdecode(img,cv.IMREAD_COLOR)
    return img

def add_noise(img):
    mean = 0
    sigma = 50
    noisy = np.random.normal(mean, sigma, img.shape)
    new_img = np.clip(img + noisy, 0, 255).astype(np.uint8)
    return new_img

def add_muoi_tieu(img, ratio=0.02):
    noisy = img.copy()
    muoitieu = int(ratio * img.size)
    # // Thêm muối (pixel trắng)
    toado = [np.random.randint(0, i - 1, muoitieu) for i in img.shape]
    noisy[toado[0], toado[1], :] = 255
    # // Thêm tiêu (pixel đen)
    toado = [np.random.randint(0, i - 1, muoitieu) for i in img.shape]
    noisy[toado[0], toado[1], :] = 0
    return noisy

if __name__ == "__main__":
   url="https://raw.githubusercontent.com/opencv/opencv/refs/heads/4.x/samples/data/lena.jpg"
   anh_goc=load_image_from_url(url)
   cv.imshow("img",anh_goc)
   cv.waitKey(0)
   cv.destroyAllWindows()
#    n_=add_noise(img)
#    cv.imshow("img",n_)
#    cv.waitKey(0)
#    cv.destroyAllWindows()
#    imt=anh_goc.copy()
#    img2=np.clip(anh_goc + n_,0, 255).astype(np.uint8)
#    cv.imshow("img",img2)
#    cv.waitKey(0)
#    cv.destroyAllWindows()

#    cb=np.concatenate((img, n_,img2), axis=1)
#    cv.imshow("img",cb)
#    cv.waitKey(0)
#    cv.destroyAllWindows()

   img4 = add_muoi_tieu(anh_goc, 0.03)
   cv.imshow("img4",img4)
   cv.waitKey(0)
   cv.destroyAllWindows()

   img5= np.concatenate()
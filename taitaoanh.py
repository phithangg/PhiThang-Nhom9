import cv2 as cv
import numpy as np
import urllib
import urllib.request

if __name__ == "__main__":
   img = cv.imread("bienbao.jpg", cv.IMREAD_COLOR)
#    img = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
#    blurred = cv.GaussianBlur(img, (5, 5), 0)
#    edge=cv.Canny(blurred,50, 85)
#    edge_color = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)
#    cb = np.concatenate((img, edge_color), axis=1)
#    cv.imshow("Anh goc vs Anh edge",cb)
#    cv.waitKey(0)
#    cv.destroyAllWindows() 
   img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   
   edge=cv.Canny(img2,50, 85)
   cv.imshow("Anh gray",img2)
   cv.waitKey(0)
   cv.destroyAllWindows()   
   w, h=edge.shape
   print(w,h)
   n_img= edge[w//2-150:w//2+150, h//2-150:h//2+150]
   cv.imshow("Anh canny",n_img)
   cv.waitKey(0)            
   cv.destroyAllWindows()
    

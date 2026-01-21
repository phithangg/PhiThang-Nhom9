import matplotlib.pyplot as plt
import numpy as np  
import cv2 as cv
import math
from datetime import datetime
import time

#Vẽ mặt đồng hồ hình tròn, nền màu tím, có các số dạng la mã màu sắc khác nhau. 
#Có 3 kim đồng hồ: Giờ, phút, giây.
#Kim giờ màu xanh dương, kim phút màu xanh lá cây, kim giây màu đỏ.
#level 2: Vẽ kim giây chuyển động.
#level 3: Vẽ kim phút chuyển động.
#level 4: Vẽ kim giờ chuyển động.   
#level 5: Vẽ thêm các vạch chỉ phút trên mặt đồng hồ. Và kim giây, kim giờ, kim phút, hoạt động theo logic

# Kích thước và thiết lập
size = 800
center = (size // 2, size // 2)
radius = 300

# Số La Mã và màu sắc
roman_numbers = ['XII', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI']
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255),
          (128, 0, 128), (255, 128, 0), (0, 128, 255), (128, 255, 0), (255, 0, 128), (128, 128, 128)]

def draw_clock_face(img):
    # Nền màu tím
    img[:] = (128, 0, 128)
    
    # Vẽ mặt đồng hồ tròn (nền trắng)
    cv.circle(img, center, radius, (255, 255, 255), -1)
    
    # Vẽ viền đồng hồ
    cv.circle(img, center, radius, (0, 255, 255), 10)
    cv.circle(img, center, radius, (0, 0, 255),4)
    
    # Vẽ các vạch phút (level 5)
    for i in range(60):
        angle = math.radians(i * 6 - 90)
        if i % 5 == 0:
            # Vạch giờ dài hơn
            start_r = radius - 30
            thickness = 3
        else:
            # Vạch phút ngắn hơn
            start_r = radius - 15
            thickness = 1
        
        start_x = int(center[0] + start_r * math.cos(angle))
        start_y = int(center[1] + start_r * math.sin(angle))
        end_x = int(center[0] + (radius - 10) * math.cos(angle))
        end_y = int(center[1] + (radius - 10) * math.sin(angle))
        cv.line(img, (start_x, start_y), (end_x, end_y), (0, 0, 0), thickness)
    
    # Vẽ số La Mã với màu sắc khác nhau
    for i, (roman, color) in enumerate(zip(roman_numbers, colors)):
        angle = math.radians(i * 30 - 90)
        x = int(center[0] + (radius - 50) * math.cos(angle))
        y = int(center[1] + (radius - 50) * math.sin(angle))
        
        # Điều chỉnh vị trí text
        text_size = cv.getTextSize(roman, cv.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
        x -= text_size[0] // 2
        y += text_size[1] // 2
        
        cv.putText(img, roman, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    # Vẽ tâm đồng hồ
    cv.circle(img, center, 10, (0, 0, 0), -1)

def draw_hand(img, angle, length, color, thickness):
    """Vẽ kim đồng hồ"""
    angle_rad = math.radians(angle - 90)
    end_x = int(center[0] + length * math.cos(angle_rad))
    end_y = int(center[1] + length * math.sin(angle_rad))
    cv.line(img, center, (end_x, end_y), color, thickness)

# Vòng lặp chính để tạo animation (level 5)
while True:
    # Tạo ảnh mới cho mỗi frame
    clock_img = np.zeros((size, size, 3), dtype=np.uint8)
    
    # Vẽ mặt đồng hồ
    draw_clock_face(clock_img)
    
    # Lấy thời gian hiện tại
    now = datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second
    
    # Tính góc cho mỗi kim (theo logic thực tế)
    second_angle = seconds * 6  # Mỗi giây = 6 độ
    minute_angle = minutes * 6 + seconds * 0.1  # Mỗi phút = 6 độ + chuyển động mượt theo giây
    hour_angle = hours * 30 + minutes * 0.5  # Mỗi giờ = 30 độ + chuyển động mượt theo phút
    
    # Vẽ kim giờ (xanh dương, ngắn, dày)
    draw_hand(clock_img, hour_angle, radius * 0.5, (255, 0, 0), 8)
    
    # Vẽ kim phút (xanh lá cây, trung bình)
    draw_hand(clock_img, minute_angle, radius * 0.7, (0, 255, 0), 6)
    
    # Vẽ kim giây (đỏ, dài, mỏng)
    draw_hand(clock_img, second_angle, radius * 0.85, (0, 0, 255), 2)
    
    # Hiển thị
    cv.imshow('Clock', clock_img)
    
    # Thoát khi nhấn ESC
    if cv.waitKey(1000) == 27:  # Update mỗi giây
        break

cv.destroyAllWindows()
# em nhờ AI hỗ trợ

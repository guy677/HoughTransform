import cv2
import numpy as np

def Hough_lines(img):
    if (img.__class__ == np.ndarray):
        img = cv2.Canny(img, 100, 200)
        image_shape = img.shape
        height = image_shape[0]
        width = image_shape[1]
        r_l= int(np.sqrt(height**2+ width**2))#Max lenght from (0,0)
        line_length=r_l/5#threshold
        accumulator = np.zeros((180, r_l), dtype=int)
        thetas=np.arange(0, 180)
        # need to create 2d array so I can use np.vstack() later
        lines = np.array([[0, 0], [0, 0]])
        # create cos an sin array
        cos_t= np.cos(np.deg2rad(thetas))
        sin_t= np.sin(np.deg2rad(thetas))

        # look for every pixel
        for y in range(height):
            for x in range(width):
                # if pixel is White (possible part of a line)
                if img[y][x] == 255:
                    # try all angles (if you need more precise just decrease step)
                    for theta in range(0, 180):
                        p = int(x *cos_t[theta] + y *sin_t[theta]) #let the lenght be naturale
                        accumulator[theta][p] += 1
                        # Check if it looks like line and if it's not in a list
                        if (accumulator[theta][p] > line_length) and ((p not in lines[:, 0]) or (theta not in lines[:, 1])):
                            lines = np.vstack((lines, np.array([p, theta])))
        # clean two first zeros
        lines = np.delete(lines, [0, 1], axis=0)
        return lines
    else:
        return None
def drawLines(img,lines):
    if(img.__class__==np.ndarray):
        for i in range(len(lines)):
            a=np.cos(np.deg2rad(lines[i][1]))
            b = np.sin(np.deg2rad(lines[i][1]))
            x0 = a*lines[i][0]
            y0 = b*lines[i][0]
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 + 1000*(b))
            y2 = int(y0 + 1000*(-a))
            cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)
    else:
        return None

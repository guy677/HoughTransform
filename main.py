from FuncHough import *
import os


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TestIm=BASE_DIR
    TestIm= os.path.join(TestIm,"test")
    for root,dirs,files in os.walk(TestIm):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root,file)
                img = cv2.imread(path)
                lines=Hough_lines(img)
                lineImag=img.copy()
                drawLines(lineImag,lines)
                compare=np.concatenate((lineImag, img), axis=1)#stick the before and after photos
                cv2.namedWindow('image', cv2.WINDOW_NORMAL)
                cv2.resizeWindow('image', 1500, 800)
                cv2.imshow('image', compare)
                cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
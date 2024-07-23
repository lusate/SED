
import cv2
vfile = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if vfile.isOpened():
    while True:
        vret, img = vfile.read()
        if vret:
            cv2.imshow('webcam', img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print("프레임 정상X")
            break
else:
    print("파일 못 염")
    
vfile.release()
cv2.destroyAllWindows()

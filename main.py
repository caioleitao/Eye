#código para abrir a webcam

import cv2

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FPS, 10)
    while(True):
        ret, frame = cam.read()
        cv2.imshow("Hey", frame)
        #letra 'q'
        fps = cam.get(cv2.CAP_PROP_FPS)
        print(fps)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.realise()
    cv2.destroyWindow() 


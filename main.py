#código para abrir a webcam

import cv2

def main():

    name = "Hey"

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FPS, 90)
    while(True):
        ret, frame = cam.read()
        cv2.imshow(name, frame)
        fps = cam.get(cv2.CAP_PROP_FPS)
        print(fps, end='\t')
        #print(cv2.waitKey(1))
        print()
        #letra 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyWindow(name) 

if __name__ == "__main__":
    main()
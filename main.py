#código para abrir a webcam

import cv2

def setup():
    print()
    for i in range(15):
        print("*",end='\t')
    print()
    #print("!CLICK IN 'Q' FOR QUIT OF THE APP!")
    for i in range((int)(15/3)):
        print(" ", end='\t')
    print("!CLICK IN 'Q' FOR QUIT OF THE APP!")
    for i in range(15):
        if i == (int)(15/2):
            print("Begin",end='\t')
        else:
            print("*",end='\t')
    print()

def main():
    name = "Hey"

    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FPS, 180)
    while(True):
        ret, frame = cam.read()
        cv2.imshow(name, frame)
        fps = cam.get(cv2.CAP_PROP_FPS)
        print(fps)
        #letra 'q'
        if cv2.waitKey(1) == ord('q'):
            break
    cam.release()
    cv2.destroyWindow(name) 

if __name__ == "__main__":
    setup()
    main()
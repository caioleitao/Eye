import cv2

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)
    
    while(True):
        ret, frame = cam.read()
        cv2.imshow("Hey", frame)
        #letra 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.realise()
    cv2.destroyWindow() 

    
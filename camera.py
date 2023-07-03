import cv2 as cv

class Camera:

#constructor defined to initiate the instance,
    def __init__(self):
        self.camera=cv.VideoCapture(0)      #videoCapture(0) denotes it is the by default our web cam which is only 1 ,if we have 2 cam,put the no u r interested in
        if not self.camera.isOpened():
            raise ValueError("Unable to open the Camera !")

        self.width = self.camera.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.camera.get(cv.CAP_PROP_FRAME_HEIGHT)

# now create a destructor, when user cloes the cam, the cam object created shld also be closed, so call destructor

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release()  #closes the camera

# write a method to call the camera again,to take image of the next instance

    def get_frame(self):
        if self.camera.isOpened():
            ret,frame= self.camera.read()
# ret = boolean value that return true if the frame is available
# frame = image array vector captured based on the default frames persecond
            if ret:
                return (ret,cv.cvtColor(frame,cv.COLOR_BGR2RGB))
            else:
                return (ret,None)
        else:
            return None     #if comera is not open
# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

def convertToQImage(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)

    Pic = image.scaled(320, 240, Qt.KeepAspectRatio)

    return Pic

class HandGesture_Thread(QThread):
    #def __init__(self, conn):
        #self.conn = conn

    Hand_Object = hg.HandGesture()

    ImageUpdate = Signal(QImage)

    ThreadActive = False
    ReadytoClose = False

    def run(self):
        self.ThreadActive = True
        
        while True:
            hg_image, hg_handsign, hg_signal,  = self.Hand_Object.main()

            self.ImageUpdate.emit(convertToQImage(hg_image))

            #self.conn.send(str.encode(str(hg_signal)+'.'))

            if self.ThreadActive == False:
                self.Hand_Object.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

class SelfDriving_Thread(QThread):
    #def __init__(self, connection):
        #self.connection = connection

    ObjectDetection = od.ObjectDetection()

    #LaneFollowing = lf.LaneFollowing()

    od_ImageUpdate = Signal(QImage)
    #lf_ImageUpdate = Signal(QImage)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    ThreadActive = False
    ReadytoClose = False

    def run(self):
        self.ThreadActive = True
        
        while True:
            #frame = self.connection.receive_image()

            _,frame = SelfDriving_Thread.cap.read()

            od_image, od_signal = self.ObjectDetection.run(frame)
            #lf_image, lf_signal = LaneFollowing.run(frame)

            #cv2.imshow('Hand Gesture Recognition', frame)

            self.od_ImageUpdate.emit(convertToQImage(od_image))
            #self.lf_ImageUpdate.emit(convertToQImage(lf_image))

            if self.ThreadActive == False:
                SelfDriving_Thread.cap.release()
                break

        self.quit()

        self.ReadytoClose = True
    
    def stop(self):
        self.ThreadActive = False

    
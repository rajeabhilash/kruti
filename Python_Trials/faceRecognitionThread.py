from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import face_recognition
import cv2

class Recognise(QThread):

    faceRecognized = pyqtSignal(str)
    isRecognized = False

    def __init__(self):
        super().__init__()
        self.captureFace = cv2.VideoCapture(0)
        self.abhiFace = face_recognition.load_image_file('ABHI_FIVE.jpg')
        self.abhiFaceEncode = face_recognition.face_encodings(self.abhiFace)[0]
        self.shreyaFace = face_recognition.load_image_file('SHREYA.jpg')
        self.shreyaFaceEncode = face_recognition.face_encodings(self.shreyaFace)[0]
        self.knownFaceEncodings = [self.abhiFaceEncode,self.shreyaFaceEncode]
        self.knownFaceNames = ["Raje Abhilash Mohite","Shreya Devkate"]
        self.faceLocations = []
        self.faceNames = []
        self.faceEncodes = []
        self.processThisFrame = True


    def run(self):
        print("Entering in Thread isRecognized : {}".format(self.isRecognized))
        while not self.isRecognized:
            check, frame = self.captureFace.read()
            smallFrame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
            smallFrameRGB = smallFrame[:,:,::-1]
            if self.processThisFrame:
                self.faceLocations = face_recognition.face_locations(smallFrameRGB)
                self.faceEncodes = face_recognition.face_encodings(smallFrameRGB,self.faceLocations)
                self.faceNames = []

                for faceEncode in self.faceEncodes:
                    matches = face_recognition.compare_faces(self.knownFaceEncodings,faceEncode)
                    name = "UNKNOWN"

                    if True in matches:
                        firstMatchIndex = matches.index(True)
                        name = self.knownFaceNames[firstMatchIndex]
                        self.faceRecognized.emit(name)
                    self.faceNames.append(name)

            self.processThisFrame = not self.processThisFrame
        print("Logged in Success.! isRecognized = {}".format(self.isRecognized))

    def __del__(self):
        self.isRecognized = True
        cv2.destroyAllWindows()
        self.captureFace.release()

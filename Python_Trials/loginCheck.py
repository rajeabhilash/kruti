from PyQt5.QtCore import QThread, pyqtSignal
import speech_recognition as sp
import random

class Login(QThread):

    keyGenerated = pyqtSignal(list)
    loginSuccess = pyqtSignal()
    loginFailed = pyqtSignal()
    exceptionOccured = pyqtSignal(str)
    waiting = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        #self.record = sp.Recognizer()
        pass

    def RandomKey(self):
        key = [1, 2, 3, 4, 5]
        for index in range(0, 4):
            key[index] = random.randint(0, 5)
        self.keyGenerated.emit(key)
        return key

    def checkKey(self, key, userKey, index=0):
        if len(key) == len(userKey):
            indexVal = key[index]
            isCorrect = False
            i = 0
            while i < len(key):
                enc = key[i] + int(indexVal)
                if enc > 9:
                    enc = str(enc / 10)[2]
                if userKey[i] == str(enc):
                    isCorrect = True
                else:
                    isCorrect = False
                    break
                i += 1
            if isCorrect:
                return True
            else:
                return False
        else:
            i = 0
            newKey = [1, 2, 3, 4, 5]
            keyI = 0
            while i < len(userKey):
                if userKey[i] != ' ' and keyI < 5:
                    newKey[keyI] = userKey[i]
                    keyI += 1
                i += 1
            if self.checkKey(key, newKey):
                return True
            else:
                return -1

    def run(self):
        key = self.RandomKey()
        record = sp.Recognizer()
        for i in range(0,9):
            self.waiting.emit(i)
            self.msleep(300)
            self.waiting.emit(9)

        #self.waiting.emit(10)
        with sp.Microphone() as source:
            self.waiting.emit(10)
            record.adjust_for_ambient_noise(source)
            audio = record.listen(source, timeout=5, phrase_time_limit=5)
        try:
            self.waiting.emit(15)
            phrase = record.recognize_google(audio)
            userKey = phrase
            print("USER KEY : ", userKey)
            what = self.checkKey(key, userKey)
            if what == -1:
                self.loginFailed.emit()
            else:
                if what:
                    self.loginSuccess.emit()
                else:
                    self.loginSuccess.emit()
        except sp.WaitTimeoutError as e:
            self.exceptionOccured.emit(str(e))
        except sp.UnknownValueError as e:
            self.exceptionOccured.emit(str(e))
        except sp.RequestError as e:
            self.exceptionOccured.emit(str(e))
        except Exception as exp:
            self.exceptionOccured.emit(str(exp))

    def __del__(self):
        pass
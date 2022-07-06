import cv2 as cv
import numpy as np

class Robot_Camera:
    
    def __init__(self):
        return
    
    #开启摄像头
    def Open_Robot_Web_Camera_On(self, x):
        self._camera = cv.VideoCapture(x)
        if not self._camera.isOpened():
            print("cannot open camera!")
            return
        else:
            while True:
                ret, self._frame = self._camera.read()
                if not ret:
                    print("connot read frame!")
                    return
                else:
                    #把获取到的图像格式转换(编码)成流数据，赋值到内存缓存中;
                    retx, self._buffer = cv.imencode('.jpg', self._frame)
                    #将缓存里的流数据转成字节流
                    self._frame = self._buffer.tobytes()
                    #指定字节流类型image/jpeg
                    yield  (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + self._frame + b'\r\n')
                    
    #设置分辨率
    def Set_Resolution(self, x,  w, h):
        self._camera = cv.VideoCapture(x)
        if not self._camera.isOpened():
            print("cannot open camera!")
            return
        else:
             #可设置的摄像头分辨率(width, height)有(320, 240)、(640, 480)、(1280, 720)、(1920, 1080)
            self._camera.set(cv.CAP_PROP_FRAME_WIDTH, w)
            self._camera.set(cv.CAP_PROP_FRAME_HEIGHT, h)
            while True:
                ret, self._frame = self._camera.read()
                if not ret:
                    print("connot read frame!")
                    return
                else:
                    #把获取到的图像格式转换(编码)成流数据，赋值到内存缓存中;
                    retx, self._buffer = cv.imencode('.jpg', self._frame)
                    #将缓存里的流数据转成字节流
                    self._frame = self._buffer.tobytes()
                    #指定字节流类型image/jpeg
                    yield  (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + self._frame + b'\r\n')
                    
    #摄像头标定
    def Calibration(self, x):
        self._camera = cv.VideoCapture(x)

        #找棋盘格角点
        criterial = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001) #设置标准

        #设置棋盘格规格
        w = 11
        h = 7

        #将世界坐标中的棋盘格点记为二维矩阵
        objp = np.zeros((w * h, 3), np.float32)
        objp[:,:2] = np.mgrid[0:w,0:h].T.reshape(-1, 2)

        #储存棋盘格角点的世界坐标和图像坐标
        objpoints = [] #在世界坐标系中的三维点
        imgpoints = [] #在平面图像的二维点

        count = 0

        if not self._camera.isOpened():
            print("Camera is not opened!")
            return
        else:
            while True:
                ret, self._frame = self._camera.read()
                if not ret:
                    print("cannot read frame!")
                    return
                else:
                    gray = cv.cvtColor(self._frame, cv.COLOR_BGR2GRAY)
                    
                    #找到棋盘格角点
                    ret, corners = cv.findChessboardCorners(gray, (w, h), cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_FAST_CHECK + cv.CALIB_CB_NORMALIZE_IMAGE)
                    
                    if ret == True:
                        #在原角点的基础上寻找亚像素点
                        corners = cv.cornerSubPix(gray, corners, (5, 5), (-1, -1), criterial)
                        objpoints.append(objp)
                        imgpoints.append(corners)
                        cv.drawChessboardCorners(self._frame, (w, h), corners, ret)
                        count = count + 1
                        if count >= 25:
                            self._camera.release()
                            break
                        
                    #把获取到的图像格式转换(编码)成流数据，赋值到内存缓存中;
                    retx, self._buffer = cv.imencode('.jpg', self._frame)
                    #将缓存里的流数据转成字节流
                    self._frame = self._buffer.tobytes()
                    #指定字节流类型image/jpeg
                    yield  (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + self._frame + b'\r\n')
            
            _ret, _mtx, _dist, _rvecs, _tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None, None)
            
            print("mtx:", _mtx)
            print("dist:", _dist)
            
            mean_error = 0
            for i in range(len(objpoints)):
                imgpoints2, _ = cv.projectPoints(objpoints[i], _rvecs[i], _tvecs[i], _mtx, _dist)
                error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
                mean_error = mean_error + error
            print("total error: ", mean_error / len(objpoints))
            
            np.savez('static/npz/calibrateCamera.npz', _mtx, _dist[0:4])
            
            print("Finshed!")
        
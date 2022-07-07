from flask import Flask, Response, redirect, render_template, request, url_for
from Robot_Camera import Robot_Camera
from Process import get_position

robot_webcam = Flask(__name__)

My_Robot_Camera = Robot_Camera()

#可设置的摄像头分辨率(width, height)有(320, 240)、(640, 480)、(1280, 720)、(1920, 1080)
#默认分辨率为640 * 480
_width = 640
_height = 480

#显示主界面
@robot_webcam.route('/', methods=['GET', 'POST'])
def show_home_page():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        if request.form["home button"] == "打开摄像头":
            return redirect(url_for("Open_Robot_Web_Camera"))
        elif request.form["home button"] == "打开摄像头(去畸变)":
            return redirect(url_for('Open_Robot_Web_Camera_Undistortion'))
        elif request.form["home button"] == "设置分辨率":
            return redirect(url_for('Set_Resolution'))
        elif request.form["home button"] == "摄像头标定":
            return redirect(url_for("Calibration"))

#打开摄像头
@robot_webcam.route('/Open_Robot_Web_Camera', methods = ['GET', 'POST'])
def Open_Robot_Web_Camera():
    if request.method == 'GET':
        return render_template('Open_Robot_Web_Camera.html')
    else:
        if request.form['close button'] == '关闭摄像头':
            return redirect(url_for('show_home_page'))

@robot_webcam.route('/open_robot_web_camera_on')
def open_robot_web_camera_on():
    return Response(My_Robot_Camera.Open_Robot_Web_Camera_On(0), mimetype='multipart/x-mixed-replace;boundary=frame')

#打开摄像头(去畸)
@robot_webcam.route('/Open_Robot_Web_Camera_Undistortion', methods = ['GET', 'POST'])
def Open_Robot_Web_Camera_Undistortion():
    if request.method == 'GET':
        return render_template('Open_Robot_Web_Camera_Undistortion.html')
    else:
        if request.form['close button'] == '关闭摄像头':
            return redirect(url_for('show_home_page'))
        
@robot_webcam.route('/open_robot_web_camera_undistortion_on')
def open_robot_web_camera_undistortion_on():
    return Response(My_Robot_Camera.Open_Robot_Web_Camera_Undistortion(0), mimetype='multipart/x-mixed-replace;boundary=frame')

#设置摄像机分辨率
@robot_webcam.route('/Set_Resolution', methods=['GET', 'POST'])
def Set_Resolution():
    if request.method == 'GET':
        return render_template("Set_Resolution.html")
    else:
        if request.form['set button'] == '设置分辨率':
            resolution = request.form.get('ResolutionList')
            print(resolution)
            global _width, _height
            pos = get_position(resolution)
            _width = int(resolution[0:pos-1])
            _height = int(resolution[pos+2:len(resolution)])
            return redirect(url_for('Set_Resolution'))
        elif request.form['return button'] == '返回主界面':
            return redirect(url_for('show_home_page'))
        
@robot_webcam.route('/set_resolution_on')
def set_resolution_on():
    print(_width)
    print(_height)
    return Response(My_Robot_Camera.Set_Resolution(0, _width, _height), mimetype='multipart/x-mixed-replace;boundary=frame')

#摄像头标定
@robot_webcam.route('/Calibration',methods=['GET', 'POST'])
def Calibration():
    if request.method == 'GET':
        return render_template("Calibration.html")
    else:
        return

@robot_webcam.route('/calibration_on')
def calibration_on():
    return Response(My_Robot_Camera.Calibration(0), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == '__main__':
    try:
        robot_webcam.run(host='0.0.0.0', port=5002, debug=True)
    except KeyboardInterrupt as e:
        pass

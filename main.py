from flask import Flask, Response, redirect, render_template, request, url_for
from Robot_Camera import Robot_Camera

robot_webcam = Flask(__name__)


My_Robot_Camera = Robot_Camera()

#显示主界面
@robot_webcam.route('/', methods=['GET', 'POST'])
def show_home_page():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        if request.form["home button"] == "打开摄像头":
            return redirect(url_for("Open_Robot_Web_Camera"))
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

#设置摄像机分辨率
@robot_webcam.route('/Set_Resolution', methods=['GET', 'POST'])
def Set_Resolution():
    if request.method == 'GET':
        return render_template("Set_Resolution.html")
    else:
        if request.form['set button'] == '设置分辨率':
            resolution = request.form.get('ResolutionList')
            print(resolution)
            return redirect(url_for('Set_Resolution'))
        elif request.form['return button'] == '返回主界面':
            return redirect(url_for('show_home_page'))
        
@robot_webcam.route('/set_resolution_on')
def set_resolution_on():
    return Response(My_Robot_Camera.Set_Resolution(0, 640, 480), mimetype='multipart/x-mixed-replace;boundary=frame')

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

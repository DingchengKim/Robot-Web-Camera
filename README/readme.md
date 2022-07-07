# Robot Web Camera使用说明

## 代码下载 git clone <https://github.com/DingchengKim/Robot-Web-Camera.git>

## 使用Robot Web Camera需要安装的相关python库

* ***Flask***
* ***numpy***
* ***opencv-python***

## 如何启动Robot Web Camera

* 运行main.py后即可启动Robot Web Camera.
* 成功启动Robot Web Camera后显示界面如下:
![主界面展示](/README/show/home_page.png)

## Robot Web Camera功能

1. ***摄像头标定***
    >摄像头标定流程
    >>
    >>第一步:开启摄像头标定功能。
    >>
    >>![开启标定功能](/README/show/calibration_button.png)
    >>
    >>第二步:使用标定板进行标定。
    >>
    >>![进行标定](/README/show/calibration_on.png)
    >>
    >>第三步:适当变换标定板角度，直至标定结束。当标定结束时在终端会出现以下内容，并且在***static/npz***文件夹下生成***calibrateCamera.npz***文件。
    >>
    >>![标定结束](/README/show/calibration_finshed.png)
    >>
    >>![npz文件](/README/show/npzfile.png)
    >
    >***<font color=Red>注意!</font>***
    >
    >***<font color=Red>使用此功能时画面显示会有严重卡顿，但不影响功能的实现!</font>***

2. ***设置摄像头分辨率***
    >摄像头可设置4种分辨率(width, height)，分别为(320, 240)、(640, 480)、(1280, 720)、(1920, 1080)。
    >
    >设置摄像头分辨率流程
    >>第一步:开启设置分辨率功能。
    >>
    >>![开启设置分辨率功能](/README/show/set_resolution_button.png)
    >>
    >>第二步:选择想要设置的分辨率，然后点击设置分辨率。成功设置分辨率后会在终端显示选择的分辨率。
    >>
    >>![设置分辨率](/README/show/set_resolution.png)
    >>
    >>![可选择的分辨率](/README/show/ResolutionList.png)
    >>
    >>![选择的分辨率](/README/show/resolution.png)
    >
    >***<font color=Red>注意!</font>***
    >
    >***<font color=Red>设置分辨率后需要手动刷新页面!</font>***

3. ***开启摄像头***
    >开启摄像头流程
    >>第一步:开启摄像头功能。
    >>
    >>![开启摄像头功能](/README/show/open_camera.png)
    >>
    >>第二步:网页中出现画面表示摄像头开启成功。
    >>
    >>![成功开启摄像头](/README/show/open_camera_on.png)
    >>
    >>可点击关闭摄像头按钮来关闭摄像头，并回到主页面。
    >>
    >>![关闭摄像头](/README/show/close_camera_button.png)

4. ***开启去畸变后的摄像头***
    >开启去畸变后的摄像头流程
    >>第一步:检查是否在***static/npz***文件夹下存在***calibrateCamera.npz***文件。
    >>
    >>![.npz文件](/README/show/npzfile.png)
    >>
    >>如果不存在先使用***摄像头标定功能***，否则在终端会出现如下错误。
    >>
    >>![错误](/README/show/error.png)
    >>
    >>第二步:开启摄像头功能
    >>
    >>![开启摄像头功能](/README/show/open_camera_undistortion_button.png)
    >>
    >>第三步:网页中出现画面表示摄像头开启成功。
    >>
    >>![去畸变后的摄像头画面](/README/show/open_camera_undistortion_on.png)
    >>
    >>可点击关闭摄像头按钮来关闭摄像头，并回到主页面。
    >>
    >>![关闭摄像头](/README/show/close_camera_button.png)

## ***<font color=Red>注意事项</font>***

* ***<font color=Red>运行时时可能出现如下问题，当遇到时只需刷新页面1~2次即可，这些问题不影响功能的实现!</font>***

    >![问题一](/README/show/problem1.png)
    >
    >![问题二](/README/show/problem2.png)

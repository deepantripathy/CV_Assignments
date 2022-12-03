"# OakD-Camera-Calibration" <br>
Files and their purpose<br><br>

Answer 1: <br>
Created depth_capture_color.py to click color pictures of target(in our case it was a 2x2 image of a chess board) <br>
Caliberated the camera using opencv.caliberateCamera() and calculated the camera matrix = Intrinsic matrix * Extrinsic matrix<br><br>

Answer 2<br>
Created program calculate_dimensions.py to take calculate sides of our target using the perspective projection equation and calculated the length and width of our chess board.<br><br>

Answer 3<br>
No its not feasible. I ran the RGB stream from mono camera using program depth_capture_mono.py and the depth_capture_stereo.py but got an error saying camera unrecognizable<br><br>


Answer 4 <br>
Ran the calibration test from luxinos documentation<br>
Luxinos caliberation Intrinsic matrix:<br>
[[485.76662085   0.         314.22305371]<br>
 [  0.         484.6142758  177.89428718]<br>
 [  0.           0.           1.        ]]<br><br>

Our program Intrinsic matrix:<br>
[[396.25760498   0.         313.0033623 ]<br>
 [  0.         411.10607861 251.44362313]<br>
 [  0.           0.           1.        ]]<br>



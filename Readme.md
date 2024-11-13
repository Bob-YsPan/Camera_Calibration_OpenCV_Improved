# Camera calibration improved version
Fork from the tarkers calibration script but fixed some bugs like
* Not easy to parse the list into the argument
* Some directory like the input image's folder is fixed

## Example command
```bash session
# Use default value
$ python ./calibration.py 
# or
$ python ./calibration.py -sr <row> -sc <col> -m <length(mm)> -S "<directory>" -l "<directory>" -c "<directory>" -f "<format string>"
# Example of use the all arguments
$ python ./calibration.py -sr 6 -sc 8 -m 25 -S "saves" -l "distorted_image" -c "calibrate" -f "png"
```


## Usage
```bash session
$ python ./calibration.py --help
usage: calibration.py [-h] [-sr SIZE_ROW] [-sc SIZE_COL] [-m MM] [-S SAVE_DIR] [-l LOAD_DIR] [-c IMG_CAL] [-f S_FORMAT]

optional arguments:
  -h, --help            Show this help message and exit
  -sr SIZE_ROW, --size_row SIZE_ROW
                        Enter number of row points, default is 6
  -sc SIZE_COL, --size_col SIZE_COL
                        Enter number of col points, default is 8
  -m MM, --mm MM        Enter square length of chessboard (unit:mm) default is 25
  -S SAVE_DIR, --save_dir SAVE_DIR
                        Directory to save undistorted images, default is "saves"
  -l LOAD_DIR, --load_dir LOAD_DIR
                        Directory to load distorted images, default is "distorted_image"
  -c IMG_CAL, --img_cal IMG_CAL
                        Directory that contain images for camera calibration, default is "calibrate"
  -f S_FORMAT, --s_format S_FORMAT
                        The file extension of the images, default is "jpg"
```
## Results
Will generate 3 types of the files:
* Undistorted image will be put to the "saves" directory(or the directory you defined)
* cam_distortion.npy (distortion coefficients)

```
===distortion coefficients===
 [[-0.45001136  0.29154511  0.00666282 -0.00271199 -0.14259603]]
```
* cam_matrix.npy (camera matrix)

```
===camera matrix===
 [[1.31907047e+03 0.00000000e+00 9.32161790e+02]
 [0.00000000e+00 1.31702001e+03 5.16839639e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]]
```

* Example command output

Calibration file not exist(Calibrate, Load and Process)
```
$ python ./calibration.py -f "png"
Calibrate parameters =  6 8 1 calibrate
Calibrate images =  ['calibrate/vlcsnap-2024-11-13-17h00m02s504.png', 'calibrate/vlcsnap-2024-11-13-17h02m09s068.png', 'calibrate/vlcsnap-2024-11-13-17h02m25s358.png', 'calibrate/vlcsnap-2024-11-13-17h00m31s628.png', 'calibrate/vlcsnap-2024-11-13-17h02m11s085.png', 'calibrate/vlcsnap-2024-11-13-17h00m59s179.png', 'calibrate/vlcsnap-2024-11-13-17h01m17s494.png']
total error: 0.10419185265976963
matrix save !!
Image to be undistorted =  ['distorted_image/vlcsnap-2024-11-13-17h00m02s504.png', 'distorted_image/vlcsnap-2024-11-13-17h01m17s494.png']
===camera matrix===
 [[1.31907047e+03 0.00000000e+00 9.32161791e+02]
 [0.00000000e+00 1.31702001e+03 5.16839640e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]] 

===distortion coefficients===
 [[-0.45001135  0.29154511  0.00666282 -0.00271199 -0.14259603]] 

----------transform images---------------
Writing:  saves/vlcsnap-2024-11-13-17h00m02s504.png
Writing:  saves/vlcsnap-2024-11-13-17h01m17s494.png
save Done!
```

Calibration file exist(Load and Processing)
```
$ python ./calibration.py -sr 6 -sc 8 -m 25 -S "saves" -l "distorted_image" -c "calibrate" -f "png"
!!! Calibrate file found, if need re-calibrate, delete 2 .npy files generated at directory!
Image to be undistorted =  ['distorted_image/vlcsnap-2024-11-13-17h00m02s504.png', 'distorted_image/vlcsnap-2024-11-13-17h01m17s494.png']
===camera matrix===
 [[1.31907047e+03 0.00000000e+00 9.32161790e+02]
 [0.00000000e+00 1.31702001e+03 5.16839639e+02]
 [0.00000000e+00 0.00000000e+00 1.00000000e+00]] 

===distortion coefficients===
 [[-0.45001136  0.29154511  0.00666282 -0.00271199 -0.14259603]] 

----------transform images---------------
Writing:  saves/vlcsnap-2024-11-13-17h00m02s504.png
Writing:  saves/vlcsnap-2024-11-13-17h01m17s494.png
save Done!
```
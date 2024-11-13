import argparse
from array import array
def calibration_parser():
    # args
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-sr", "--size_row", help="Enter number of row points, default is 6", type=int, default=6)
    parser.add_argument(
        "-sc", "--size_col", help="Enter number of col points, default is 8", type=int, default=8)
    parser.add_argument(
        "-m", "--mm", help="Enter square length of chessboard (unit:mm) default is 25", type=int, default=1)
    parser.add_argument(
        "-S", "--save_dir", help="Directory to save undistorted images, default is \"saves\"", default="saves")
    parser.add_argument(
        "-l", "--load_dir", help="Directory to load distorted images, default is \"distorted_image\"", default="distorted_image")
    parser.add_argument(
        "-c", "--img_cal", help="Directory that contain images for camera calibration, default is \"calibrate\"", default="calibrate")
    parser.add_argument(
        "-f", "--s_format", help="The file extension of the images, default is \"jpg\"", default="jpg")
    return parser
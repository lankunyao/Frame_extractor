import argparse
import os
import sys
from PIL import Image
import cv2


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='video',
                        help='the path to the folder of the original video')
    parser.add_argument('--output_path', type=str, default='img',
                        help='the path to the folder of the output frame')
    parser.add_argument('--interval', type=int, default=25,
                        help='the interval of the extraction')
    args = parser.parse_args()
    return args


def get_frame_from_video(input_path, output_path, interval, video):
    output_path = os.path.join(output_path, video, '1.mp4')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    input_path = os.path.join(input_path, video)
    video_capture = cv2.VideoCapture(input_path)

    i = 0
    j = 0

    while True:
        flag, frame = video_capture.read()
        i += interval
        if flag:
            j += 1
            cv2.imwrite(os.path.join(output_path, '{}_{}.jpg'.format(video, j)), frame)
        else:
            break


def main():
    sys.path.insert(0, '.')
    print('sys.path is:\n\t{}'.format('\n\t'.join(sys.path)))
    cfg = parse_args()
    input_path = cfg.input_path  # 源文件所在文件夹的绝对路径
    output_path = cfg.output_path
    interval = cfg.interval
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    filenames = os.listdir(input_path)
    for video in filenames:
        get_frame_from_video(input_path, output_path, interval, video)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse
import time
import torch
import os


def alg(input_dir, output_dir):
    print("start pred !")
    input_path = input_dir
    output_path = output_dir
    pwd = os.path.dirname(os.path.realpath(__file__))
    print("path:   ",pwd)
    status = os.system(pwd+ '/infer_remote_rotation_plane.sh' + ' ' +  input_path + ' ' + output_path)
    print("end pred !")

    #pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # 数据集路径
    parser.add_argument("--input_dir", default='/input_path', help="input path", type=str)
    # 输出路径
    parser.add_argument("--output_dir", default='/output_path', help="output path", type=str)
    args = parser.parse_args()
    start_time = time.time()
    torch.backends.cudnn.benchmark = True
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    alg(args.input_dir, args.output_dir)
    print('total time:', time.time() - start_time)

import sys
import adapter
import os

def main():
    args = sys.argv
    input_dir = args[1]
    npy_dir = args[1][:-1] + '_npy/'
    output_dir = args[2]
    adapter.convert_images_in_dir(input_dir, npy_dir)
    os.system(f'bash ./rgb-footprint-extract/run.sh {npy_dir} {output_dir}')


if __name__ == '__main__':
    main()

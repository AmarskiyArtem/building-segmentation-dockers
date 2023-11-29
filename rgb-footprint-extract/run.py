import sys
import adapter
import os

def main():
    args = sys.argv
    npy_dir = '/home/user/programming/squareTest/2_npy/'
    #npy_folder = args[1][:-1] + '_npy/'
    input_dir = '/home/user/programming/squareTest/2/'
    output_dir = '/home/user/programming/new_test/'
    adapter.convert_images_in_dir(input_dir, npy_dir)
    os.system('bash run.sh {npy_dir} {output_dir}')
    print('ok')

if __name__ == '__main__':
    main()
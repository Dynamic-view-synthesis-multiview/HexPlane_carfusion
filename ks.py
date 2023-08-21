import argparse
import glob
import os
import cv2
import imageio
import numpy as np


SAVE_IMG = True
FINAL_H = 288

# inverse of transformation matrix
def inverse_of_transformation_matrix(Tr):
    R = Tr[0:3, 0:3]
    t = Tr[0:3, 3]
    T_inv = np.vstack((np.hstack((R.T, -(R.T @ t).reshape(-1, 1))),
                         [0, 0, 0, 1]))
    return T_inv

def read_intrinsics(filename: str) -> tuple:
    '''
    
    '''
    # print(f"{intrinsics_file}")
    if os.path.exists(filename): 
        with open(filename) as f:
            lines = f.readlines()
        index, K = [], []
        for line in lines:
            index.append(line.split(' ')[0])
            Int = np.array(line.split(' ')[5:10]).astype(float)
            K_computed = np.asarray([[Int[0],0.0,Int[3]],[0.0,Int[1],Int[4]],[0.0,0.0,1.0]], dtype = float)
            K.append(K_computed)
        return K, index
    
if __name__ == '__main__':
#   parser = argparse.ArgumentParser()
  # parser.add_argument('--cvd_dir', type=str, help='depth directory')
#   parser.add_argument('--camera_dir', type=str, help='camera params directory')   #/home/jayaram/research/research_tracks/dynamic_nerf_reconstruction/dynibar/dynibar_dataset/carfusion_small_dataset/dense/camera_params
#   parser.add_argument('--depth_dir', type=str, help='depth directory')   ##/home/jayaram/research/research_tracks/dynamic_nerf_reconstruction/dynibar/dynibar_dataset/carfusion_small_dataset/dense/depth
#   parser.add_argument('--data_dir', type=str, help='dataset directory') #/home/jayaram/research/research_tracks/dynamic_nerf_reconstruction/dynibar/dynibar_dataset/carfusion_small_dataset
#   # parser.add_argument("--scene_name", type=str, 
#                       # help='Scene name') # 'kid-running'
#   args = parser.parse_args()

#   pt_out_list = sorted(glob.glob(os.path.join(args.camera_dir, '*.npz')))    #this is list of camera extrinsic params
#   data_dir = os.path.join(args.data_dir, 'dense')

#   try:
#     original_img_path = os.path.join(data_dir, 'images', '000000.png')
#     o_img = imageio.imread(original_img_path)
#   except:
#     original_img_path = os.path.join(data_dir, 'images', '000000.jpg')
#     o_img = imageio.imread(original_img_path)

#   o_ar = float(o_img.shape[1]) / float(o_img.shape[0])
#   final_w, final_h = int(round(FINAL_H * o_ar)), int(FINAL_H)

#   original_img_dir = os.path.join(data_dir, 'images')
# #   img_dir = os.path.join(data_dir, 'images_%dx%d' % (final_w, final_h))
# #   os.makedirs(img_dir, exist_ok=True)
# #   print('img_dir ', img_dir)
# #   disp_dir = os.path.join(data_dir, 'disp')
# #   os.makedirs(disp_dir, exist_ok=True)  #do we need to comment here?

    Ks = []  #intrinsic matrices
    mono_depths = []
    c2w_mats = []
    imgs = []
    bounds_mats = []

    intrinsics_path = "/home/sky/Engg/MS/recons/body_slam/live_stream/carfusion/Morewood/CamPose_0000.txt"
    file = ['camera_params/frame_000000.npz', 'camera_params/frame_000001.npz', 'camera_params/frame_000002.npz', 'camera_params/frame_000003.npz',
            'camera_params/frame_000004.npz', 'camera_params/frame_000005.npz', 'camera_params/frame_000006.npz', 'camera_params/frame_000007.npz',
            'camera_params/frame_000008.npz', 'camera_params/frame_000009.npz', 'camera_params/frame_000010.npz']
    Tx = []
    Ty = []
    Tz = []
    # for shit in file:
        # pt_data = np.load(shit)
    Ks, index = read_intrinsics(intrinsics_path)

    print(Ks[0])
    exit()
    # print(Ks)
    K = Ks[0]
    # print(K)
    cam_w2c = pt_data['world2cam']   #4*4 matrix

    # print(cam_w2c)
    # Tx.append(cam_w2c[0,3])
    # Ty.append(cam_w2c[1,3])
    # Tz.append(cam_w2c[2,3]) 
    
    cam_c2w = inverse_of_transformation_matrix(cam_w2c)
    Tx.append(cam_c2w[0,3])
    Ty.append(cam_c2w[1,3])
    Tz.append(cam_c2w[2,3]) 
    # print(cam_c2w)
    # exit()
    K[0, :] *= 800 / 1920#img.shape[1]    
    K[1, :] *= 800 / 1080#img.shape[0]
    print(K)
    fx, fy = K[0, 0], K[1, 1]

    # print(fx, fy)
    # print(bounds_mats)
    # print('bounds_mats ', np.min(bounds_mats), np.max(bounds_mats))
    # exit()
    print(max(Tx), min(Tx))
    print(max(Ty), min(Ty))
    print(max(Tz), min(Tz))
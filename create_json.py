import json
import numpy as np
import os
from ogks import read_extrinsics

def inverse_of_transformation_matrix(Tr):
    R = Tr[0:3, 0:3]
    t = Tr[0:3, 3]
    T_inv = np.vstack((np.hstack((R.T, -(R.T @ t).reshape(-1, 1))),
                         [0, 0, 0, 1]))
    return T_inv

purpose = 'test'
cam_pose_path = '/home/sky/Engg/MS/recons/body_slam/live_stream/carfusion/Morewood/CamPose_0000.txt'
w2c, _, _ = read_extrinsics(cam_pose_path)
train_path = f'mini/{purpose}/'
frames = []
img_path = sorted(os.listdir(train_path))
# print(img_path)
# exit()
Xs = []
Ys = []
Zs = []
for count, i in enumerate(w2c):
    # if count >= 11:
    #     break
    # print(i)
    # i = inverse_of_transformation_matrix(i)
    # print(i[:, 3])
    Xs.append(i[:, 3][0])
    Ys.append(i[:, 3][1])
    Zs.append(i[:, 3][2])
    
print(max(Xs), min(Xs))
print(max(Ys), min(Ys))
print(max(Zs), min(Zs))


    # print(count)
    # print(i)
#     i = np.concatenate((i, np.array([[0, 0, 0, 1]])), axis=0)
#     # print(i)
    
#     frame_dict = {
#         "file_path": './'+train_path.split('/')[1] + '/' +img_path[count][:-4],
#         "rotation": 0,
#         "time": int(img_path[count][:-4]) * (1/30),
#         "transform_matrix": inverse_of_transformation_matrix(i).tolist()
#     }
#     # print(frame_dict['transform_matrix'])
#     # exit()
#     frames.append(frame_dict)
# final_dict = {
#     "camera_angle_x": 0,
#     "frames": frames
# }

# # print(final_dict)
# final = json.dumps(final_dict, indent=4)
# # print(final)
# with open(f"mini/transforms_{purpose}.json", "w") as outfile:
#     outfile.write(final)
#     json.dumps(final_dict, outfile)


exit()
purpose = 'train'
train_path = f'smallerForHexFusion/{purpose}/'
camera_extrinisic_path = 'camera_params/'
frames = []
for i in os.listdir(train_path):
    # print(i)
    data = np.load(camera_extrinisic_path+'frame_'+i[:-4]+'.npz')
    # print(data['world2cam'])
    # exit()

    frame_dict = {
        "file_path": './'+train_path.split('/')[1] + '/' +i[:-4],
        "rotation": 0,
        "time": int(i[:-4]) * (1/30),
        "transform_matrix": inverse_of_transformation_matrix(data['world2cam']).tolist()
    }
    # print(frame_dict['transform_matrix'])
    # exit()
    frames.append(frame_dict)

final_dict = {
    "camera_angle_x": 0,
    "frames": frames
}

# print(final_dict)
final = json.dumps(final_dict, indent=4)
# print(final)
with open(f"smallerForHexFusion/transforms_{purpose}.json", "w") as outfile:
    outfile.write(final)
#     json.dumps(final_dict, outfile)
    
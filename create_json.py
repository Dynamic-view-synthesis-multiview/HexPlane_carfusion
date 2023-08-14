import json
import numpy as np
import os

train_path = 'ForHexPlane/val/'
camera_extrinisic_path = 'camera_params/'
frames = []
for i in os.listdir(train_path):
    # print(i)
    data = np.load(camera_extrinisic_path+'frame_'+i[:-4]+'.npz')
    # print(data['world2cam'])
    # exit()

    frame_dict = {
        "file_path": './'+train_path+i[:-4],
        "rotation": 0,
        "time": 0,
        "transform_matrix": data['world2cam'].tolist()
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
with open("ForHexPlane/transforms_val.json", "w") as outfile:
    outfile.write(final)
#     json.dumps(final_dict, outfile)
    
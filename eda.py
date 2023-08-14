from PIL import Image
import numpy as np

img = Image.open('data/standup/train/r_001.png')
arr = np.asarray(img)
print(arr[:,:,0])
print(np.max(arr[:,:,0]))
print(np.min(arr[:,:,0]))


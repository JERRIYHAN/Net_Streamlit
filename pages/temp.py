from PIL import Image
import numpy as np

im = np.array(Image.open('./media/logo-haircut.png'))
with np.nditer(im, flags=['multi_index'], op_flags=['writeonly']) as it:
    while not it.finished:
        if it.multi_index[2] == 3:
            if r == g == b == 255:
                it[0] = 0
        elif it.multi_index[2] == 0:
            r = it[0]
        elif it.multi_index[2] == 1:
            g = it[0]
        elif it.multi_index[2] == 2:
            b = it[0]
        is_not_finished = it.iternext()

horizontalImg = Image.fromarray(im)
horizontalImg.save('./media/logo-alpha.png')
from cost_function import *
from pic import *
s = "(V 0.5 (H 0.5 (L 255 0 0) (L 0 0 255)) (L 255 255 255))"
x = to_array(s, 600, 600, 1)
print(x.shape)
print(x)
rgb2pic(np.array(x,dtype=np.uint8))
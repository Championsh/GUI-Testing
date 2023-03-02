import cv2
import glob
from tqdm import tqdm
from fractions import Fraction

unique = []
path = "D:\\combined/195*.jpg"
for filename in tqdm(glob.glob(path)):
    im = cv2.imread(filename)
    h, w, c, = im.shape
    tmp_s = str(h) + 'x' + str(w)
    # print(tmp_s)
    # print(Fraction(h, w))
    unique.append(tmp_s)
    unique.append(Fraction(h, w))

unique = set(unique)
print(unique)

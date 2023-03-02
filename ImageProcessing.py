import cv2
import glob
from tqdm import tqdm
from fractions import Fraction

unique = []
path = "D:\\combined/19*.jpg"

for filename in tqdm(glob.glob(path)):
    im = cv2.imread(filename)
    h, w, c = im.shape
    tmp_s = str(h) + 'x' + str(w)
    if tmp_s not in unique:
        unique.append(tmp_s)
        tmp = Fraction(h, w)
        tmp_s = str(tmp.numerator) + '/' + str(tmp.denominator)
        if tmp_s not in unique:
            unique.append(tmp_s)

print(unique)

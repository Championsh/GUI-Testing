import cv2
import glob
from tqdm import tqdm
from fractions import Fraction

unique = {}
path = "D:\\combined/19*.jpg"
res_path = "D:\\ImageProcessing/res.json"
for filename in tqdm(glob.glob(path)):
    im = cv2.imread(filename)
    h, w, c = im.shape
    tmp_s = str(h) + 'x' + str(w)
    if tmp_s not in unique:
        unique[tmp_s] = 1
        tmp = Fraction(h, w)
        tmp_s = str(tmp.numerator) + '/' + str(tmp.denominator)
        if tmp_s not in unique:
            unique[tmp_s] = 1

unique = set(unique)
print(unique)

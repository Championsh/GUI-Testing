import argparse
import json
import glob
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-path", "--path", type=str,
                    help="Input the data's path, if not specified=D:\\\\combined/*.jpg",
                    default="D:\\\\combined/119*.json")
args = parser.parse_args()


def recursive_sonSearch(searchlist):
    max_sons = 0
    OBJECT = "children"
    if OBJECT in searchlist:
        max_sons = len(searchlist[OBJECT])
        for i in range(max_sons):
            if not isinstance(searchlist[OBJECT][i], dict):
                tmp_sons = recursive_sonSearch(searchlist[OBJECT][i])
            else:
                break
            if max_sons < tmp_sons:
                max_sons = tmp_sons
    return max_sons


histlist = []
for filename in glob.glob(args.path):
    data = json.load(open(filename, 'r'))["activity"]["root"]
    sons = recursive_sonSearch(data)
    histlist.append(sons)

plt.hist(histlist, bins=10, color='blue', edgecolor='black')
plt.title('MAX_GUI_SONS')
plt.xlabel('Nodes')
plt.ylabel('MAX_SONS')
plt.show()

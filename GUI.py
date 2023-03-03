import argparse
import json
import glob
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-path", "--path", type=str,
                    help="Input the data's path, if not specified=D:\\\\combined/*.jpg",
                    default="D:\\\\combined/*.json")
parser.add_argument("-func", "--func", type=str,
                    help="Input the traversal algorithm (po/r/cmp), if not specified: Post Order",
                    default="po", choices=['po', 'r', 'cmp'])
args = parser.parse_args()

OBJECT = "children"


def recursive_sonSearch(searchlist):
    max_sons = 0
    if isinstance(searchlist, dict) and OBJECT in searchlist:
        cur_list = searchlist[OBJECT]
        max_sons = len(cur_list)
        for i in range(max_sons):
            tmp_sons = recursive_sonSearch(cur_list[i])
            if max_sons < tmp_sons:
                max_sons = tmp_sons
    return max_sons


tmp_max = 0


def postorder_traversal(searchlist):
    global tmp_max
    if isinstance(searchlist, dict) and OBJECT not in searchlist:
        return
    elif searchlist is None:
        return
    cur_list = searchlist[OBJECT]
    sons = len(cur_list)
    for i in range(sons):
        postorder_traversal(cur_list[i])
    if tmp_max < sons:
        tmp_max = sons


histlist = []
for filename in glob.glob(args.path):
    data = json.load(open(filename, 'r'))["activity"]["root"]
    if args.func == "po":
        postorder_traversal(data)
        histlist.append(tmp_max)
        tmp_max = 0
    elif args.func == "r":
        sons = recursive_sonSearch(data)
        histlist.append(sons)
    else:
        postorder_traversal(data)
        print(f"{recursive_sonSearch(data)}vs{tmp_max}")
        tmp_max = 0

plt.hist(histlist, bins=10, color='blue', edgecolor='black')
plt.title('MAX_GUI_SONS')
plt.ylabel('Nodes')
plt.xlabel('MAX_SONS')
plt.show()

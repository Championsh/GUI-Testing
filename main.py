import json
import glob
import matplotlib.pyplot as plt
from tqdm import tqdm

def sonSearch(searchlist):
    max_sons = 0
    if "children" in searchlist:
        max_sons = len(searchlist["children"])
        for i in range(max_sons):
            if type(searchlist["children"][i]) == type(list):
                tmp_sons = sonSearch(searchlist["children"][i])
            else:
                break
            if max_sons < tmp_sons:
                max_sons = tmp_sons
    return max_sons


histlist = {}
path = "D:\\combined/*.json"
for filename in tqdm(glob.glob(path)):
    data = json.load(open(filename, 'r'))["activity"]["root"]
    sons = sonSearch(data)
    if sons in histlist:
        histlist[sons] += 1
    else:
        histlist[sons] = 1
    #print("MAX_SONS:", sons)

#print(histlist)
histtmp = [key for key, val in histlist.items() for _ in range(val)]
plt.hist(histtmp, bins=10, color='blue', edgecolor='black')
plt.title('MAX_GUI_SONS')
plt.xlabel('Nodes')
plt.ylabel('MAX_SONS')
plt.show()

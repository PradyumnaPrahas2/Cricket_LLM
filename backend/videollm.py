import sys
import re,time
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
import numpy as np
import json
import warnings
warnings.filterwarnings('ignore')
start_time=time.time()
sen=sys.argv[1]
test_vec1=model.encode([sen])[0]
filename = 'Videos.json'
with open(filename, 'r') as json_file:
    data_loaded = json.load(json_file)
hashmap=[]
for i in range(len(data_loaded)):
    test_vec3=np.array(data_loaded[str(i)]['vector'])
    similarity_score = 1-distance.cosine(test_vec1,test_vec3)
    if(similarity_score>0.70):
        hashmap.append([data_loaded[str(i)]['description'],data_loaded[str(i)]['url'],similarity_score])
sorted_list = sorted(hashmap, key=lambda x: x[2],reverse=True)
hashmap=[[i[0],i[1]] for i in sorted_list]
print(hashmap)
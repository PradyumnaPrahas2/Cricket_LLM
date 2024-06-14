import re,time
from scipy.spatial import distance
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
import sys
import numpy as np
import json
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')
from queue import PriorityQueue
generator = pipeline("text-generation", model="gpt2")
start_time=time.time()
sen=sys.argv[1]
test_vec1=model.encode([sen])[0]
filename = 'data.json'
with open(filename, 'r') as json_file:
    data_loaded = json.load(json_file)
hashmap={}
for i in range(3041):
    test_vec3=np.array(data_loaded[str(i)]['vector'])
    similarity_score = 1-distance.cosine(test_vec1,test_vec3)
    if(similarity_score>0.63):
        m=data_loaded[str(i)]['question'].strip()
        n=data_loaded[str(i)]['answer'].strip()
        hashmap[m+' '+n]=similarity_score
s=''
count=7
for i in hashmap:
    s=s+i[0]+'\n'
    if(count<=0):
        break
    count-=1
    
    
with open("data_context.json","r") as outfile:
    saved_data=json.load(outfile)
que=sen
for i in range(len(saved_data)):
    test_vec2=np.array(saved_data[str(i)]['vector'])
    similarity_score=1-distance.cosine(test_vec2,test_vec1)
    if(similarity_score>0.60):
        hashmap[saved_data[str(i)]['sentence'].strip()]=similarity_score
hashmap = sorted(hashmap.items(), key=lambda item: item[1] ,reverse=True)
count=7
# print(hashmap)
for i in hashmap:
    s=s+i[0]+'\n'
    if(count<=0):
        break
    count-=1
# print(s)
if(len(s)==0):
    print("Sorry i cannot answer that!")
else:
    pattern = r"(W\n)+"

    # Replace the matched pattern with an empty string
    s = re.sub(pattern, "", s)
    context = s.lower()
    question = que.lower()
    qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    result = qa_pipeline(question=question, context=context)
    print(f"Answer:{result['answer']}")
import json
# with open("combined_10000.json","r") as f:
#     saved_file=json.load(f)
# s=''
# for obj in saved_file:
#     #print(obj['context'])
#     #break;
#     s=s+obj['context']+'.'
# f=open("saved_context.txt","w")
# f.write(s)
# print("Task completed")
f=open("saved_context.txt","r")
print(f.read())
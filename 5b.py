import sys
from functools import reduce

f=open(sys.argv[1])
#make a text file say counting.txt(in same location)
#in terminal run: python3 sk_5b.py counting.txt
contents=f.read().split()
print("\nfile Contents:")

print(*contents,sep=' ')
count_dict={}
for word in contents:
    if word in count_dict:
        count_dict[word]=count_dict[word]+1
    else:
        count_dict[word]=1
print("\n\n",count_dict)
print("\n10 Words in decreasing order of occurance:")

s=(sorted(count_dict.items(),key=lambda x:x[1],reverse=True))
print(s[:10])
wordlen=[len(i) for i,j in s[:10]]
print("\nList with length of each word:\n",wordlen)
avg=(reduce(lambda x,y:x+y,wordlen))/len(wordlen)
print("Avg: ",avg)

sq_odd=[i*i for i in wordlen if i%2!=0]

print("Square of odd numbers: \n",sq_odd)

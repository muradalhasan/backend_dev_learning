num=input()
idx=int(input())
new=''
for i in range(idx,-1,-1):
    new+=num[i]
if idx!=len(num):
    new+=num[idx+1:]
print(new)
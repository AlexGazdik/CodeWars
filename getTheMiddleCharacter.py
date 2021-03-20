def get_middle(s):
    count=0
    for i in s:
        count+=1
    mid=count//2
    if count % 2==0:
        return s[mid-1: mid+1]
    else:
        return s[mid]

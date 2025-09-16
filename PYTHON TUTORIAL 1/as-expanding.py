def expanding(l):
    le=len(l)
    for i in range(0,le-1):
        if(l[i+1]-l[i]<=l[i+2]-l[i+1]):
            return True
        else:
            return False
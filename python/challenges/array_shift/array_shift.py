def insertShiftArray(l,val):
    if len(l)==0 or type(val)!=int:
        return 'plz enter valid inputs'
    if len(l)%2==0:

        index=len(l)//2


        l=l[:index]+[val]+l[index:]

    elif len(l)%2!=0:
        index=len(l)//2+1
        l=l[:index]+[val]+l[index:]

    return l





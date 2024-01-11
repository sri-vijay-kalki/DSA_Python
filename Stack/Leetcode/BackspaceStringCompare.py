def backspaceCompare( s, t):
    i = len(s)-1
    j = len(t)-1
    while i>=0 and j>=0:
        hashCount = 0
        while(s[i] == "#"):
            i-=1
            hashCount+=1
        if(hashCount!=0):
            while hashCount:
                if s[i] =="#":
                    hashcount+=1
                else:
                    hashCount-=1
                i-=1

            hashCount = 0

        while(t[j] =="#"):
            j-=1
            hashCount+=1
        if(hashCount!=0):
            while hashCount:
                if t[j] =="#":
                    hashCount+=1
                else:
                    hashCount-=1
                j-=1
            hashCount = 0
        if(i<0 and j<0):
            return True
        if(i<0):
            while(j>=0):
                if(hashCount>0):
                    j-=1
                if(t[j] != "#"):
                    return False
                else:
                    hashCount+=1
                j-=1
            return True
        if(j<0):
            while(i>=0):
                if(s[i] != "#"):
                    return False
                i-=1
            return True
        if(s[i]==t[j]):
            i-=1
            j-=1
        else: 
            return False
    return True

print(backspaceCompare ("ab##", "c#d#"))

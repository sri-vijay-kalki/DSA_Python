def plusOne( digits):
    i = len(digits)-1
    while i>=0:
        if(digits[i]!=9):
            digits[i]+=1
            return digits
        digits[i] = 0
    digits.insert(0,1)
    return digits

print(plusOne([9]))
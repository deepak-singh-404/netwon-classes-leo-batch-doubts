def MagicNumber(num):
    if (num > 100):
        # Get last two digit of number
        last_two_digit = int(str(num)[-2:])
        diff = 0
        if (last_two_digit > 79 and last_two_digit <97):
            tempdiff1 = last_two_digit - 79
            tempdiff2 = 97 - last_two_digit
            if (tempdiff1 >= tempdiff2):
                diff = tempdiff2
            else:
                diff =  tempdiff1
            return diff
        if (last_two_digit < 79):
            diff = 79 - last_two_digit
            return diff
        if (last_two_digit > 97):
            diff = last_two_digit - 97
            return diff
        
        return diff
    else:
        return 0

print(MagicNumber(188))

#162
#79
#80
#97
#101

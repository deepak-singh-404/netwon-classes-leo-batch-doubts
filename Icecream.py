def Main(total_input_icream,days_count):

    if(days_count == 0):
        return total_input_icream

    icecream_left = total_input_icream

    for day in range(0,days_count):
        quotient = icecream_left // 2
        multiplier =  (icecream_left - quotient) * 3
        icecream_left =   multiplier
    return icecream_left


print(Main(5,1))


        
        

    

   




        



    




        
        




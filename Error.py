def Error_Test(Type,Func_input, Lrange,Urange):
    
    True_False=0
    conver={
        "int": int,
        "str": str,
        "char": str,
        "float": float,
    }
    test_type = conver.get(Type, str) 
    try:
        #Test type is str int or float. char is a str but with a length of 1.
        test_type(Func_input)
        if Type == "int":
            if int(Func_input) >= Urange or int(Func_input) <= Lrange:
                raise ValueError
        if Type == "float":
            
            if Urange == False:
                pass
            elif float(Func_input) > Urange or float(Func_input) < Lrange:
                raise ValueError              
        if Type == "char":
            if len(Func_input)!=1:
                raise ValueError
        return True_False+1, test_type(Func_input)

    except ZeroDivisionError:
        print("Try again, you cannot divide by 0")
        return True_False,Func_input
    except ValueError:
        print(f"Please input a {Type} and in the right range")
        return True_False,Func_input
#NOTE: this WIL NOT raise a error, only return a value of 0 if the input is invalid,
#  1 wil be returned if the input is valid.

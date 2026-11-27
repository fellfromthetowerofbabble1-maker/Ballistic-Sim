def Error_Test(Type,Func_input, Lrange,Urange):
    True_False=0
    conver={
        "int": int,
        "str": str,
        "char": str,
        "float": float
    }
    
    
    
    if (
        None in (Func_input,Type)
        or Type not in conver
        or "" in (Func_input,Type)
       ):
        raise Exception("the type  has to in the conver setion of the code")
    test_type = conver.get(Type, str) 
    try:
        #Test type is str int or float. char is a str but with a length of 1.
        Func_input=test_type(Func_input)
        limit= len(Func_input) if Type in ( "str" , "char") else Func_input

        if Urange is not None and Urange<limit:
            print(f"\n{Func_input} is over the range of {Urange}")
        elif Lrange in not None and Lrange>limit:
            print(f"\n{Func_input} is under the range of {Lrange}")
            raise ValueError
                          
        if Type == "char":
            if len(Func_input)!=1:
                
                raise ValueError
        
        return True_False+1, test_type(Func_input)

#    except ZeroDivisionError:
#        print("Try again, you cannot divide by 0")
 #       return True_False,Func_input
        
    except ValueError:
        print(f"\nPlease input a {Type} and in the right range\n")
        return True_False,Func_input
#NOTE: this will NOT raise a error, only return a value of 0 if the input is invalid,
#  1 will be returned if the input is valid.

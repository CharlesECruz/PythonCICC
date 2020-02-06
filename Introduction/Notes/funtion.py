def mrange(start,end,steps=1):
    """
    Return a list of integers from start
    :param start:
    :param end:
    :param steps:
    :return:
    """
    result = []
    while start < end:
        result.append(start)
        start+=steps
    print(result)

    pass

def xrange(*args): #*args means that I could receive more than one parameter
    if len(args)==1:
        return mrange(0,args[0])
    elif len(args)==2:
        return mrange(args[0],args[1])
    elif len(args)==3:
        print("this are the parameter that I receive:",args)
        return mrange(*args)# *args means that I give like parameter all the args that I receive
    else:
        raise TypeError("Invalid numbers of parameters dumb") #raise a Error by yourself like try catch in java


xrange(1,1,1,1,1,1,1,1)
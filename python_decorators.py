def outer_function(f):
    def wrapper(*args,**kwargs):
        res = f(*args,**kwargs)
        if isinstance(res, dict):
            print("Checked that the output is a dictionary")
            return res
    return wrapper

@outer_function
def give_dict(arg):
    return{"program": arg}

print(give_dict("python"))
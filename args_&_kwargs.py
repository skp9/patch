def show_numbers(**kwargs):
    for i,j in enumerate(kwargs):
        print(i,j)


show_numbers(zero=1,one=2,two=3)
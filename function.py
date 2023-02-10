def your_name(name:str)->int:
    return name

your = your_name('kevin')
print(type(your))
print(your)

iam = your_name(22)
print(type(iam))
print(iam)

we = your_name(33.3)
print(type(we))
print(we)

# -> str just tells the function to return a string(but it doesn't force the function to return a string)
#this is called return annotation
#so in this case the name will be expected to be a string but also can be an integer


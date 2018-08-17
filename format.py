#Format methods

name = "Hello"
age = 20


#type1

detail = "My name is {0} My age is {1}" .format(name,age)
print(detail)

#type2

detail = "My name is {} My age is {}" .format(name,age)
print(detail)

#type3

print("You are trying {info} and Testing the {meth} method".format(info="python" , meth = "Format"))


# three digits allowed after point in .3f



print("{0:.3f}".format(1.0/3))


#here in below example from 0-5 it will scan Hello word, then after that from 6th position 1 ( _ ) 
# will be inserted after Hello then at 7th position another( _ ) will be inserted before Hello and then so on.


print("{0:_^11}".format("Hello"))

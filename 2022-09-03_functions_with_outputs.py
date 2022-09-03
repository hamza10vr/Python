#Functions with outputs
#capatalize the first letter of each word

def format_name(f_name ="", l_name = ""):
    if f_name =="" or l_name == "":
        return "You didn't provide valid inputs."
        
    first_name = f_name.title()
    last_name = l_name.title()
    full_name = first_name + " " + last_name
    return full_name

name = format_name("hamZa", "tANveeR")
print(name)

name = format_name( "tANveeR")
print(name)
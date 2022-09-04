#Functions with outputs
#capatalize the first letter of each word
# adding docstring for documentation

def format_name(f_name ="", l_name = ""):
    """Take a first and last name and format it to return the title case version of the name."""

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

format_name()
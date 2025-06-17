newString = "We are the so-called 'Ram' from the north."
print(newString)

# escape "Ram" from the below string
# newString = "We are the so-called "Ram from the north." -> errored string
newString = "We are the so-called \"Ram from the north." # -> used escape character to avoid string error
print(newString)

# escape character new line and tab
print(newString + "\n" + newString)
print(newString +"\t" + newString)

# Escape Characters 
# https://www.w3schools.com/python/python_strings_escape.asp
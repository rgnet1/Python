


# input: string 1, string 2
# output: determines if stirngs are equal in case insensative way
def stringCompare(str1, str2):
    
    if str1.lower() == str2.lower():
        return True
    return False


print(stringCompare("a", "A"))
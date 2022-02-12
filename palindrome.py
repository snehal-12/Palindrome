from audioop import reverse


def is_palindrome(input_string):
    # create two strings to compare them
    new_string=""
    reverse_string=""

    #Traverse through each letter of the input string
    for letter in input_string:
        #Add any non-blank letters to the end of new string 
        # and to the front of reverse string
        if(letter!=" "):
            new_string=new_string+letter
            reverse_string=letter+reverse_string

    #Compare to see if the two strings are same
    if(new_string.lower()==reverse_string.lower()):
        return True
    else:
        return False

print(is_palindrome("Never Odd or Even"))
print(is_palindrome("abcd"))
print(is_palindrome("kayak"))
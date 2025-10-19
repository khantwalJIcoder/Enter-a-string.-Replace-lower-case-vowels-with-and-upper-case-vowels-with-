'''Q1)Enter a string. Replace lower case vowels with ‘#’ and upper case vowels with ‘@’. Display the new string after change.'''
s = input("Enter a string: ")
new_s = ""
for ch in s:
    if ch in 'aeiou':         
        new_s += '#'
    elif ch in 'AEIOU':       
        new_s += '@'
    else:
        new_s += ch           
print(new_s)

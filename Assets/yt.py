# take user input(string)
#if the length of string is greter than 3
#add "ing" as a suffix in the original string 
#else print the same string given by user


s=str(input())
if len(s)>3:
    print(s+"ing")
else:
    print(s)
age=26
agestring="I am {} years old"
print(agestring.format(age))



a=5
b=4
c=3
st="a={},b={},c={}"
print(st.format(a,b,c))

#place holders
#replacing values according to the index no. written after the format comment
b=5
c=15
d=20
s="a={2},b={0},c={3},d={1}"
print(s.format(c,d,b,a))
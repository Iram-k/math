sal=int(input("Enter your salary : "))
time=int(input("Enter the time spent in the company : "))
if time>=10:
    ts=sal+((10/100)*sal)
    print ("Your net bonus amount is=",ts)
elif time>=6 and time<10:
    ts=sal+((8/100)*sal)
    print ("Your net bonus amount is=",ts)
elif time<6 :
    ts=sal+((5/100)*sal)
    print ("Your net bonus amount is=",ts)
else:
    print ("You receive no bonus amount, your salary is=",sal)

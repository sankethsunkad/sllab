conversions=set([])
amendd=[]
def c_f(temp):
    final=(temp*1.8)+32
    return final
def f_c(temp):
    final=(temp-32)*(5/9)
    return final
while('true'):
    print("1.Celsius to fahrenheit")
    print("2.fahrenheit to celsius")
    print("3.to print the convrsions value")
    print("press 0 to terminate")
    op = int(input("Enter the option"))
    if(op==1):
        tem=int(input("enter the temprature in celsius scale"))
        f_tem=c_f(tem)
        a=["celsius",tem,"to","fahrenheit",f_tem]
        amendd=list(conversions)
        amendd.append(a)
        conversions=tuple(amendd)
        print("Temperature in fahrenheit scale is",f_tem)
    elif(op==2):
        tem = int(input("enter the temprature in fahrenheit scale"))
        f_tem = f_c(tem)
        a = ["fahrenheit", tem, "to", "celsius", f_tem]
        amendd = list(conversions)
        amendd.append(a)
        conversions = tuple(amendd)
        print("Temperature in celsius scale is", f_tem)
    elif(op==3):
        print(conversions)
    elif(op==0):
        exit()
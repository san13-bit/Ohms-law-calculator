def ohmlaw():
     print("program to find the unknown electrical value when the given other two known using Ohm's law")
     c=int(input("MENU:\n->1=Find current value\n->2=Find voltage\n->3=Find resistance\nEnter your choice:"))
     if c==1:
         v1=float(input("Enter  the value of voltage in Volts "))
         r1=float(input("Enter the value of resistance in ohms"))
         print("The value of current is=",v1/r1,"ampere")
     elif c==2:
         i2=float(input("Enter the value of current in ampere"))
         r2=float(input("Enter the value of resistance in ohms"))
         print("The value of voltage is=",i2*r2,"volts")
     elif c==3:
         i3=float(input("Enter the value of current in ampere"))
         v3=float(input("Enter the value of voltage in volts"))
         print("The value of resistance=",v3/i3,"ohms")
     else:
         print("!Enter a valid choice!")
ohmlaw()     

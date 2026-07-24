def calc_resistanceband():
    print("To decode the resitance value using the colour bands")
    colour_values={"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"gray":8,"white":9}
    print("Enter the colours of the bands from left to right:")
    b1=input("Enter colour of first band :").strip().lower()
    b2=input("Enter colour of second band :").strip().lower()
    b3=input("Enter colour of third band :").strip().lower()
    digit1=colour_values.get(b1)
    digit2=colour_values.get(b2)
    digit3=colour_values.get(b3)
    base_value=(digit1*10)+digit2
    res_value=base_value*(10**digit3)
    print("The resistance of the resistor is",res_value,"ohms")
calc_resistanceband()   

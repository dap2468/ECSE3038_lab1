def parallel(r):

    size=len(r)

    if (size>=2):
        RT=0.0
        for x in r:
            RT=(1/x)+RT

        RT=1/RT
        print("%.3f"%RT,"ohms")
    else:
        print ("not enough resistors")

parallel([1000,330,2200])




def potential_divider(v,r):
    sum=0

    for x in r :
        sum+=x
    
    for y in r:
        v_specific = (y/sum)*v
        print ("%.2f"%v_specific,"v")

potential_divider(9,[3000,1000])


def temperature_check(temp,unit):
    if(unit=='C'):
        if (temp<36):
            print("the patient is hypothermic")
        elif (temp>37):
            print("the patient is hyperthermic")
        else:
            print("the patient's temperature is normal")

    if(unit=='F'):
        if (temp<(36*(9/5))):
            print("the patient is hypothermic")
        elif (temp>(36*(9/5))):
            print("the patient is hyperthermic")
        else:
            print("the patient's temperature is normal")       

temperature_check(14,"C")
temperature_check(100, "C")
temperature_check(37, "F")

1.  parallel() when called, outputs the outputs the effective resistance of a network of 2 or more resistors connected in parallel.
Eg. parallel([330, 1000, 2200])
    "222.973 ohms"

2.  potential_divider(), that takes two values as argument, a number that represents a voltage supply value and a list of numbers that represent resistance values of resistors connected in series. The function outputs the voltage drop across each resistor in your resistor list.
Eg. potential_divider(9, [3000, 1000])
    "6.75v"
    "2.25v"

3. temperature_check() accepts a single number, a patient's body temperature, and a single character, the unit of temperature. The function outputs whether the patient is hypothermic, hyperthermic or has normal body temperature based on the number passed to the function. 
    
    The second value passed as argument should tell the function whether the condition should calculated in degrees celcius or degrees fahrenheit.
Eg. temperature_check(14, "C")
    "the patient is hypothermic"

    temperature_check(37, "C")
    "the patient's temperature is normal"

    temperature_check(37, "F")
    "the patient is hypothermic"


CODE WAS WRITTEN FOR LAB1


Why did the two Java methods get a divorce?
    Because they had constant arguments.
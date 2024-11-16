print("""
=========Build Your EV=========
Please select the EV model (Sedan, SUV): x
Invalid model
Please select the EV model (Sedan, SUV): sedan
Please select the wheel drive type (Front, Rear, All): front
Please select the color (White, Blue, Red): blue
Do you want the leasing option? ([Y], [N]): y
Please enter the leasing months between 1 and 9: x
Invalid number
Please enter the leasing months: 9

Press 'Return' to see the order summary


=========Order Summary========
Model:      SEDAN
Wheel Drive FRONT
Color:      BLUE

Payment:    Leasing
Months:     9
Monthly Payment:   $ 367.50
Monthly Tax:       $  22.97
-------------------------------
Total:      $ 3,514.22

Month   MonthlyPmt  MonthlyTax  TotalPmt  Balance
1       $ 367.50    $ 22.97     $ 390.47  $3,123.75
2       $ 367.50    $ 22.97     $ 780.94  $2,733.28
3       $ 367.50    $ 22.97     $1,171.41 $2,342.81
4       $ 367.50    $ 22.97     $1,561.88 $1,952.34
5       $ 367.50    $ 22.97     $1,952.34 $1,561.88
6       $ 367.50    $ 22.97     $2,342.81 $1,171.41
7       $ 367.50    $ 22.97     $2,733.28 $  780.94
8       $ 367.50    $ 22.97     $3,123.75 $  390.47
9       $ 367.50    $ 22.97     $3,514.22 $    0.00
""")

print("""
=========Build Your EV=========
Please select the EV model (Sedan, SUV): suv
Do you want to add the tow hitch? ([Y], [N]): y
Please select the wheel drive type (Front, Rear, All): all
Please select the color (White, Blue, Red): red
Do you want the leasing option? ([Y], [N]): y
Please enter the leasing months between 1 and 9: 9

Press 'Return' to see the order summary


=========Order Summary========
Model:      SUV
Wheel Drive ALL
Color:      RED

*Added the Tow Hitch

Payment:    Leasing
Months:     9
Monthly Payment:   $ 585.00
Monthly Tax:       $  36.56
-------------------------------
Total:      $ 5,594.06

Month   MonthlyPmt  MonthlyTax  TotalPmt  Balance
1       $ 585.00    $ 36.56     $ 621.56  $4,972.50
2       $ 585.00    $ 36.56     $1,243.12 $4,350.94
3       $ 585.00    $ 36.56     $1,864.69 $3,729.38
4       $ 585.00    $ 36.56     $2,486.25 $3,107.81
5       $ 585.00    $ 36.56     $3,107.81 $2,486.25
6       $ 585.00    $ 36.56     $3,729.38 $1,864.69
7       $ 585.00    $ 36.56     $4,350.94 $1,243.12
8       $ 585.00    $ 36.56     $4,972.50 $  621.56
9       $ 585.00    $ 36.56     $5,594.06 $    0.00
""")

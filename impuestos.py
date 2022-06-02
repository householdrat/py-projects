income = float(input("Introduce el ingreso anual:"))

if income < 85528:
    IPI = (18 * income)/100  
    tax = IPI - 556.2
    
if  income > 85528:
    excedente = income - 85528
    IPI = (excedente * 32) / 100
    tax = IPI +14839.2

else:
    income <= 0
    tax = 0.0

    

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

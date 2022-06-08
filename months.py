def is_year_leap(year):
	if year % 4 != 0: #Si no es divisible en 4 es común
		return False
	elif year % 100 !=0: #Si no es divisible en 100 es bisiesto
		return True
	elif year % 400 != 0: # si no es divisible en 400 es común
		return False
	else:
		return True 

def days_in_month(year, month):
    daysMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        if daysMonth[month -1] == 28:
            return 29
        else:
            return daysMonth[month -1]
    else:
        return daysMonth[month -1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
    
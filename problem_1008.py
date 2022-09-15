employee_number = int(input(''))
worked_hours = int(input(''))
received_per_hour = float(input(''))
salary = received_per_hour * worked_hours
print('NUMBER = {}\nSALARY = U$ {:.2f}'.format(employee_number,salary))
# def multiply_x2(input):
  #  total = input * 2
   # return total


#number = int(input ("write a number "))
#total_calculated = multiply_x2(number)
# print(total_calculated)
# ---------------------------------------------------------

def get_pay_with_more_info(num_hours, hourly_wage, tax_bracket):
    pay_pretax = num_hours * hourly_wage
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax

weekly = get_pay_with_more_info(40, 15, 0.12)
print(f'${int(weekly)}')

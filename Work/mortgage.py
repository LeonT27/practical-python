# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month_payment = payment;
    if total_month >= extra_payment_start_month and total_month <= extra_payment_end_month:
        month_payment = payment + extra_payment;

    if (principal * (1+rate/12)) < month_payment:
        month_payment = principal * (1+rate/12)
        
    total_paid = total_paid + (month_payment)
    principal = principal * (1+rate/12) - (month_payment)
    total_month = total_month + 1

    print(total_month, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid,2), 'Total Month', total_month)
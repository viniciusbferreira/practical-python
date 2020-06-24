# extra_payments.py
#
# Exercise 1.8
principal = 500000.0
rate = 0.05
total_paid = 0.0
months = 0

while principal > 0:
    if months < 12:
        payment = 2684.11 + 1000
        principal = principal * (1 + rate/12) - (payment)
        months += 1
        total_paid += payment
    else:
        payment = 2684.11
        principal = principal * (1 + rate/12) - (payment)
        months += 1
        total_paid += payment
    
print('Total paid', total_paid)
print('Total months', months)
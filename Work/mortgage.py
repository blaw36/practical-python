# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
total_mths = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

# while principal > 0:
#     if total_mths >= (extra_payment_start_month - 1) and total_mths < (extra_payment_end_month):
#         principal = principal * (1+rate/12) - (payment + extra_payment)
#         total_paid = total_paid + (payment + extra_payment)
#     else:
#         principal = principal * (1+rate/12) - payment
#         total_paid = total_paid + payment
#     total_mths += 1
#     print(f'{total_mths} {round(total_paid,2)} {round(principal,2)}')

while principal > 0:
    if total_mths >= (extra_payment_start_month - 1) and total_mths < (extra_payment_end_month):
        if payment + extra_payment > principal * (1+rate/12):
            total_paid = total_paid + principal * (1+rate/12)
            principal = 0
        else:
            total_paid = total_paid + (payment + extra_payment)
            principal = principal * (1+rate/12) - (payment + extra_payment)
    else:
        if payment > principal * (1+rate/12):
            total_paid = total_paid + principal * (1+rate/12)
            principal = 0
        else:
            total_paid = total_paid + payment
            principal = principal * (1+rate/12) - payment
    total_mths += 1
    print(f'{total_mths} {round(total_paid,2)} {round(principal,2)}')


# print('Total paid', total_paid)
# print('Total months', total_mths)
print(f'Total paid:\t {total_paid}')
print(f'Total months:\t {total_mths}')

# bool("False") yields True, because bool(str) = True except for bool("") (ie. the empty string), which yields False.
# This is the only string (?) which yields False when converted to boolean.
# Therefore, bool("False") yields True.
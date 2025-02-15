def calculate_bill(units):   
    if units <= 199:
        charge_per_unit = 1.20
    elif 200 >= units < 400:
        charge_per_unit = 1.50
    elif 400 >= units < 600:
        charge_per_unit = 1.80
    else:
        charge_per_unit = 2.00
    total_bill = units * charge_per_unit
    if total_bill > 400:
        surcharge = total_bill * 0.15
        total_bill += surcharge
    else:
        surcharge = 0
    if total_bill < 100:
        total_bill = 100
    return charge_per_unit, total_bill, surcharge
customer_id = input("Enter The Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))
charge_per_unit, total_amount, surcharge = calculate_bill(units_consumed)
print("Electricity Bill")
print(f"Customer ID       : {customer_id}")
print(f"Customer Name     : {customer_name}")
print(f"Units Consumed    : {units_consumed}")
print(f"Charge per Unit   : Ksh {charge_per_unit:.2f}")
print(f"Surcharge Applied : Ksh {surcharge:.2f}")
print(f"Total Amount to Pay: Ksh {total_amount:.2f}")
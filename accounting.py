def accounting(customer_name, amount, paid):
    melon_cost = 1.00
    customer_expected = amount * melon_cost
    
    if customer_expected != paid:
        print(f"{customer_name} paid ${paid},",
          f"expected ${customer_expected}"
          )
accounting("Joe", 5,  5.00 )
accounting("Frank", 6,  6.00 )
accounting("Sally", 3, 3.00)
accounting("Sean", 9, 9.50)
accounting("David", 4, 4.00)
accounting("Ashley", 3, 2.00)

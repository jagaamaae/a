def print_payment(path):
  path=open(path)
  for line in path:
    order=line.split("|")
    order_id, customer_name, amount, paid= order
    amount=float(amount)
    paid=float(paid)

    melon_cost = 1.00
    customer_expected = amount * melon_cost
    
    if customer_expected > paid:
      print(f"{customer_name} paid ${paid}, but expected {customer_expected}--underpaid")
    else:
      if customer_expected < paid:
        print(f"{customer_name} paid ${paid}, but expected {customer_expected}--overpaid")

print_payment("customer-orders.txt")

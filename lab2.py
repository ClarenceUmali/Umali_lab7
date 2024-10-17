item_1= float(input (" Enter the price of item #1 :"))
item_2= float(input ("Enter the price of item #2"))
item_3= float(input ("Enter thre price of item #3"))

total_cost = item_1 + item_2 + item_3
discount = 100.00

if total_cost >= discount:
      # Apply discount
      discount_cost = total_cost * 0.1
      total_cost -= discount_cost
      exit
      
      # Compute the loyalty points
      loyalty = 10
      loyalty_points = total_cost // loyalty
      
      #Aplly loyalty points
      total_cost -= loyalty_points
      
      #Input for payment
      payment = float (input("Enter payment"))
      
      if payment >= total_cost:
           print(f"Your change is: {change}")
else:
    print("Payment Failed")
    





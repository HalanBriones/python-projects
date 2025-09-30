'''
    get_retail_function allow enter information about retail purchase this function
    Has no parameters the function ask for description, quantity of items the price per unit and the tax rate
'''
def get_retail_purchase(): #
    description = str(input("Enter retail item description: "))
    quantity = int(float(input("Enter integer quantity item purchased: ")))
    price_unit = float(input("Enter price per unit: "))
    tax_rate = float(input("Enter tax rate with float numbers 'example 6% = 0.06' : "))
    #float_rate = tax_rate/100 #
    return description,quantity,price_unit,tax_rate
'''
    calculate_subtotal multiply the price of the item by the quantity
    has 2 parameters quantity and price
'''
def calculate_subtotal(quantity,price):
    subtotal= price*quantity
    return subtotal
'''
    calculate_tax calculate the amount of tax
    has 2 parameter subtotal and tax
'''
def calculate_tax(subtotal,tax):
    tax_amount = subtotal*tax
    return tax_amount

'''
    calculate_total calculate the addition of subtotal and the tax amount
    has 2 parameters subtotal and tax amount
'''
def calculate_total(subtotal, taxamount):
    total_amount= subtotal+taxamount
    return total_amount
'''
    display_sales_receipt only display a summary of all information plus come calculations 
    has 7 parameters description, number of units, unit price, tax rate, subtotal, tax amount
    and the total
'''
def display_sales_receipt(description,number_unit,unit_price,tax_rate,subtotal,tax_amount,total):
    print("Item Description: ",description)
    print("Number of Purchased items: ", number_unit)
    print("Unit Price: ", unit_price)
    print("Tax rate: ", tax_rate)
    print("Subtotal: ", subtotal)
    print("Tax: ", tax_amount)
    print("Total: ", total)

def main ():
    description,quantity,price_unit, float_rate =get_retail_purchase()
    subtotal = calculate_subtotal(quantity,price_unit)
    tax_amount = calculate_tax(subtotal,float_rate)
    total_amount = calculate_total(subtotal,tax_amount)
    print("Receipt")
    display_sales_receipt(description,quantity,price_unit,float_rate,subtotal,tax_amount,total_amount)

if __name__=="__main__" :
    main()
'''Importing functions from laboratory number 2'''


#I don't know how define a constant instead I use a global variable
months_year = 12
qualify_salary = 50000.0
'''Function define if you qualify for a loan having in mind years being employed and your anual salary'''
def qualifies_for_loan():
    month_salary = float(input("Please insert your monthly salary in CAD: "))
    years_employed = int(input("Please insert numbers of years employed: "))

    annual_salary = month_salary*months_year #Annual salary calculation

    if years_employed<3: #first I filter if they have more than 3 years employed
        print("You must be employed at least for 3 years or more, you don't qualify for a loan")
    else:
        if annual_salary>=qualify_salary:
            print("You qualify for a loan")
        else:
            print("Your income must be $50000 CAD or more, you don't qualify for a loan ")

#global variables of the plan details
minutes_plan = 50
messages_plan = 50
tax_rate = 0.05
'''Funtion that calculate your phone bill, have 2 parameters air time in minutes also amount of text messages'''
def calculate_monthly_cell_phone_bill_charge_cad(air_time,text_messages):
    if (air_time or text_messages) < 0:
        print("Invalid minutes or messages amount, try again")
        return
    else:
        base_charge_month = 15.0 #charge per month for 50 messages and 50 minutes
        additional_minute = 0.25 #additional charge each minute
        additional_message = 0.15 # additional charge each message
        additional_charge = 0.44 #911 calls charge
        if air_time>minutes_plan: #extra minutes
            total_extra_minutes = air_time-minutes_plan
            additional_charge_minutes=total_extra_minutes*additional_minute
        else:
            additional_charge_minutes=0 #No charge if no more than 50 minutes

        if text_messages>messages_plan: #extra messages
            total_extra_messages = text_messages-messages_plan
            additional_charge_messages=total_extra_messages*additional_message
        else:
            additional_charge_messages=0 #No charge if no more than 50 messages

        #Total charge in order to calculate the tax
        bill = base_charge_month+additional_charge_minutes+additional_charge_messages+additional_charge
        tax_charge = bill*tax_rate
        total_charge = bill+tax_charge

        print("Base charge is: ",base_charge_month)
        if additional_charge_minutes != 0: #Making sure to don't show if the charge is 0
            print("Additional minutes charge is: ", additional_charge_minutes)

        if additional_charge_messages != 0: #Making sure to don't show if the charge is 0
            print("Additional text messages charge is: ", additional_charge_messages)

        print("911 service fee", additional_charge)
        print("Tax amount is: ", tax_charge)
        print("Total charge is: ", total_charge)

def main():
    #qualifies_for_loan()
    print("----------------------------------------")
    calculate_monthly_cell_phone_bill_charge_cad(-1,-1)
if __name__ == "__main__":
    main()


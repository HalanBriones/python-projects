def get_car_csv_info():
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    year= input("Enter car year: ")
    milage = input("Enter car milage: ")
    price = float(input("Enter car price in float numbers: "))

    # save values in a list also get rid of spaces
    # join all the values into a string with no spaces
    final_make = make.split(" ")
    join_make = "".join(final_make)

    final_model = model.split(" ")
    join_model = "".join(final_model)

    final_year = year.split(" ")
    join_year = "".join(final_year)

    final_milage = milage.split(" ")
    join_milage = "".join(final_milage)

    #I wasn't able to do a split on price because transform into a list I cannot cut decimals if is a list

    #mix of f string and also formating in order to just show two decimals in price
    final_strg = f"{join_make.title()},{join_model.title()},{join_year},{join_milage},%.2f" %price
    return final_strg
def to_json_format(csv_format):
    data = csv_format.split(",") #transform from csv to a list and assigning the corresponding values
    make=data[0]
    model=data[1]
    year = data[2]
    milage = data[3]
    price = data[4]
    #creation of the JSON without formating or f string
    json = '{ "make": '+make+' , '+'"model" : '+model+' , '+'"year" : '+year+' , '+'"milage" : '+milage+' , '+'"price" : '+price+' }'
    return json

def main():
    csv_format = get_car_csv_info()
    print("The CSV car data is: ",csv_format)
    json_format = to_json_format(csv_format)
    print("The JSON car data is: ",json_format)

if __name__ == "__main__":
    main()
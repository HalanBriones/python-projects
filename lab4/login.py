def generate_login(first_name, last_name, bcit_id):
    #Making sure that first letter of first and last name are Uppercase
    if len(first_name)<3: #save full name if the length is small than 3
        final_fname= first_name.capitalize()
    else:
        final_fname=first_name[:3].capitalize()

    if len(last_name)<3: #save full last name if the length is small than 3
        final_lname= last_name.capitalize()
    else:
        final_lname=last_name[:3].capitalize()

    if len(bcit_id)<3: #save full id number if the length is small than 3
        final_id=bcit_id
    else:
        final_id= bcit_id[-3:]
    id_student = f"{final_fname}{final_lname}{final_id}"
    return id_student

def get_password():
    while True:
        password = input("Enter your password: ")
        if len(password)<7 or len(password)>30: #Conditioning the amount of characters
            print("Password needs to be minimun 7 and maximum 30 characters")
            continue
        else:
            if "password" in password: #conditioning the word password in the string
                print("Password cannot contain the word 'password'")
                continue
            elif " " in password: #conditioning spaces in the string
                print("Password cannot contain spaces")
                continue

            ##saving the last 3 characters of the password and return it
            last_char_pass=password[-3:]
            return last_char_pass


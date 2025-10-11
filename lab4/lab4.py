import login, sys

def main():
    # call the function with the parameters from the console
    id_student = login.generate_login(sys.argv[1], sys.argv[2], sys.argv[3])
    print(f"Your login ID is {id_student}")

    #we call the function get password
    print(f"Your initial password ends with {login.get_password()}")

if __name__ == "__main__":
    main()

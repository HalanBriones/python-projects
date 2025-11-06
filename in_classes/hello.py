def welcome_message():
    print("Hello welcome message")

def test_code():
    print("Hello test code")

def main():
    welcome_message()
    test_code()

#main()
#print("from hello.py __name__is:",__name__)
if(__name__ == "__main__"): #flag to do not run in case we are using this as a module because I wont be in the main
    main()
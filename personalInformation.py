while True:
    #declare empty dictionary
    personalInfo = {
    }
    #display menu
    print ("========== Menu ==========")
    print ("")
    print ("1. Add an Item")
    print ("2. Search")
    print ("3. Exit Y/N")
    print ("")
    print ("==========================")
    print ("")
    #ask user input
    personalData = int(input("What do you want to do? (1-3) "))
    print ("")

    #if user input 1: ask personal data
    if personalData == 1:
        print ("========== Answer the requested information correctly ==========")
        print ("")
        name = input("Your Name: ")
        cellphoneNo = int(input("Your Cellphone Number: "))
        eMail = input("Your Email Address: ")
        birthday = input("Your Birthday: ")
        print ("Your information saved successfully!")
        print ("")
        print ("================================================================")
        print ("")
        
    #if user input 2: ask full name
        userdata = {
            'name': name,
            'cellphoneNo': cellphoneNo,
            'eMail': eMail,
            'birthday': birthday
        }
        personalInfo [name] = userdata
        
    if personalData == 2:
        search = input("Enter your name: ")
        print ("")
        print ("========== Printing user information ==========")
        print ("")
        if search in personalInfo:
            print ("Your Name:", + personalInfo [search]['name'])
            print ("Your Cellphone Number:", +personalInfo [search]['cellphoneNo'])
            print ("Your Email Address:", +personalInfo [eMail]['eMail'])
            print ("Your Birthday:", +personalInfo [birthday]['birthday'])
            print ("")
            print ("===============================================")
        
    #if user input 3: ask if want to exit
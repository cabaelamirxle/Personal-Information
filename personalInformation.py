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
    personalInfo [name] = {}
    personalInfo [name]['Name'] = name
    personalInfo [name]['Mobile Number'] = cellphoneNo
    personalInfo [name]['Email'] = eMail
    personalInfo [name]['Birthday'] = birthday
    print ("Information Saved Successfully!")
    print ("")
    print ("================================================================")
    
#if user input 2: ask full name
#if user input 3: ask if want to exit
from urllib.request import urlopen, hashlib

sha1hash = input("Please input the hash to crack.\n>")
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

# guess from the list of passwords we opened, and split it by line

for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):

#checking if the password is in the list so we can compare it to the hash the user gave us

    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()

# compare the hash the user gave us to the hashed version of the password guess and determine if they are equal

    if hashedGuess == sha1hash:

#Sixth, we'll tell the program what to do if the password guess matches, which is to print the current guess and quit the program.
#We'll also tell the program what to do if the password guess don't match, which is to return to step 3 to get a new password from the list

        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, trying next...")

#In the seventh and final step, we'll tell the program what to do if we get all the way through the password list without finding a match.
print("Password not in database, we'll get them next time.")
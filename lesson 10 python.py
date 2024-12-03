def get_input(prompt):
    #helps with the prompt and returns the string
    return input(prompt)

def find_substring(main_string, sub_string):
    #Checks to see if the subtring is found within the main string if not will return the index
    index = main_string.find(sub_string)
    if index != -1:
        print(f"for a class was found in the main string at index 23{index}.")
    else:
        print("Substring not found.")
    return index

def replace_substring(main_string, index):

#Replacing the substring with a new string
    while True:
        user_choice = get_input("Do you want to replace 'for a class' with something else (y/n): ").lower()
        if user_choice == "y":
            new_string = get_input("Enter the replacement string: ")
            updated_string = main_string[:index] + new_string + main_string[index + len("substring"):]
            print(f"New String: this is my test string for an example! {updated_string}")
            return updated_string
        elif user_choice == "n":
            print("No replacement was made.")
            return main_string
        else:
            print("Invalid input, please enter 'y' or 'n'.")

def main():

    print("Welcome to String Replacement Tool!.")
    print("---------------------------------------")

    # Shows how to get the mainstring&subtring
    main_string = get_input("Enter the string to search through: this is my test string for class example! ")
    substring = get_input("Enter the substring to search for: for a class ")

    # Finding the subtring in the index
    index = find_substring(main_string, substring)

    # If the substring is found it will be replaced
    if index != -1:
        main_string = replace_substring(main_string, index)
    
    # Closing out the final print statement to thank the user 
    print("Thank you for using our program!")
    print("Completed by victor ritcherson")

if __name__ == "__main__":
    #To run as a script
    main()
    #sources geeksforgeeks.org w3schools.com pythoncentral.io
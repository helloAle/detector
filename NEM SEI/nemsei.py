def check_name(name):
    # Convert the name to lowercase for case-insensitive comparison
    lowercase_name = name.lower()
    
    # Check if the name matches any of the specified variations
    if lowercase_name == "kaique" or lowercase_name == "ike" or lowercase_name == "maiku" or lowercase_name == "kaiq":
        print("I love you")

# Receive names from the user until they input "exit"
while True:
    name = input("Enter a name (type 'exit' to quit): ")
    
    if name.lower() == "exit":
        break
    
    check_name(name)

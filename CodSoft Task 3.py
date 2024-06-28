def get_password_length():
    length = 0
    while length <= 0:
        user_input = input("Enter the desired length of the password: ")
        if user_input.isdigit():
            length = int(user_input)
            if length <= 0:
                print("Please enter a positive number.")
        else:
            print("Please enter a valid number.")

    return length

def simple_random(initial_value):
    a = 1103515245
    c = 12345
    m = 2**31
    initial_value = (a * initial_value + c) % m
    return initial_value

def generate_password(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?/~`'
    characters = letters + digits + punctuation

    
    initial_value = sum(ord(c) for c in "password")  
    password = ''
    for _ in range(length):
        initial_value = simple_random(initial_value)
        index = initial_value % len(characters)
        password += characters[index]

    return password

length = get_password_length()


password = generate_password(length)


print("Generated password:", password)

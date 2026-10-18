import random
import string

def get_password_criteria():
    """Prompt the user for password preferences and validation."""
    print("--- Secure Password Generator ---")
    
    # Get desired length
    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters for security.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Get character type preferences
    print("\nSelect character sets to include:")
    use_upper = input("Include uppercase letters (A-Z)? (y/n): ").strip().lower() == 'y'
    use_lower = input("Include lowercase letters (a-z)? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include special symbols (!@#$%^&*...)? (y/n): ").strip().lower() == 'y'

    # Ensure at least one character set is selected
    if not (use_upper or use_lower or use_digits or use_symbols):
        print("\n[!] Error: You must select at least one character set! Defaulting to lowercase letters.")
        use_lower = True

    return length, use_upper, use_lower, use_digits, use_symbols

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password based on the specified criteria."""
    char_pool = ""
    mandatory_chars = []

    # Build the character pool and guarantee at least one character from each selected set
    if use_upper:
        char_pool += string.ascii_uppercase
        mandatory_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        mandatory_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        mandatory_chars.append(random.choice(string.digits))
    if use_symbols:
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        char_pool += special_chars
        mandatory_chars.append(random.choice(special_chars))

    # If requested length is shorter than mandatory characters, adjust length
    if length < len(mandatory_chars):
        length = len(mandatory_chars)

    # Fill the rest of the password length with random choices from the full pool
    remaining_length = length - len(mandatory_chars)
    password_chars = mandatory_chars + [random.choice(char_pool) for _ in range(remaining_length)]

    # Shuffle the resulting list to ensure randomness in positions
    random.shuffle(password_chars)
    
    return "".join(password_chars)

def evaluate_strength(password, use_upper, use_lower, use_digits, use_symbols):
    """Provide a simple strength evaluation of the generated password."""
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if use_upper and use_lower:
        score += 1
    if use_digits:
        score += 1
    if use_symbols:
        score += 1

    if score >= 5:
        return "Strong "
    elif score >= 3:
        return "Moderate "
    else:
        return "Weak "

def main():
    while True:
        length, use_upper, use_lower, use_digits, use_symbols = get_password_criteria()
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        strength = evaluate_strength(password, use_upper, use_lower, use_digits, use_symbols)

        print("\n" + "="*40)
        print(f"Generated Password: {password}")
        print(f"Password Strength:  {strength}")
        print(f"Length:             {len(password)} characters")
        print("="*40)

        choice = input("\nWould you like to generate another password? (y/n): ").strip().lower()
        if choice != 'y':
            print("\nStay secure! Goodbye.")
            break

if __name__ == "__main__":
    main()      

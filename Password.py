
import random
import string
import hashlib


def generate_password(length=12, use_special_chars=True, use_uppercase=True, use_lowercase=True, use_digits=True):
    """
    Generate a random password based on the specified criteria.

    :param length: Length of the generated password (default is 12).
    :param use_special_chars: Include special characters (default is True).
    :param use_uppercase: Include uppercase letters (default is True).
    :param use_lowercase: Include lowercase letters (default is True).
    :param use_digits: Include digits (default is True).
    :return: The generated password as a string.
    """
    # Define character pools
    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected!")

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def save_password(password, filename="passwords.txt"):
    """
    Save the password and its hashed version to a file.

    :param password: The password to be saved.
    :param filename: The file to which the password will be saved (default is 'passwords.txt').
    """
    try:
        # Encrypt the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with open(filename, "a") as file:
            file.write(f"{password} : {hashed_password}\n")
        print(f"Password saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving the password: {e}")


def evaluate_password_strength(password):
    """
    Evaluate the strength of the given password.

    :param password: The password to be evaluated.
    :return: The strength of the password ('Weak', 'Moderate', or 'Strong').
    """
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digits:
        score += 1
    if has_special:
        score += 1

    if score < 3:
        return "Weak"
    elif score < 5:
        return "Moderate"
    else:
        return "Strong"


# Example usage
if name == "__main__":
    password = generate_password(length=16, use_special_chars=True,
                                 use_uppercase=True, use_lowercase=True, use_digits=True)
    print(f"Generated Password: {password}")

    strength = evaluate_password_strength(password)
    print(f"Password Strength: {strength}")

    save_password(password)

Password Generator

Description

This project is a Python script that generates secure passwords, evaluates their strength, and saves them to a file. The script allows you to customize the generated password based on criteria such as length, inclusion of special characters, uppercase letters, lowercase letters, and digits. It also provides a mechanism to evaluate the strength of the password and saves both the password and its hashed version to a file.

Features

 • Generate Passwords: Create random passwords with customizable length and character types.
 • Evaluate Password Strength: Determine if the generated password is ‘Weak’, ‘Moderate’, or ‘Strong’.
 • Save Passwords: Save the generated password and its hashed version to a file.

Installation

 1. Clone the repository:

git clone https://github.com/your-username/password-generator.git


 2. Navigate to the project directory:

cd password-generator



Usage

To generate a password and save it, run the script as follows:

python password_generator.py

You can customize the password generation parameters directly in the script:

 • length: Length of the generated password (default is 12).
 • use_special_chars: Include special characters (default is True).
 • use_uppercase: Include uppercase letters (default is True).
 • use_lowercase: Include lowercase letters (default is True).
 • use_digits: Include digits (default is True).

Example

password = generate_password(length=16, use_special_chars=True, use_uppercase=True, use_lowercase=True, use_digits=True)
print(f"Generated Password: {password}")

strength = evaluate_password_strength(password)
print(f"Password Strength: {strength}")

save_password(password)

Contributing

 1. Fork the repository.
 2. Create a new branch:

git checkout -b feature-branch


 3. Commit your changes:

git commit -am 'Add new feature'


 4. Push to the branch:

git push origin feature-branch


 5. Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

For any questions or suggestions, please contact me at
yousefsayed3119@gmail.com

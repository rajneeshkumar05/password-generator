import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    # Character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure strong password (at least one from each)
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    all_chars = upper + lower + digits + special

    # Fill remaining characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle password
    random.shuffle(password)

    return ''.join(password)


# ---- Main Program ----
print("🔐 Password Generator 🔐")

length = int(input("Enter password length: "))
result = generate_password(length)

print("Generated Password:", result)

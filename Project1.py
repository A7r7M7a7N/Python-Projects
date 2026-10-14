# Password Generator and Strength Checker
import random
import string
import re

def generate_password(length=16, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    score = 0
    if len(password) >= 12: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"\d", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1

    ratings = {1: "Very Weak", 2: "Weak", 3: "Medium", 4: "Strong", 5: "Very Strong"}
    return ratings.get(score, "Very Weak")
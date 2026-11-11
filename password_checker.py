
import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    print("\n===== PASSWORD SECURITY REPORT =====")
    print("Password length:", len(password))
    print("Security score:", score, "/ 5")

    if score <= 2:
        print("Password Strength: WEAK")
        print("Recommendation: Use a stronger password.")

    elif score <= 4:
        print("Password Strength: MEDIUM")
        print("Recommendation: Improve your password.")

    else:
        print("Password Strength: STRONG")
        print("Your password meets all five checks.")

    print("====================================")


print("====================================")
print("       PASSWORD STRENGTH CHECKER")
print("====================================")

password = input("Enter your password: ")

check_password_strength(password)

input("\nPress ENTER to exit...")

import string
password=input("Enter a password:")
has_upper=any(ch.isupper()for ch in password)
has_lower=any(ch.islower()for ch in password)
has_digit=any(ch.isdigit()for ch in password)
has_special=any(ch in string.punctuation for ch in password)
if len(password)<8:
        print("Weak:must be atleast 8 characters")
elif not has_upper:
        print("Weak:must contain atleast 1 uppercase letter")
elif not has_lower:
        print("Weak:must contain atleast 1 lowercase letter")
elif not has_digit:
        print("Weak:must contain atleast 1 number")
elif not has_special:
        print("Weak:must contain atleast 1 special character(!,@,#,$...)")
else:
        print("Strong password")

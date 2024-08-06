import re
password = "Example@123"  
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
is_valid = bool(re.match(pattern, password))
print(f"Password is valid: {is_valid}")

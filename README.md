# 🔐 Password Strength Checker & Generator

A Python script that checks the strength of a user-provided password and suggests a secure one if the password is weak. It evaluates common security criteria and uses the `getpass` module to hide input for privacy.

---

## ✅ Features

- Hides password input using `getpass` for secure entry  
- Evaluates password based on:
  - Length (minimum 8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Presence of digits
  - Presence of special characters
- Generates a strong random password if the entered one is weak  
- Provides clear feedback on what is missing in the password  

---

## 🧠 Concepts Covered

- `getpass.getpass()` for hidden input  
- String validation using `any()` and `string` module  
- Random password generation with `random.choice()`  
- Use of list comprehensions and conditionals  

---

## 🔧 How It Works

1. User is prompted to enter a password securely.
2. The password is checked against several criteria.
3. If the password is strong:
   ```
   Strong password! you are good to go
   ```
4. If the password is weak:
   - Issues are listed (e.g., "Missing uppercase letter")
   - A strong password is suggested

---

## 💡 Example

```
Enter a password: 
You got weak password
- Too short (minimum 8 characters)
- Missing special character

 Suggesting you a strong password
gA8#W@1pZx$q
```

---

## 🛠 How to Run

1. Save the script as `password_checker.py`.
2. In terminal or command prompt, run:
   ```bash
   python password_checker.py
   ```
3. Enter your password when prompted (it won't show as you type).

---

## 🔒 Tip

Never use suggested passwords directly — modify them slightly to keep them unique and secure.

---


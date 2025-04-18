# Email Validation Program

This Python script checks whether a user-provided email address is valid based on a series of custom validation rules.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Validation Rules](#validation-rules)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Sample Output](#sample-output)
- [Limitations](#limitations)
- [License](#license)

---

## 🔍 Overview
This script prompts the user to enter an email address and then performs several checks to determine whether the email is valid according to a specific set of rules. If the email passes all checks, a confirmation message is displayed.

---

## ✅ Validation Rules
The email is considered valid only if it meets the following conditions:

1. Must be at least 6 characters long.
2. First character must be an alphabet.
3. Must contain exactly one `@` symbol.
4. Must contain either `.com` or `.in` at the end.
5. Should not contain any spaces.
6. Should not contain uppercase letters.
7. Only the following special characters are allowed: `_`, `.`, `@`

---

## ⚙️ How It Works
The script performs step-by-step checks using conditional statements and loops. It tracks three flags:

- `k`: Set if space is found.
- `j`: Set if an uppercase alphabet is found.
- `d`: Set if any disallowed special character is found.

If any of these flags are raised, the email is considered invalid.

---

## ▶️ Usage
Run the Python script and enter your email when prompted:

```bash
python email_validator.py
```

Example:
```
 Enter your Email : swapnilbilgoji@gmail.com
 YOUR__EMAIL__IS__CORRECT 

 THANK__YOU__FOR__ENTERING__YOUR__EMAIL
```

---

## 💡 Sample Output

### ✅ Valid Email:
```
 Enter your Email : test_email@g.com
 YOUR__EMAIL__IS__CORRECT 

 THANK__YOU__FOR__ENTERING__YOUR__EMAIL
```

### ❌ Invalid Email:
```
 Enter your Email : 9email@gmail.com
First letter of the email should be alphabet
```

---

## ⚠️ Limitations
- This is a basic validator and may not cover all edge cases as per RFC 5322 (email standard).
- Does not support emails with subdomains (e.g., name@mail.co.in).
- No GUI, CLI-based only.

---

## 📝 License

This project is licensed under the MIT License.



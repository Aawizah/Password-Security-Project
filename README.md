# Password-Security-Project (Beginner)

⚠️ **WARNING: This repository contains intentionally vulnerable code (for educational purposes only).**  
- Do **NOT** deploy the `weak-login` app to any public server.  
- Do **NOT** use the brute-force script against any real website or system you do not own.  
- This project is for **local learning and demonstration only**.  

---

## 📖 About
This beginner-friendly project demonstrates:
- Why storing passwords in plain text (or with weak hashes) is insecure.
- How a simple brute-force script can guess weak passwords quickly.
- How secure password storage using bcrypt mitigates brute-force attacks.

You will build and test:
- `weak-login/` → a deliberately insecure login system.
- `secure-login/` → a corrected login system using bcrypt.
- `brute-force/` → a Python script that attempts to brute-force the weak system.
- `report/` → short write-up with findings and recommendations.

---

## 🛠️ Tools Used
- Python 3, Flask
- SQLite
- Flask-Bcrypt
- Requests (for brute-force script)

---

## 🚀 How to Run (Locally)
1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/Password-Security-Project.git
   cd Password-Security-Project

# 🔐 Brute Force Simulation Tool (Python GUI)

A Python-based graphical user interface tool that simulates brute-force login attacks.  
Designed for **educational and penetration testing awareness purposes**, this tool allows users to test multiple password attempts against a specified login endpoint.

---

## 🖥️ Features

- ✅ Modern `Tkinter`-based GUI
- ✅ Input fields for target URL, username, wordlist, and error message
- ✅ Real-time logging with color-coded console
- ✅ Threaded execution (no freezing)
- ✅ Status bar with dynamic updates
- ✅ File picker for password wordlist
- ✅ Success pop-up when valid credentials are found

---

## 📸 GUI Preview

<img width="1365" height="728" alt="bruteforce" src="https://github.com/user-attachments/assets/0f759782-0ab6-46a6-97cd-6372d6207bce" />


---

## 🚀 How to Run

### 1. ✅ Clone the Repo

```bash
git clone https://github.com/Nitinsingh7643/Brute-Force-Simulation-Tool.git
cd Brute-Force-Simulation-Tool
2. ✅ Install Required Packages
bash
Copy
Edit
pip install requests
3. ✅ Run the GUI Tool
bash
Copy
Edit
python brute_force_gui.py
🧪 Sample Inputs
Field	Example
Target URL	https://httpbin.org/post (demo endpoint)
Username	admin
Password File	passwords.txt (must exist in project dir)
Error Message	invalid or login failed

📝 passwords.txt
Copy
Edit
123456
admin123
testpass
letmein
securepass
⚠️ Disclaimer
This tool is built strictly for educational purposes and ethical demonstrations.
Do not use it on systems or endpoints you do not own or have explicit permission to test.

🙌 Author
Nitin Singh
GitHub: @Nitinsingh7643

📌 To Do / Future Improvements
⏳ Add multi-threaded password distribution

🌐 Integrate proxy or delay options

📊 Add login success/failure statistics

🖥 Export logs to .txt or .csv

🐍 Convert to .exe using pyinstaller for easy sharing

⭐️ If you found this helpful
Consider starring ⭐ the repository to support the project!

yaml
Copy
Edit

---

### ✅ Next Steps for You:

1. Create a file called `README.md` in your root project folder
2. Paste the content above
3. Run:

```bash
git add README.md
git commit -m "Add custom project README"
git push

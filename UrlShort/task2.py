
import tkinter as tk
from tkinter import messagebox
import pyshorteners

# Function to shorten the URL
def shorten_url():
    long_url = url_entry.get()
    if long_url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(long_url)
            result_label.config(text=short_url)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL. {str(e)}")
    else:
        messagebox.showwarning("Input Required", "Please enter a URL to shorten.")

# Function to copy the shortened URL to clipboard
def copy_to_clipboard():
    short_url = result_label.cget("text")
    if short_url:
        root.clipboard_clear()
        root.clipboard_append(short_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard.")
    else:
        messagebox.showwarning("No URL", "There is no shortened URL to copy.")

# Create the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")

# URL input label and entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Shorten button
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

# Label to display the shortened URL
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()

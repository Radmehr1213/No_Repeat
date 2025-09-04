import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def file_hash(path):
    #return files
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def remove_duplicates(folder_path):
    #delete duplicate files
    hashes = {}
    deleted_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            h = file_hash(file_path)

            if h in hashes:
                os.remove(file_path)
                deleted_files.append(file_path)
            else:
                hashes[h] = file_path

    return deleted_files

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path_var.set(folder)

def start_removing():
    folder = folder_path_var.get()
    if not folder:
        messagebox.showwarning("warning", "select a folder!")
        return

    deleted_files = remove_duplicates(folder)
    messagebox.showinfo("result", f"files deleted: {len(deleted_files)}")

# GUI
root = tk.Tk()
root.title("delete duplicate files")
root.geometry("500x150")

folder_path_var = tk.StringVar()

tk.Label(root, text="path to folder:").pack(pady=10)
tk.Entry(root, textvariable=folder_path_var, width=50).pack(pady=5)
tk.Button(root, text="select folder", command=select_folder).pack(pady=5)
tk.Button(root, text="delete duplicate files", command=start_removing, bg="red", fg="white").pack(pady=10)

root.mainloop()

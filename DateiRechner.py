import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title("Datei Rechner")
root.geometry("250x350")
root.resizable(width=False, height=False)
root.configure(bg="#c1edf7")

# Fenster zentrieren
window_width = 250
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Frame für die Eingabe
frame1 = tk.Frame (root, bg="#33c7e8")
frame1.pack(padx=20, pady=20, anchor="nw")

# Frame für Umrechnungsbutton
frame2 = tk.Frame (root, bg="#33c7e8")
frame2.pack(padx=20, pady=10, anchor="center")

# Frame für Result
frame3 = tk.Frame (root, bg="#33c7e8")
frame3.pack(padx=20,pady=20, anchor="w")


# help button
def on_click():
    return messagebox.showinfo(title="Info", message="Geben Sie die Datenmenge ein!\n"
                                                     "Bis zu 15 Zeichen.", icon=messagebox.INFO)

help_button = tk.Button(text="❓", command=on_click, font=("Arial", 14))
help_button.place(relx=1, x=-20, y=20, anchor="ne")


# Eingabeblock
label = tk.Label(frame1,text = "Eingabe:", bg="#33c7e8", font=("Arial", 10))
label.pack(anchor="w")

# prüft und begrenzt die eingegebenen Symbole
def validate_input(P):
    if len(P) > 15:
        messagebox.showinfo("Info", "Sie können maximal 15 Ziffern eingeben.")
        return False
    return P.isdigit() or P == ""

vcmd = (root.register(validate_input), '%P')
entry = tk.Entry(frame1, width=25, validate="key", validatecommand=vcmd)
entry.pack(pady=5, padx = 5)


# Combobox für Einheitenauswahl
unit_label = tk.Label(frame1, text="Einheit:", bg="#33c7e8", font=("Arial", 10))
unit_label.pack(anchor="w")

units = ['Bytes', 'KB', 'MB', 'GB', 'TB']
unit_combobox = ttk.Combobox(frame1, values=units, state="readonly", width=22)
unit_combobox.set('Bytes')
unit_combobox.pack(pady=5, padx=5)


# konvertiert Bytes in GB und GiB
def convert_datei():
    try:
        value = float(entry.get())
        unit = unit_combobox.get()

        # Umrechnung in Bytes
        if unit == 'KB':
            bytes_val = value * 1_000
        elif unit == 'MB':
            bytes_val = value * 1_000_000
        elif unit == 'GB':
            bytes_val = value * 1_000_000_000
        elif unit == 'TB':
            bytes_val = value * 1_000_000_000_000
        else:  # Bytes
            bytes_val = value

        gb = bytes_val / 1_000_000_000
        gib = bytes_val / (1024 ** 3)
        result_label.config(text=f"{value} {unit} sind:\n"
                                 f"{gb:.6f} GB\n"
                                 f"{gib:.6f} GiB")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie eine gültige Zahl ein.")


# Umrechnen Button
calculate_button = tk.Button(frame2, text="Umrechnen", command=convert_datei, font=("Arial", 14))
calculate_button.pack(pady=5, padx = 5)

# Ausgabeblock
result_label_text = tk.Label(frame3,text = "Result:", bg="#33c7e8", font=("Arial", 10))
result_label_text.pack(anchor="w")
result_label = tk.Label(frame3, width=50, height=4, bg="white", text="", justify=tk.LEFT)
result_label.pack(pady=5, padx = 5)

root.mainloop()
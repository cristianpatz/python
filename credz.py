import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os
import uuid


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a CSV file", filetypes=[("CSV Files", "*.csv")])
    return file_path


def select_output_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder to save the output")
    return folder_path


def process_csv(file_path):
    if not file_path:
        return None

    try:
        credz = pd.read_csv(file_path, sep=";", encoding='ISO-8859-1')
        credz['VALOR PRESENTE'] = credz['VALOR PRESENTE'].str.replace(',', '.', regex=True).astype(float)
        soma = credz['VALOR PRESENTE'].sum()
        return soma
    except Exception as e:
        return str(e)


def save_sum_to_txt(soma, folder_path):
    if isinstance(soma, (int, float)):
        unique_filename = f"sum_of_valor_presente_{uuid.uuid4()}.txt"
        output_file = os.path.join(folder_path, unique_filename)
        with open(output_file, 'w') as f:
            f.write(f"Sum of 'VALOR PRESENTE': {soma}\n")
        return output_file
    return None


def main():
    file_path = select_file()

    if not file_path:
        print("No file selected. Exiting.")
        return

    result = process_csv(file_path)

    if isinstance(result, (int, float)):
        print("Sum of 'VALOR PRESENTE':", result)

        output_folder = select_output_folder()

        if output_folder:
            output_file = save_sum_to_txt(result, output_folder)
            if output_file:
                print(f"Sum saved to {output_file}")
            else:
                print("No data to save.")
        else:
            print("No output folder selected.")
    else:
        print("Error:", result)


if __name__ == "__main__":
    main()

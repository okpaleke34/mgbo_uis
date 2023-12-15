import PyPDF2
import os
import os
from dotenv import load_dotenv
import platform


# Load variables from .env file
load_dotenv()


PROG_DIR = ""
if platform.system() == "Windows":
    PROG_DIR = os.environ.get('WINDOWS_PROG_DIR')
elif platform.system() == "Linux":
    PROG_DIR = os.environ.get('UNIX_PROG_DIR')
elif platform.system() == "Darwin":
    PROG_DIR = os.environ.get('MAC_PROG_DIR')

def get_all_files(folder_path):
    # List to store the names of all files in the folder
    all_files = []

    # Iterate through all items in the folder
    for item in os.listdir(folder_path):
        item_path = f"{folder_path}/{item}"
        # item_path = os.path.join(folder_path, item)

        # Check if the item is a file
        if os.path.isfile(item_path):
            # all_files.append(item_path)
            all_files.append(item)

    return all_files

def pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                txt_file.write(page.extract_text())



PROG_DIR = f"{PROG_DIR}/documents/slides"
input_path = f"{PROG_DIR}/pdf"
output_path = f"{PROG_DIR}/txt"
if __name__ == "__main__":
   
    files_in_folder = get_all_files(input_path)

    # Print the list of files
    print("Files in the folder:")
    for filename in files_in_folder:
        base_name = filename.split('.')[0]
        print(filename)
        pdf_to_text(f"{input_path}/{filename}", f"{output_path}/{base_name}.txt")
        


        
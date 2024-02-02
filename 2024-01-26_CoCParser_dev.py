
# Import necessary libraries
import os  # For interacting with the operating system (file paths, etc.)
import re  # For regular expression operations (text matching patterns)
import fitz  # For working with PDF files
import shutil  # For file operations like copying and moving
import logging  # For logging information and errors
import traceback  # For capturing error tracebacks

from PIL import Image  # For working with images
from pyzbar.pyzbar import decode  # For decoding barcodes

# Print a message to console to indicate processing has started
print("Processing Certificate of Conformance Parser.......")


# Set up logging for tracking progress and errors
log = logging.getLogger(__name__)  # Get a logger object
log_directory = r"C:\Users\hamzat\Desktop\CoCParser-Project\dev\logs\mylogs.log"
logging.basicConfig(
    filename=log_directory,  # Specify the log file path
    format="%(asctime)s | %(filename)s:%(lineno)s | %(levelname)s | %(message)s",  # Set the format for log messages
    level=logging.DEBUG  # Set the logging level to DEBUG (captures detailed information)
)

# Log a header for the processing report
log.info(f"\n====================================================================="
         f"\n######     Certificate of Conformance Documment Processor      ######"  
         f"\n=====================================================================")

###### For Testing in local environment ######
# source_folder = r'C:\Users\hamzat\Desktop\Project1-RenameFiles\ScannedFiles'
# destination_folder = r'C:\Users\hamzat\Desktop\Project1-RenameFiles\RenamedFiles'

###### For DEV / DEMO Testing on ICT-SERVER ######

##### for PROD environment #########
source_folder =r"C:\Users\hamzat\Desktop\CoCParser-Project\dev\ScannedFiles"
destination_folder = r"C:\Users\hamzat\Desktop\CoCParser-Project\dev\ParsedFiles" 

def create_jpg_of_first_page(pdf_file, zoom_x, zoom_y):
    """Creates a JPEG image of the first page of the specified PDF file.

    Args:
        pdf_file (str): The path to the PDF file.
        zoom_x (float): The horizontal zoom factor for the JPEG image.
        zoom_y (float): The vertical zoom factor for the JPEG image.

    Returns:
        str: The path to the created JPEG image.
    """

    with fitz.open(pdf_file) as doc:
        # Create a matrix for zooming
        zoom_matrix = fitz.Matrix(zoom_x, zoom_y)

        # Extract the first page
        first_page = doc.load_page(0)

        # Create a JPEG image of the first page with the specified zoom
        pix = first_page.get_pixmap(matrix=zoom_matrix)
        image_name = f"{doc.name}_page1.jpg"
        pix.save(image_name)

    return image_name

def extract_transaction_number_from_image(image_name):
    """Extracts the transaction number from the specified image using a barcode decoder.

    Args:
        image_name (str): The path to the image file.

    Returns:
        str: The extracted transaction number, or an empty string if no barcode is found.
    """

    try:
        # Open the image and decode barcodes
        with Image.open(image_name) as img:
            decoded_data = decode(img)  # `decode` is a barcode decoding function

        # Extract transaction number from the first decoded barcode
        if decoded_data:
            transaction_number = re.findall(r'\d+', str(decoded_data[0].data))[0]
            if len(transaction_number) != 10:
                return "" # invalid barcode
            else:
                return transaction_number
        else:
            return ""  # No barcode found

    finally:
        # Remove the image file
        os.remove(image_name)

def find_transaction_number(filename):
    """
    Attempts to extract the transaction number from the first page of the PDF.
    Iterates through multiple zoom levels to try to locate the number.

    Args:
        filename (str): The name of the PDF file.

    Returns:
        tuple: (transaction_number, attempts)
            transaction_number (str or None): The extracted transaction number if found, otherwise None.
            attempts (int): The number of zoom levels attempted.
    """

    zoom_levels = [(4, 4), (5, 7), (7, 9), (6, 8), (4, 6), (2, 2), (8, 6), (2, 4)]
    attempts = 0  # Initialize a counter for zoom attempts

    for zoom_x, zoom_y in zoom_levels:
        attempts += 1  # Increment the counter for each attempt
        image_name = create_jpg_of_first_page(filename, zoom_x, zoom_y)
        transaction_number = extract_transaction_number_from_image(image_name)
        if transaction_number:
            return transaction_number, attempts

    return None, attempts  # Return None for both values if not found

def rename_file(old_filename, new_filename, destination_folder):
    """
    Renames a file, handling potential errors, checking for existence in the destination folder,
    and applying a duplicate naming convention if needed.

    Args:
        old_filename (str): The current filename.
        new_filename (str): The desired new filename.
        destination_folder (str): The path to the destination folder.
    """
    duplicate_counter = 1
    # Iterate until a unique filename is found:
    while True:
        destination_path = os.path.join(destination_folder, new_filename)
        renamed_filename = new_filename
        if not os.path.exists(destination_path):
            break  # Unique filename found

        # Apply duplicate naming convention:
        base, extension = os.path.splitext(new_filename)  # Split filename into base and extension
        new_filename = f"{base}-copy{duplicate_counter}{extension}"  # Add counter to filename
        duplicate_counter += 1

    # Copy, rename, and remove the original file:
    try:
        shutil.copy2(old_filename, destination_path)  # Copy the file to the destination
        os.remove(old_filename)  # Remove the original file
        
    except FileExistsError:
        log.critical(f"Unexpected error: {new_filename} already exists after duplicate checking")
    except Exception as e:
        log.critical(f"Error copying {old_filename}: {e}")
    
    return renamed_filename

#########################################
# Main processing logic
#########################################
try:
    
    # Set working directory
    os.chdir(source_folder)

    # Log a header for the processing of available Certificates of Conformance
    log.info(f"====================================================")
    log.info(f"Processing Available C of C ........        ")
    log.info(f"====================================================")

    error_files, processed_files = 0, 0

    # Grab all PDFs from the source folder
    pdfs = [filename for filename in os.listdir(source_folder) if filename.endswith(".pdf")]

    # Loop through each filename in the list
    for filename in pdfs:

        processed_files += 1

        transaction_number, attempts = find_transaction_number(filename)

        # If a transaction number was found:
        if transaction_number:
            new_filename = f"{transaction_number}.pdf"
            new_filename = rename_file(filename, new_filename, destination_folder)
            log.info(f"Renamed {filename} to {new_filename} after {attempts} attempt(s)")

        else:
            error_files += 1
            new_filename = filename
            new_filename = rename_file(filename, new_filename, destination_folder)
            log.warning(f"Unable to extract transaction number from {filename} after {attempts} attempts")
                
    log.info(f"====================================================")
    log.info(f"Processed files: {processed_files}")
    log.info(f"Barcode failure: {error_files}")
    log.info(f"====================================================\n")

except Exception as e:
    traceback_str = traceback.format_exc()
    log.error("Traceback:\n%s", traceback_str)

#command for EXE compilation
# pyinstaller  --add-binary="C:\Users\project1-venv\Lib\site-packages\pyzbar:pyzbar" CoCParser.py -F --onefile
    

#######  requirements.txt ###########
# altgraph==0.17.4
# packaging==23.2
# pefile==2023.2.7
# pillow==10.2.0
# pyinstaller==6.3.0
# pyinstaller-hooks-contrib==2024.0
# PyMuPDF==1.23.15
# PyMuPDFb==1.23.9
# pywin32-ctypes==0.2.2
# pyzbar==0.1.9

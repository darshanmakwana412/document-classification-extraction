import os
import easyocr

# Initialize the OCR reader with English as the language and set gpu to False
reader = easyocr.Reader(['en'], gpu=False)

# Define a function named 'extract' that takes in two parameters, docs_pth and data_pth
def extract(docs_pth, data_pth="data"):
    # If the data_pth directory does not exist, create it
    if not os.path.exists(data_pth):
        os.mkdir(data_pth)

    # Iterate through all subdirectories in the docs_pth directory
    for doc in next(os.walk(docs_pth))[1]:
        # Create the full path for the current subdirectory
        doc_pth = os.path.join(docs_pth, doc)
        # Create the full path for the corresponding data subdirectory
        data_doc_pth = os.path.join(data_pth, doc)
        # If the data subdirectory does not exist, create it
        if not os.path.exists(data_doc_pth):
            os.mkdir(data_doc_pth)
        # Get the list of all files in the current subdirectory
        doc_files = os.listdir(doc_pth)

        # Iterate through all files in the current subdirectory
        for doc_file in doc_files:
            # If the file is an image or pdf file (based on file extension)
            if doc_file.lower().endswith(('.png', '.pdf', '.jpg', '.jpeg')):
                # Read the text from the file using the OCR reader
                data = reader.readtext(os.path.join(doc_pth, doc_file))
                # Open a file with the same name as the image/pdf file but with the extension removed
                with open(os.path.join(data_doc_pth, doc_file.rsplit('.', maxsplit=1)[0]), "w") as f:
                    # Write the extracted text to the file, with each line separated by a newline character
                    for text in data:
                        f.writelines([text[1], "\n"])
                # Close the file
                f.close()
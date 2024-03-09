# JPG to PDF Converter

## Introduction

JPG to PDF Converter is a simple tool based on Streamlit and PyMuPDF, designed to help users convert JPG images to PDF files. This tool supports custom page sizes, orientations, alignments, and allows multiple images to be placed on a single PDF page.

A live demo is available at [jpg2pdf.wingetgui.com](https://jpg2pdf.wingetgui.com/).

## Features

- Supports multiple image formats, including JPG, JPEG, and PNG.
- Customizable page size (A4, A3) and orientation (portrait, landscape).
- Options for center or top alignment of images within the PDF page.
- Ability to include multiple images on a single PDF page.
- Customizable page margins.
- Downloadable PDF directly from the webpage.

## Usage

1. Visit [jpg2pdf.wingetgui.com](https://jpg2pdf.wingetgui.com/) or the application deployed locally.
2. Upload the images you want to convert by clicking the "Choose Images" button. You can select multiple images at once.
3. Choose the desired page size and orientation.
4. Select how you want the images aligned within the PDF page.
5. If you chose "top" alignment, you can check "Multiple images on one page?" to include multiple images in a single PDF page.
6. If necessary, check "Set page margins?" to customize the page margins.
7. Click the "Generate PDF" button to create the PDF.
8. Click the "Download PDF" button to download your generated PDF file.

## Local Deployment

To deploy this Streamlit application locally, ensure you have Python and the necessary libraries installed. Follow these steps to install and start:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Enter the project directory and install dependencies:

   ```
   cd your-repo-name
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```
   streamlit run app.py
   ```

4. Visit `http://localhost:8501` in your browser to view the application.

## Contributing

We welcome any form of contributions, whether it be improvements to the code, documentation, or issues. Please fork the project first, create a new branch, make your changes, and then submit a Pull Request to the main repository.



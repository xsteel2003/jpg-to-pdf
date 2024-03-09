import streamlit as st
from PIL import Image
import os
from reportlab.lib.pagesizes import A4, A3, landscape, portrait
import io
#import PyPDF2
from reportlab.pdfgen import canvas
import time
import random
from reportlab.lib.units import cm
import fitz  # PyMuPDF

def images_to_pdf_v13_with_PyMuPDF(image_paths, output_filename, page_size, orientation, alignment, multiple_images, 
                                   margin_horizontal, margin_vertical):
    
    sizes = {
        "A4": (595.28, 841.89),  # dimensions in points
        "A3": (841.89, 1190.55)
    }
    page = sizes.get(page_size)
        
    if orientation == "landscape":
        page = (page[1], page[0])  # swap width and height
    
    pdf = fitz.open()
    current_page = None
    current_y = margin_vertical
    
    for image_path in image_paths:
        img = fitz.open(image_path)
        
        img_width, img_height = img[0].rect.width, img[0].rect.height
        ratio = min((page[0] - 2*margin_horizontal) / img_width, 
                    (page[1] - 2*margin_vertical) / img_height)
        img_width, img_height = img_width * ratio, img_height * ratio

        # If no current_page or the image doesn't fit in the remaining space of the current page, create a new page.
        if not current_page or (multiple_images and current_y + img_height > page[1] - margin_vertical):
            current_page = pdf.new_page(width=page[0], height=page[1])
            current_y = margin_vertical
        
        if alignment == "center":
            x = (page[0] - img_width) / 2
            y = (page[1] - img_height) / 2
        elif alignment == "top":
            x = (page[0] - img_width) / 2
            y = current_y
        
        current_page.insert_image(fitz.Rect(x, y, x + img_width, y + img_height), filename=image_path)
        
        # If multiple images are allowed, update the current_y
        if multiple_images:
            current_y += img_height + 28.34
        else:
            current_page = None  # force to create a new page for the next image
    
    pdf.save(output_filename)
    pdf.close()


def streamlit_ui_v3():
    st.title("Jpg to PDF Converter")

    uploaded_files = st.file_uploader("Choose Images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    page_size = st.selectbox("Select Page Size", ["A4", "A3"])
    orientation = st.selectbox("Select Page Orientation", ["portrait", "landscape"])
    alignment = st.selectbox("Select Alignment", ["center", "top"])
    multiple_images = False
    if alignment == "top":
        multiple_images = st.checkbox("Multiple images on one page?")

    set_margin = st.checkbox("Set page margins?",value=True)
    if set_margin:
        margin_horizontal = st.number_input("Set left-right margin (cm)", min_value=0.0, max_value=4.0, value=1.0, step=0.1) * 28.34
        margin_vertical = st.number_input("Set top-bottom margin (cm)", min_value=0.0, max_value=4.0, value=1.0, step=0.1) * 28.34
    else:
        margin_horizontal, margin_vertical = 0, 0

    if uploaded_files and st.button("Generate PDF"):
        image_paths = []
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            img_path = f"temp_{uploaded_file.name}"
            img.save(img_path)
            image_paths.append(img_path)

        output_filename = f"pdftemp/output_{time.time()}_{random.randint(1000, 9999)}.pdf"
        images_to_pdf_v13_with_PyMuPDF(image_paths, output_filename, page_size, orientation, alignment, multiple_images, 
                        margin_horizontal, margin_vertical)

        for path in image_paths:
            os.remove(path)

        with open(output_filename, "rb") as f:
            pdf_data = f.read()
        st.download_button(label="Download PDF", data=pdf_data, file_name="output.pdf", mime="application/pdf", type='primary')



streamlit_ui_v3()

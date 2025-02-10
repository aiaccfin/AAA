import os

async def save_pdf(oUploadFile):
    pdf_folder = os.path.abspath("./tmp/pdf")
    pdf_name = f"{pdf_folder}/{oUploadFile.filename}"
    os.makedirs(pdf_folder, exist_ok=True)

    # Save uploaded PDF temporarily
    with open(pdf_name, "wb") as f:
        f.write(await oUploadFile.read())

    return pdf_name, pdf_folder


async def save_img(oUploadFile):
    print(5)
    pdf_folder = os.path.abspath("./tmp/img")
    pdf_name = f"{pdf_folder}/{oUploadFile.filename}"
    os.makedirs(pdf_folder, exist_ok=True)
    print(5)

    # Save uploaded PDF temporarily
    with open(pdf_name, "wb") as f:
        f.write(await oUploadFile.read())

    return pdf_name, pdf_folder
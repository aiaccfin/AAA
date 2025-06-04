import os

async def save_upload_file(oUploadFile):
    upload_folder = os.path.abspath("./tmp/v6")
    upload_name = f"{upload_folder}/{oUploadFile.filename}"
    os.makedirs(upload_folder, exist_ok=True)

    # Save uploaded PDF temporarily
    with open(upload_name, "wb") as f:
        f.write(await oUploadFile.read())

    return upload_name, upload_folder


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
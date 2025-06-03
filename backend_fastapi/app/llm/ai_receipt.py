import openai, dotenv

CFG = dotenv.dotenv_values(".env")
age = 300 # seconds

client = openai.OpenAI(api_key = CFG['OPENAI_API_KEY'])
model = "gpt-4o"


receipt_system_prompt = """
You are an assistant that extracts structured data from receipts provided.
Return a JSON object with the following fields, based on the ReceiptBase schema:

- receipt_date: ISO 8601 date string (e.g., "2025-05-28")
- payer_name: string
- payee_name: string
- vendor_name: string
- coa: string

- subtotal: number
- tax: number
- total: number

- currency: string (e.g., "USD")
- payment_method: string (e.g., "cash", "credit_card", etc.)
- reference: string
- description: string

If a field is not found, return it with a null value.
Do not guess missing information. Only extract data present in the receipt.
Return only valid JSON.
"""



def receipt_ai_txt(lines: list[str]):
    prompt_text = "\n".join(lines)
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": receipt_system_prompt},
            {"role": "user", "content": prompt_text},
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content


def receipt_ai_b64(base64_image):
    response = client.chat.completions.create(
        model=model,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system",  "content": receipt_system_prompt},
            {"role": "user",    "content": [
                    {"type": "text", "text": "extract the data in this receipt and output into JSON "},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}", "detail": "high"}}
                ]
            }
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content


    
import openai, dotenv

CFG = dotenv.dotenv_values(".env")
age = 300 # seconds

client = openai.OpenAI(api_key = CFG['OPENAI_API_KEY'])
model = "gpt-4o"

bs_system_prompt = """You are an expert at extracting structured data from bank statements. 
        Extract the following information from the provided bank statement text:

        1. Summary Information:
        - account_number
        - account_name 
        - bank_name
        - statement_period_start (YYYY-MM-DD)
        - statement_period_end (YYYY-MM-DD)
        - opening_balance
        - closing_balance
        - currency (3-letter code)

        2. Transaction Details (array):
        - date (YYYY-MM-DD)
        - description
        - amount
        - transaction_type (debit/credit)
        - reference (if available)
        - balance_after

        Return the data in JSON format with two top-level keys: "summary" and "transactions".
        Example:
        {
        "summary": {
            "account_number": "123456789",
            "account_name": "John Doe",
            "bank_name": "National Bank",
            "statement_period_start": "2023-01-01",
            "statement_period_end": "2023-01-31",
            "opening_balance": 1000.00,
            "closing_balance": 1500.00,
            "currency": "USD"
        },
        "transactions": [
            {
            "date": "2023-01-05",
            "description": "Grocery Store",
            "amount": 50.00,
            "transaction_type": "debit",
            "balance_after": 950.00
            }
        ]
        }
        """


def bs_ai_txt(lines: list[str]):
    prompt_text = "\n".join(lines)
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": bs_system_prompt},
            {"role": "user", "content": prompt_text},
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content


def bs_ai_b64(base64_image):
    response = client.chat.completions.create(
        model=model,
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system",  "content": bs_system_prompt},
            {"role": "user",    "content": [
                    {"type": "text", "text": "extract the data in this bs and output into JSON "},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}", "detail": "high"}}
                ]
            }
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content


    
def verification_template(code: str) -> tuple[str, str]:
    subject = "Verification Code from xAIBooks"
    body = f"Your verification code is: {code}. Please check Spam folder if you don't see it in your inbox."
    return subject, body

def invoice_reminder_template(vendor: str, invoice_number: str, due_date: str, balance_due: float) -> tuple[str, str]:
    subject = f"Reminder: Invoice #{invoice_number} is Due TODAY!"
    # body = f"""
    # This is a friendly reminder from xAIBooks Automatical Accounting. 
    
    # The Invoice #{invoice_number} is due on {due_date}.
    # <b>The balance</b> due is ${balance_due:.2f}.

    # Please ensure timely payment to avoid penalty. Thank you!
    # """
    body = f"""
      <body style="font-family: Arial, sans-serif; color: #333;">
        <p>Dear Valued Customer,</p>

        <p>This is a friendly reminder from <strong>xAIBooks Automatical Accounting</strong>.</p>

        <table style="border-collapse: collapse; margin: 15px 0;">
          <tr>
            <td style="padding: 8px; font-weight: bold;">Vendor:</td>
            <td style="padding: 8px;">{vendor}</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: bold;">Invoice Number:</td>
            <td style="padding: 8px;">#{invoice_number}</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: bold;">Due Date:</td>
            <td style="padding: 8px;">{due_date}</td>
          </tr>
          <tr>
            <td style="padding: 8px; font-weight: bold;">Balance Due:</td>
            <td style="padding: 8px;">${balance_due:.2f}</td>
          </tr>
        </table>

        <p>Please ensure timely payment to avoid any penalties.</p>
        <p>Thank you!</p>
        
        <p style="margin-top: 30px;">Sincerely,<br>xAIBooks Team</p>
      </body>
    """
    return subject, body

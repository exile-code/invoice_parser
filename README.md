# 🧾 Invoice Parser to Google Sheets (Python Automation Tool)

This tool reads raw invoice data from a `.txt` file, extracts key details like client name, items, pricing, totals, and automatically:
- Saves the structured data to a `.csv` file
- Pushes the invoice to a Google Sheet using `gspread`

---

## 📥 Input Format

Each invoice must follow this structure:
Invoice #001 Client: Acme Corp Date: 2024-04-25 Items: 3x T-shirt @ $10, 2x Jeans @ $50 Total: $130


---

## 🚀 Features

✅ Extracts invoice data  
✅ Supports multiple items  
✅ Calculates totals per item  
✅ Writes to `.csv` and Google Sheet  
✅ Great for automating business processes

---

## 🧠 Tech Used

- Python 3.x  
- `csv` module  
- `gspread` + `oauth2client`  
- Google Sheets API  
- Manual text parsing logic

---

## 📤 Output Example (`invoice_001.csv`)
Invoice,Client,Date,Item,Quantity,Unit Price,Total Item Price 001,Acme Corp,2024-04-25,T-shirt,3,10.0,30.0 001,Acme Corp,2024-04-25,Jeans,2,50.0,100.0


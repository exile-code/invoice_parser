#parse_invoice.py

def parse_invoice(file_path):
    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]
    
    invoice_number = lines[0].replace("Invoice #", "")
    client = lines[1].split(":")[1].strip()
    date = lines[2].split(":")[1].strip()
    raw_items = lines[3].split(":")[1].strip()
    total = float(lines[4].split(":")[1].replace("$","").strip())

    #process items
    items = raw_items.split(", ")
    parsed_items = []

    for item in items:
        quantity_part, rest = item.split("x ")
        name_part, price_part = rest.split(" @ $")
        parsed_items.append({
            "name" : name_part.strip(),
            "quantity" : int(quantity_part.strip()),
            "unit_price" : float(price_part.strip()),
            "total_price" : int(quantity_part.strip())*float(price_part.strip())
        })

    invoice = {
        "invoice_number" : invoice_number,
        "client" : client,
        "date" : date,
        "items" : parsed_items,
        "total" : total
    }

    return invoice

#test run
invoice_data = parse_invoice("invoice_001.txt")
print(invoice_data)


import csv

def write_invoice_to_csv(invoice, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Invoice", "Client", "Date", "Item", "Quantity", "Unit Price", "Total Item Price"])
        
        for item in invoice["items"]:
            writer.writerow([
                invoice["invoice_number"],
                invoice["client"],
                invoice["date"],
                item["name"],
                item["quantity"],
                item["unit_price"],
                item["total_price"]
            ])

write_invoice_to_csv(invoice_data, "invoice_001.csv")
print("✅ Invoice exported to CSV.")


import gspread
from oauth2client.service_account import ServiceAccountCredentials

def push_to_google_sheet(invoice, sheet_name="Invoices"):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    sheet.clear()  # Optional: clear old data

    # Write header
    sheet.append_row(["Invoice", "Client", "Date", "Item", "Quantity", "Unit Price", "Total Item Price"])

    # Write rows
    for item in invoice["items"]:
        sheet.append_row([
            invoice["invoice_number"],
            invoice["client"],
            invoice["date"],
            item["name"],
            item["quantity"],
            item["unit_price"],
            item["total_price"]
        ])

    print("✅ Invoice pushed to Google Sheets!")

push_to_google_sheet(invoice_data)

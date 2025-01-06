# import pandas as pd
# from bs4 import BeautifulSoup

# # Path to the local HTML file
# html_file_path = "/Users/aminjamain/Documents/Phyton-Project/publicholiday-extract/Malaysia Public Holidays 2025.html"

# # Read the HTML file
# with open(html_file_path, "r", encoding="utf-8") as file:
#     soup = BeautifulSoup(file, "html.parser")

# # Extract and print all table information for inspection
# holidays = []
# table = soup.find("table")
# if table:
#     rows = table.find_all("tr")
#     print("Extracted Table Data:")
#     for index, row in enumerate(rows):
#         cols = row.find_all("td")
#         if cols:
#             row_data = [col.text.strip() for col in cols]
#             print(f"Row {index}: {row_data}")
#         if len(cols) == 2:  # Assuming date and holiday name columns
#             date = cols[0].text.strip()
#             holiday_name = cols[1].text.strip()
#             holidays.append({"Date": date, "Holiday": holiday_name})

# # Create a DataFrame and save it to an Excel file
# if holidays:
#     df = pd.DataFrame(holidays)
#     output_path = "/Users/aminjamain/Documents/Phyton-Project/publicholiday-extract/Public_Holidays_2025.xlsx"
#     df.to_excel(output_path, index=True)
#     print(f"\nPublic holidays data has been saved to {output_path}")
# else:
#     print("No public holiday data found in the table.")

import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate  # For better visual display of data

# Path to the local HTML file
html_file_path = "/Users/aminjamain/Documents/Phyton-Project/publicholiday-extract/Malaysia Public Holidays 2025.html"

# Read the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract and print all table information for inspection
holidays = []
table = soup.find("table")
extracted_data = []  # List to store raw extracted rows for display
if table:
    rows = table.find_all("tr")
    for index, row in enumerate(rows):
        cols = row.find_all("td")
        row_data = [col.text.strip() for col in cols]
        if row_data:
            extracted_data.append(row_data)
        if len(cols) == 4:  # Assuming date and holiday name columns
            date = cols[0].text.strip() if len(cols) > 0 else ""
            day = cols[1].text.strip() if len(cols) > 1 else ""
            holiday_name = cols[2].text.strip() if len(cols) > 2 else ""
            state_holiday = cols[3].text.strip() if len(cols) > 3 else ""
            holidays.append({"Date": date,
                             "Day": day,
                             "Holiday": holiday_name,
                             "State Holiday": state_holiday})

# Print extracted table data using tabulate
if extracted_data:
    print("\nExtracted Table Data:")
    print(tabulate(extracted_data, headers=["Date","Day","Holiday","State Holiday"], tablefmt="grid"))
else:
    print("No table data found for inspection.")

#Create a DataFrame and save it to an Excel file
if holidays:
    df = pd.DataFrame(holidays)
    output_path = "Public_Holidays_2025.xlsx"
    df.to_excel(output_path, index=False)
    print(f"\nPublic holidays data has been saved to {output_path}")
else:
    print("\nNo public holiday data found in the table.")

# Create a DataFrame and group by "State Holiday"
# if holidays:
#     df = pd.DataFrame(holidays)
#     output_path = "Public_Holidays_2025.xlsx"

#     with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
#         for state, group in df.groupby("State Holiday"):
#             # Save each group (state) to a separate sheet in the Excel file
#             group.to_excel(writer, index=False, sheet_name=state[:31])  # Sheet names max 31 chars

#     print(f"\nPublic holidays data has been saved to {output_path} with separate sheets based on 'State Holiday'.")
# else:
#     print("\nNo public holiday data found in the table.")
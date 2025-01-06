import pandas as pd
from bs4 import BeautifulSoup

# Path to the local HTML file
html_file_path = "/Users/aminjamain/Documents/Phyton-Project/publicholiday-extract.html"

# Read the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract holiday data from the table
holidays = []
table = soup.find("table")
if table:
    rows = table.find_all("tr")
    for row in rows[1:]:  # Skip header row
        cols = row.find_all("td")
        if len(cols) == 2:
            date = cols[0].text.strip()
            holiday_name = cols[1].text.strip()
            holidays.append({"Date": date, "Holiday": holiday_name})

# Create a DataFrame and save it to an Excel file
if holidays:
    df = pd.DataFrame(holidays)
    output_path = "Public_Holidays_2025.xlsx"
    df.to_excel(output_path, index=False)
    print(f"Public holidays data has been saved to {output_path}")
else:
    print("No public holiday data found in the table.")

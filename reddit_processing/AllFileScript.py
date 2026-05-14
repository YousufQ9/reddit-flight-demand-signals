from to_csv import convertcsv

files = [
    "uktravel_submissions", "travel_submissions","solotravel_submissions",
    "Europetravel_submissions","backpacking_submissions"
]

for filename in files:
    print(f"Processing {filename}...")
    convertcsv(filename)
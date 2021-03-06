import csv

# For counting favorites
counts = {}

# Open CSV file
with open("CS50 2019 - Lecture 7 - Favorite TV Shows (Responses) - Form Responses 1.csv", "r") as file:

    # Create DictReader
    reader = csv.DictReader(file)

    # Iterate over CSV file
    for row in reader:

        # Force title to lowercase
        title = row["title"].lower()

        # Add title to counts
        if title in counts:
            counts[title] += 1
        else:
            counts[title] = 1

# Print counts
for title, count in counts.items():
    print(title, count, sep=" | ")

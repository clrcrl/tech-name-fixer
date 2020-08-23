import csv
import plistlib as plist

SOURCE_FILE = "tech-names.csv"

snippets_array = []

with open(SOURCE_FILE, "rt") as csvfile:
    reader = csv.DictReader(csvfile)
    firstline = True
    for row in reader:
        snippets_array.append(
            {"phrase": row["correct_spelling"], "shortcut": row["common_misspelling"]}
        )

with open("tech-names.plist", "wb") as fp:
    plist.dump(snippets_array, fp)

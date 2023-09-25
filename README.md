# Hanseatic Bank CSV Creator

The credit cards from Hanseatic Bank don't have a CSV export. This is how it works.

Install `pip install pyperclip` and start the program with `python hanseatic-bank-csv-creator.py`.

This script will then wait for changes in the clipboard. Go to the Hanseatic Bank online banking and select a block of statements below one month and copy them to the clipboard. A new CSV file should then be created.

It only supports settled statements for now.

Elegant? Not really.
Stable? Not really.
Does it work? Yes.

import csv
import pyperclip
from datetime import datetime
import os
import sys

clipboard = pyperclip.waitForNewPaste(timeout=None)
txt = clipboard.splitlines()

header = ['Payee','Memo','Date','Outflow']

outpath = sys.argv[1] if len(sys.argv) > 1 else  ""
targetname = datetime.today().strftime('%Y-%m-%d') + "_Hanseatic_Bank.csv"
filename = os.path.join(outpath, targetname)

with open(filename, 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(header)

	for i in range(0, len(txt), 5):
		k = txt[i]
		lines = txt[i+1:i+5]

		if k != "Kartenumsatz" and k != "Lastschrifteinzug":
			print("First line is not Kartenumsatz or Lastschrifteinzug, but "+k)
			exit()

		writer.writerow(lines)


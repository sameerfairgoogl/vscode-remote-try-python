#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------


import pdfplumber
import csv

with pdfplumber.open("test.pdf") as pdf:
    page = pdf.pages[0]
    table = page.extract_table()

    with open("output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(table)

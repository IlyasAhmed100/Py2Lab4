# Task 4.2

with open("dickens.txt") as dickens_txt:
    dickens_data = dickens_txt.read()

with open("dickens_new.txt", "w") as dickens_new_txt:
    no_commas_dickens = dickens_data.replace(",", " ")
    no_fullstop_dickens = no_commas_dickens.replace(".", "")
    new_line_dickens = no_fullstop_dickens.replace("  ", "\n")
    lowercase_dickens = new_line_dickens.lower()
    dickens_new_txt.write(lowercase_dickens)

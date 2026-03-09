import csv

## write into CSV files 
with open("Files.csv", "w", newline="") as files:
    write=csv.writer(files, delimiter=" ", quotechar="|")
    write.writerow(["Nom","Prenom","Sexe","Age"])
    data=[  ["SOUROU","Bel","M","20"],
            ["ASSOGBA","Damilola","M",21],
            ["SOUROU", "Prince, Olawoumi","M",19],
            ["AKAKPO"]
            ]
    write.writerows(data)

 ## read in CSV Print as dictionar 
with open("Files.csv", "r")as Files:
   
    readerD=csv.DictReader(Files, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    for row in readerD:
        print(f"{row.get("Nom","")} {row.get("Prenom","") or "Indefine"}=>{row.get("Sexe") or "Indefine"}, {row.get("Age") or "Indefine"}")


print("_"*64,"\n")

## read in CSVPrint as Table
with open("Files.csv", "r")as Files:
    readerT=csv.reader(Files, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    for row in readerT:
        print(row)

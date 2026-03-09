import csv
class CSVhandle():
    
    def __init__(self , filename):
        self.filename=filename
        self.delimiter=","
        self.quotechar="|"
        self.quoting=csv.QUOTE_MINIMAL

    def write_file(self, data_head, data):
        with open (self.filename, "w" ) as file:
            writer=csv.writer(file , self.delimiter , self.quotechar,self.quoting)
            writer.writerow(data_head)
            writer.writerows(data)
    def read_file(self):
        with open( self.filename, "r")as file:
            reader=csv.reader(file, self, quotechar="|")
            for row in reader:
                print(row)
    def reader_dict(self):
        with open(self.filename, "r")as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{k}=> {v}" for k, v in row.items())
            
             

        

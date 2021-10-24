# unique id(class variable)
# name
# no. persons with him
# date
# orderlist(with number of items included)
# contact no.
# 	*methods- print info

class Customer():
    id =1
    def __init__(self,nme,no,dte,contact,olis=None,b=0):
        self.name=nme
        self.no=no
        self.date=dte
        self.ordrlst=olis
        self.contact=contact
        self.bill = b
        Customer.id += 1
    def __str__(self):
        return (str(self.id)+" "+str(self.name)+"DOB: "+str(self.date)+" "+str(self.ordrlst)+" "+str(self.contact))+" "+str(self.bill)
    def set_ordrlst(self,olis):
        self.ordrlst=olis
    def set_bill(self,b):
        self.bill=b
        
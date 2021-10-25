# unique id(class variable)
# name
# no. persons with him
# date
# orderlist(with number of items included)
# contact no.
# 	*methods- print info
from datetime import date
class Customer():
    id =1
    def __init__(self,nme,nop,contact):
        self.name = nme
        self.n = nop
        self.contactno = contact
        self.Id = Customer.id
        Customer.id += 1
        self.temp = date.today()
        self.date = self.temp.strftime("%B %d, %Y")
    def set_ordrlst(self,ols):
        self.ordrlst=ols
    def set_bill(self,b):
        self.billl=b

    def get_name(self):
        return self.name
    def get_no_persons(self):
        return self.n
    def get_contactno(self):
        return self.contactno
    def get_id(self):
        return self.Id
    def get_contactno(self):
        return self.contactno
    def get_bill(self):
        return self.billl
    def get_date(self):
        return self.date

    def __str__(self):
        return ("Id"+str(self.id)+"\nName:"+str(self.name)+"\nNo. of persons:"+str(self.n)+"\nDOB: "+str(self.date)+"\nItems ordered:"+str(self.ordrlst)+"\nContact details: "+str(self.contactno))+"\nBill: "+str(self.billl)


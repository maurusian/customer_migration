from datetime import datetime #for handling dates


#class that handles customer objects
class Customer():
    def __init__(self,customer_id,update_date,location,update_flag = None):
        self.customer_id = customer_id
        self.update_date = update_date
        self.location = location
        self.update_flag = update_flag

    def update_customer(self,upd_customer):
        #must fill in

        #check dates

        #will only update if the date of the new row is larger than the date from the currect row

        #should customer be updated if the new location is empty?
        #I suppose not, since it's the only meaningful piece of date here, but depends on the specifications


        return self


class CustomerList():
    def __init__(self,customers,system):
        self.customers = customers
        self.system = system

    def get_cust_list_by_id(self,cust_id):
        cust_list = []

        for cust in self.customers:
            if cust.customer_id == cust_id:
                cust_list.append(cust)
        return cust_list

    def delete_cust_from_list(self,customer):
        pass

        #check dates

        #will only delete if the date of the new row is larger than the date from the currect row

    def update_row(self,new_customer):
        #calls update_customer from Customer class
        pass


    #central functionality
    def update_curr_cust_list(self,upd_cust_list):  #upd_cust_list = updated list
        for i in range(len(upd_cust_list.customers)):
            tmp_cust_list = self.get_cust_list_by_id(upd_cust_list[i].customer_id) #querying to get the customer who has the same id
            if len(tmp_cust_list) == 0: #no customer returned
                if upd_cust_list[i].update_flag == 'I': #normal case
                    self.customers.append(upd_cust_list[i])
                else:
                    print('warning') #maybe the cust was already deleted in a previous run, maybe it's something that should be looked into
            elif len(tmp_cust_list) == 1:
                if upd_cust_list[i].update_flag == 'U':
                    self.update_row(upd_cust_list[i])
                elif upd_cust_list[i].update_flag == 'D':
                    #delete
                    self.delete_cust_from_list()
                else:
                    print('warning')
                


if __name__ == '__main__':
    N = int(input()) #number of rows of current customer data

    #get list of customer space-separated data, one customer per row
    customers = []
    for _ in range(N):
        cust_data = input().split()
        #creating the list of Customer objects

    M = int(input()) #number of rows of updated customer data

    #get list of customer space-separated data, one customer per row
    customers = []
    for _ in range(M):
        cust_data = input().split()
        #creating the list of Customer objects

    
        
        

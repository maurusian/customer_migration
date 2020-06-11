from datetime import datetime #for handling dates


#class that handles customer objects
class Customer():
    def __init__(self,customer_id,update_date,location,update_flag = None):
        self.customer_id = customer_id
        self.update_date = datetime.strptime(update_date,'%d.%m.%Y')
        self.location    = location
        self.update_flag = update_flag

    def update_customer(self,upd_customer):
        #must fill in

        #check dates

        #will only update if the date of the new row is larger than the date from the currect row

        #should customer be updated if the new location is empty?
        #I suppose not, since it's the only meaningful piece of data here, but depends on the specifications


        return self


class CustomerList():
    def __init__(self,customers,system):
        self.customers = customers
        self.system = system

    def __contains__(self,cust_id):
        for cust in self.customers:
            if cust.customer_id == cust_id:
                return True
        return False

    def get_cust_by_id(self,cust_id):
        cust_list = [cust for cust in self.customers if cust.customer_id == cust_id]

        """
        for cust in self.customers:
            if cust.customer_id == cust_id:
                cust_list.append(cust)
        """

        if len(cust_list) == 0:
            return None
        elif len(cust_list) == 1:
            return cust_list[0]
        
        #code needs to be tested
        return sorted(cust_lis,key = lambda x:x[i].customers.update_date,reverse = True)[0]

    def clean_customer_list(self):
        """
        removing any superfluous records, i.e.
        duplicate IDs among which only the most
        recent record will be treated anyway).

        In another version, we could also remove
        any empty records (location = NULL).
        """
        cleaned_list = []

        for cust in self.customers:
            if cust_id not in self:
                cleaned_list.append(self.get_cust_by_id(cust.customer_id))

        self.customers = cleaned_list

    def delete_cust_from_list(self,customer):
        pass

        #check dates

        #will only delete if the date of the new row is larger than the date from the currect row

    def update_row(self,new_customer):
        #calls update_customer from Customer class
        pass


    #central functionality
    def update_curr_cust_list(self,upd_cust_list):  #upd_cust_list = updated CustomerList object, self = current CustomerList object

        upd_cust_list.clean_customer_list()
        
        for i in range(len(upd_cust_list.customers)):

            cust = self.get_cust_by_id(upd_cust_list[i].customer_id) #querying to get the customer who has the same id from the current system
            
            if cust is None: #no customer returned
                
                if upd_cust_list[i].update_flag == 'I': #normal case
                    self.customers.append(upd_cust_list[i])

                elif upd_cust_list[i].update_flag == 'D':
                    print('warning')  #maybe the cust was already deleted in a previous run, maybe it's something that should be looked into
                    
                elif upd_cust_list[i].update_flag == 'U':
                    #depending on the expected behavior, this should trigger an exception or just a warning
                    print('Update error: Customer with ID '+str(upd_cust_list[i].customer_id)+' not found in the current instance')
                    
            else:
                
                if upd_cust_list[i].update_flag == 'U':
                    self.update_row(upd_cust_list[i])
                
                elif upd_cust_list[i].update_flag == 'D':
                    #delete
                    self.delete_cust_from_list(cust)
                
                elif upd_cust_list[i].update_flag == 'I':
                    print('Insert warning: customer with ID '+str(cust.customer_id)+' already inserted in the current instance.')

    def purge_customer_list(self):
        """
        Empties list of customers. Will usually
        be used to purge the customer rows from
        the update system.
        """
        pass
                


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

    
        
        

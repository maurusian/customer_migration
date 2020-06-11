from datetime import datetime #for handling dates
import sys

DATE_FORMAT = '%d.%m.%Y'


class Customer():
    """
    Class that handles Customer objects
    """
    def __init__(self,customer_id,update_date,location,update_flag = None):
        self.customer_id = customer_id
        self.update_date = datetime.strptime(update_date,DATE_FORMAT)  #convert to datetime type
        self.location    = location
        self.update_flag = update_flag

    def update(self,upd_customer):
        """
        Updates a customer, by copying the update
        date and the location from the attributes
        of upd_customer.

        The customer_id should normally be the same.

        #should customer be updated if the new location is empty?
        #I suppose not, since it's the only meaningful piece of
        #data here, but depends on the specifications
        """
        self.update_date = upd_customer.update_date
        self.location = upd_customer.location
       

    def copy(self):
        """
        Returns a copy of the calling Customer object
        but without the update_flag
        """
        return Customer(self.customer_id,self.update_date.strftime(DATE_FORMAT),self.location)

    def __repr__(self):
        """
        Returns a string that can be printed when
        calling the built-in function "print" on
        the calling object.
        """
        if self.update_flag is None:
            flag = ''
        else:
            flag = self.update_flag
        
        return str(self.customer_id).ljust(5,' ')+self.update_date.strftime(DATE_FORMAT).ljust(15,' ')+ self.location.ljust(10,' ')+flag


class CustomerList():
    """
    Class that handles tables consisting of Customer records
    """
    def __init__(self,customers,system):
        self.customers = customers
        self.system    = system

    def __contains__(self,cust_id):
        """
        Implements the built-in functionality
        "in" to test if a customer is in the
        customer list or not.

        This functionality was not used in the
        end.
        """
        for cust in self.customers:
            if cust.customer_id == cust_id:
                return True
            
        return False

    def __repr__(self):
        """
        Returns a string that can be printed when
        calling the built-in function "print" on
        the calling object.
        Uses __repr__ from Customer class.
        """
        ss = self.system+'\n'

        if len(self.customers)==0:
            ss+='No customers to show'
        else:
            for cust in self.customers:
                ss+=cust.__repr__()+'\n'

        return ss


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
        return sorted(cust_list,key = lambda x:x.update_date,reverse = True)[0]

    def clean_customer_list(self):
        """
        removing any superfluous records, i.e.
        duplicate IDs among which only the most
        recent record will be treated anyway).

        In another version, we could also remove
        any empty records (location = NULL).
        """
        cleaned_list = []
        added_id = []
        for cust in self.customers:
            if cust.customer_id not in added_id:
                cleaned_list.append(self.get_cust_by_id(cust.customer_id))
                added_id.append(cust.customer_id)
        
        self.customers = cleaned_list

    def insert_customer(self,customer):
        """
        Inserts a customer into the customers
        attribute of the current Customer_List
        object.
        """
        self.customers.append(customer)

    def delete_cust_from_list(self,customer):
        """
        Deletes a customer from the customers
        attribute of the current Customer_List
        object.
        """
        del self.customers[self.customers.index(customer)]

    def update_row(self,upd_customer):
        """
        Updates the customer with the same index
        upd_customer.
        calls update_customer from Customer class.
        """
        for i in range(len(self.customers)):
            if self.customers[i].customer_id == upd_customer.customer_id:
                self.customers[i].update(upd_customer)
                break


    #central functionality
    def update_curr_cust_list(self,upd_cust_list):  #upd_cust_list = updated CustomerList object, self = current CustomerList object
        """
        Runs the routine to update the current system with
        data from the update system.
        Runs all kinds of checks to ensure reliability.
        Reports issues on the console.
        """
        print('start update proc')
        upd_cust_list.clean_customer_list()
        
        for i in range(len(upd_cust_list.customers)):

            cust = self.get_cust_by_id(upd_cust_list.customers[i].customer_id) #querying to get the customer who has the same id from the current system

            
                
            if cust is None: #no customer returned
                        
                if upd_cust_list.customers[i].update_flag == 'I': #normal case
                    try:
                        self.insert_customer(upd_cust_list.customers[i].copy())
                    except:
                        print('Insertion error for cust '+str(upd_cust_list.customers[i].customer_id))
                        print(sys.exc_info())

                elif upd_cust_list.customers[i].update_flag == 'D':
                    print('warning')  #maybe the cust was already deleted in a previous run, maybe it's something that should be looked into
                            
                elif upd_cust_list.customers[i].update_flag == 'U':
                    #depending on the expected behavior, this should trigger an exception or just a warning
                    print('Update error: Customer with ID '+str(upd_cust_list.customers[i].customer_id)+' not found in the current instance')
                            
            else:
                if upd_cust_list.customers[i].update_date >= cust.update_date: #there's no point checking any further if the update record is older than the current record
                        
                    if upd_cust_list.customers[i].update_flag == 'U':
                        try:
                            self.update_row(upd_cust_list.customers[i])
                        except:
                            print('Update error for cust '+str(upd_cust_list.customers[i].customer_id))
                            print(sys.exc_info())
                        
                    elif upd_cust_list.customers[i].update_flag == 'D':
                        try:
                            self.delete_cust_from_list(cust)
                        except:
                            print('Deletion error for cust '+str(upd_cust_list.customers[i].customer_id))
                            print(sys.exc_info())
                        
                    elif upd_cust_list.customers[i].update_flag == 'I':
                        print('Insert warning: customer with ID '+str(cust.customer_id)+' already inserted in the current instance.')

    def purge_customer_list(self):
        """
        Empties list of customers. Will usually
        be used to purge the customer rows from
        the update system.
        """
        self.customers = []
                


if __name__ == '__main__':
    tmp_list = []
    N = int(input()) #number of rows of current customer data

    #get list of customer space-separated data, one customer per row, in the right order: ID update_date [location]
    for _ in range(N):
        cust_data = input().split()
        #creating the list of Customer objects
        curr_cust_list = CustomerList([],'Current')
        if len(cust_data) == 2: #when we have an empty location, the ID and date cannot be empty
            cust_data.append('')
        tmp_list.append(Customer(cust_data[0],cust_data[1],cust_data[2]))
        curr_cust_list.customers = tmp_list

    tmp_list = []
    M = int(input()) #number of rows of updated customer data

    #get list of customer space-separated data, one customer per row, in the right order: ID update_date [location] update_flag
    for _ in range(M):
        cust_data = input().split()
        #creating the list of Customer objects
        upd_cust_list = CustomerList([],'Update')
        if len(cust_data) == 3: #when we have an empty location, other values cannot be empty
            cust_data.append(cust_data[2])
            cust_data[2] = ''
        tmp_list.append(Customer(cust_data[0],cust_data[1],cust_data[2],cust_data[3]))
        upd_cust_list.customers = tmp_list

    #updating the current system
    curr_cust_list.update_curr_cust_list(upd_cust_list)


    print('\n********* After update ********')
    print(upd_cust_list)
    print(curr_cust_list)

    
    upd_cust_list.purge_customer_list()
    print('\n********* After purge of update system ********')
    print(upd_cust_list)

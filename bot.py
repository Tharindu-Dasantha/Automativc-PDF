import datetime
from fillpdf import fillpdfs
import pandas as pd
import os


def main(): 
    formFields = list(fillpdfs.get_form_fields('Template.pdf').keys())

    # validate the name input
    Name = get_name()
    
    # Get the today's date
    Date = datetime.datetime.today()
    
    # reading data from the csv file
    df = pd.read_csv('smalldata.csv')
    
    for index, row in df.iterrows():
        CustomerName = row['CustomerName']
        DueDate = row['DueDate']
        Amount = row['Price']
        PaidAmount = row['PaidPrice']
        Balance = calculate_balance(Amount, PaidAmount)
        
        add_values(formFields, Name, CustomerName, Date, DueDate, Amount, PaidAmount, Balance)
    
    
def calculate_balance(Amount, PaidAmount):
    return Amount - PaidAmount


# Adding values
def add_values(formFields, Name, CustomerName, Date, DueDate, Amount, PaidAmount, Balance):
    data_dict = {
        formFields[0]: Name,
        formFields[1]: CustomerName,
        formFields[2]: Date,
        formFields[3]: DueDate,
        formFields[4]: Amount,
        formFields[5]: PaidAmount,
        formFields[6]: Balance
    }
    
    fillpdfs.write_fillable_pdf('Template.pdf', os.path.join('invoices', f'{CustomerName}.pdf') , data_dict)
    



def get_name():
    while(True):
        name = input("Enter you name: ")
        error = validate_name(name)
        if not error:
            break
        print("Invalid name. Please try again.")
            

def validate_name(name):
    name = name.strip()
    if not name:
        return True
    return False



if __name__ == '__main__':
    main()
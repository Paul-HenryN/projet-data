from openpyxl import Workbook

def create_excel_file(data, file_name):
    #Creation of a new Excel Workbook
    Wkbks = Workbook()
    
    #Select the active sheet of the Workbook
    sht = Wkbks.active

    #Insertion of the columns' readings on the first line of the sheet
    data.insert(0, ['Vehicles_no', 'Iterations_no', 'Clients_no', 'Covered_dist', 'Convergence_Time', 'Mem_Storage'])

    #Insertion of data in the sheet
    for row in data:
        sht.append(row)
    
    #Save the Workbook with the specified file name     
    Wkbks.save(file_name)
    
    
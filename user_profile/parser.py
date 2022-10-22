from openpyxl import load_workbook
from pathlib import Path
def parser(request):
    group = request.user.first_name
    # Define Django project base directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    base_str = str(BASE_DIR)
    # Define text file name

    # for g in Schedule.get_groups(request):
    #     if User.first_name == g:
    #         filegroup = Schedule.group+'.xlsx'
    #     else:
    #         pass
    # a = User.first_name

    filename = group+'.xlsx'
    # Define the full file path
    filepath = base_str + "\\schedule\\" + filename


    book = load_workbook(filename=filepath)
    sheet = book['Лист1']
    i = 0
    for item in book["Лист1"]:
        i = i + 1

    # text = ''

    a = {}
    keys = 'A', 'B', 'C', 'D', 'E', 'F'
    for key in keys:
        a.setdefault(key,[])
        for j in range(1, i+1):
            a[key].append(sheet[key + str(j)].value)
            

    # for j in range(2, i+1):
    #     # for k in 'ABCDE':
    #         # text += str(sheet[k + str(j)].value).split()
    #     text += sheet['A' + str(j)].value, sheet['B' + str(j)].value, sheet['C' + str(j)].value, sheet['D' + str(j)].value, sheet['E' + str(j)].value, sheet['F' + str(j)].value
    
    context = {
        'text': a
    }

    return (context)
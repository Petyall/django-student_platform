from openpyxl import load_workbook
from pathlib import Path
def parser(request):
    group = request.user.first_name
    BASE_DIR = Path(__file__).resolve().parent.parent
    base_str = str(BASE_DIR)

    filename = group+'.xlsx'
    filepath = base_str + "\\schedule\\" + filename


    book = load_workbook(filename=filepath)
    sheet = book['Лист1']
    i = 0
    for item in book["Лист1"]:
        i = i + 1


    a = {}
    keys = 'A', 'B', 'C', 'D', 'E', 'F'
    for key in keys:
        a.setdefault(key,[])
        for j in range(1, i+1):
            a[key].append(sheet[key + str(j)].value)
            
    
    context = {
        'text': a
    }

    return (context)
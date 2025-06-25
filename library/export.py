from openpyxl import Workbook
from django.http import HttpResponse
from .models import Book, Author, BorrowRecord

def export_library_data(request):
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Library Data'

    # Adding headers
    sheet.append(['Book Title', 'Author', 'Borrower', 'Borrow Date'])

    # Fetching data from the database
    borrow_records = BorrowRecord.objects.select_related('book', 'borrower').all()

    for record in borrow_records:
        sheet.append([
            record.book.title,
            record.book.author.name,
            record.borrower.username,
            record.borrow_date.strftime('%Y-%m-%d')
        ])

    # Creating the response
    response = HttpResponse(content=workbook.save(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=library_data.xlsx'

    return response
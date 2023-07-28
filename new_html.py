from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration
from django.template.loader import render_to_string
from django.http import HttpResponse

def generate_pdf():
    # Получите данные из базы данных (это пример, вы должны заменить это на свой код получения данных)
    data_from_db = {
        'title': 'Мальта 2 Евро, 2017 | Malta 2 euro 2017 Hagar Qim title from script'
    }

    # Сгенерируйте HTML с помощью Django шаблона и заполните его данными из базы данных
    html_content = render_to_string('index.html', data_from_db)

    # Установка размера страницы на A4
    font_config = FontConfiguration()
    pdf_file = "output.pdf"
    HTML(string=html_content).write_pdf(pdf_file, font_config=font_config, presentational_hints=True)

    # Отправьте PDF файл в ответе
    # with open(pdf_file, 'rb') as pdf:
    #     response = HttpResponse(pdf.read(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'inline; filename="output.pdf"'
    #     return response

generate_pdf()
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

# HTML-код для конвертации
html_file = 'new_index.html'

font_config = FontConfiguration()

# Установка собственного размера страницы (в миллиметрах)
width_mm = 300  # Ширина страницы в мм (например, A4 = 210 мм)
height_mm = 250  # Высота страницы в мм (например, A4 = 297 мм)

# Создание объекта CSS с указанными размерами страницы
css = CSS(string=f'@page {{ size: {width_mm}mm {height_mm}mm; }}')

# Создание объекта HTML и передача объекта CSS в качестве стилей
pdf = HTML(html_file).write_pdf(stylesheets=[css], font_config=font_config)

pdf_file = "output.pdf"
with open(pdf_file, 'wb') as f:
    f.write(pdf)

print("PDF создан успешно!")


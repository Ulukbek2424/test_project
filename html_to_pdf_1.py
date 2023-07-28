from weasyprint import HTML
from weasyprint.text.fonts import FontConfiguration

# HTML-код для конвертации
html_file = 'new_index.html'

font_config = FontConfiguration()

# Установка размера страницы на A4
pdf_file = "output.pdf"
HTML(filename=html_file).write_pdf(pdf_file, font_config=font_config, presentational_hints=True)

print("PDF создан успешно!")

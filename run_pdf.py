from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Table, TableStyle, KeepInFrame



# Создание PDF файла
pdf_file = "example.pdf"

# Определение размера страницы (A4)
page_width, page_height = A4

# Определение цвета фона (rgb = DED6D6)
background_color = colors.HexColor("#141414")

# Создание объекта Canvas с указанием размера страницы и шрифта
c = canvas.Canvas(pdf_file, pagesize=(page_width, page_height))

# Установка цвета фона для всей страницы
c.setFillColor(background_color)
c.rect(0, 0, page_width, page_height, fill=True, stroke=False)

# Загрузка шрифта с поддержкой кириллицы
pdfmetrics.registerFont(TTFont('DejaVuSans', 'DejaVuSans.ttf'))

# Использование шрифта с поддержкой кириллицы
c.setFont("DejaVuSans", 20)

# Создание стиля для заголовка
title_style = ParagraphStyle("Title", fontName="DejaVuSans-Bold", fontSize=20, alignment=1)

# Определение текста заголовка (включая русский текст)
title_text = "Кыргызстан 3 Киргизский сом, 2008"

# Определение координат для центрирования заголовка
title_x = page_width / 2
title_y = page_height - inch  # Заголовок будет располагаться над верхним краем страницы с отступом в 1 дюйм

# Рисование заголовка на странице
c.setFillColor(colors.white)
c.drawCentredString(title_x, title_y, title_text)

# Определение координат для позиционирования фотографий
photo_x = page_width / 2 - inch * 2.2 # Начальная координата X
photo_y = title_y - inch * 3  # Начальная координата Y

# Загрузка и добавление первой фотографии
photo1_path = "3_som.jpg"
photo1 = ImageReader(photo1_path)
c.drawImage(photo1, photo_x, photo_y, width=150, height=150)

# Определение пространства между фотографиями
space_between_photos = 0.25 * inch

# Перемещение координаты X для второй фотографии
photo_x += 150 + space_between_photos

# Загрузка и добавление второй фотографии
photo2_path = "3_som_back.jpg"
photo2 = ImageReader(photo2_path)
c.drawImage(photo2, photo_x, photo_y, width=150, height=150)

# Определение координат для позиционирования списка
list_spacing = 36 * 0.75 # Пространство между пунктами списка (в пикселях)
list_x = page_width / 2 - inch * 2.8  # Начальная координата X
list_y = photo_y - inch / 2 - list_spacing  # Начальная координата Y с учетом отступа

# Определение координат для позиционирования таблицы
list_spacing = 36 * 0.75 # Пространство между пунктами списка (в пикселях)
table_x = page_width / 2 - inch * 2.8  # Начальная координата X
table_y = photo_y - inch / 2 - list_spacing  # Начальная координата Y с учетом отступа

# Определение данных для таблицы
data = [
    ["KM Code", "km15"],
    ["Страна", "Кыргызстан"],
    ["Серия", "2008~н.в. - Республика - Обращение"],
    ["Год начала выпуска", "2008"],
    ["Год конца выпуска", "2008"],
    ["Распространение", "Стандартный тираж"],
    ["Монетный двор", "Казахстан монетный двор НБ РК, г. Усть-Каменогорск, Казахстан"],
    ["Материал", "Никелированая сталь"],
    ["Описание состава", "~ 90% железо, 1,2 углерод, 9% никель"],
]

# Определение стиля таблицы
table_style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#141414")),  # Задаем белый фон для ячеек с данными
    ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),  # Задаем черный цвет текста для заголовка
    ("TEXTCOLOR", (0, 0), (0, -1), colors.HexColor("#555555")),  # Задаем красный цвет текста для значений первого столбца
    ("ALIGN", (0, 0), (-1, -1), "LEFT"),  # Выравниваем текст по центру
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),  # Выравниваем текст по вертикали посередине для всех ячеек таблицы
    ("FONTNAME", (0, 0), (-1, -1), "DejaVuSans"),  # Задаем жирный шрифт для заголовка
    ("FONTSIZE", (0, 0), (-1, -1), 14),  # Задаем размер шрифта для заголовка
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),  # Задаем отступ снизу для заголовка
    ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#555555")),  # Задаем черные границы для всех ячеек
    ("WORDWRAP", (0, 0), (-1, -1), True),  # Включаем перенос строк
])

# Создание таблицы
column_widths = [250, 250]
table = Table(data, style=table_style, colWidths=column_widths, rowHeights=30)

# Расчет ширины столбцов таблицы
table_width, table_height = table.wrapOn(c, page_width, page_height)
column_widths = [table_width / 2] * 2

# Определение координат для центрирования таблицы
table_x = (page_width - table_width) / 2
table_y -= table_height

# Рисование таблицы на странице
table.drawOn(c, table_x, table_y)

# Закрытие PDF файла
c.save()

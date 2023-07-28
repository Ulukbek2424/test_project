import re

size = "172 x 101"

# Извлечение чисел из строки с помощью регулярного выражения
match = re.match(r"(\d+)\s*x\s*(\d+)", size)

if match:
    length = int(match.group(1))
    width = int(match.group(2))
else:
    length = None
    width = None

print(length)  # 172
print(width)  # 101

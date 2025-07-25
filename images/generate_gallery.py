import os

# Путь к папке с изображениями
image_folder = "images"
output_file = "gallery.html"

# Получаем список изображений
image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.jfif')
images = [f for f in os.listdir(image_folder) if f.lower().endswith(image_extensions)]

# Начало HTML
html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Галерея</title>
  <style>
    body {{
      background: #000;
      color: white;
      font-family: sans-serif;
      margin: 0;
      padding: 0;
      text-align: center;
    }}
    header, footer {{
      background: rgba(0, 0, 0, 0.7);
      padding: 1.5rem;
    }}
    .gallery {{
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 1rem;
      padding: 2rem;
    }}
    .gallery img {{
      width: 280px;
      height: auto;
      border-radius: 10px;
      box-shadow: 0 0 15px lime;
      transition: transform 0.3s ease;
    }}
    .gallery img:hover {{
      transform: scale(1.05);
    }}
    a.button {{
      display: inline-block;
      margin-top: 1rem;
      background: lime;
      padding: 12px 24px;
      color: black;
      text-decoration: none;
      border-radius: 8px;
      font-weight: bold;
    }}
    a.button:hover {{
      background: #6eff6e;
    }}
  </style>
</head>
<body>
  <header>
    <h1>🖼️ Галерея</h1>
    <p>Автоматически собранная из папки <code>{image_folder}/</code></p>
  </header>

  <main class="gallery">
"""

# Добавляем изображения
for image in images:
    html += f'    <img src="{image_folder}/{image}" alt="{image}">\n'

# Закрытие HTML
html += """
  </main>

  <footer>
    <p><a href="index.html" class="button">🔙 Назад</a></p>
  </footer>
</body>
</html>
"""

# Сохраняем файл
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Галерея создана: {output_file} (найдено {len(images)} изображений)")

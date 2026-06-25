import os

def generate_html():
    """Генерирует HTML-страницу с информацией об Университете «Синергия»."""

    html_content = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Университет «Синергия»</title>
    <style>
        /* Сброс отступов */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            font-family: Raleway, sans-serif;
            padding: 20px;
        }

        .container {
            max-width: 900px;
            width: 100%;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
            padding: 40px;
        }

        h1 {
            text-align: center;
            color: #1a3c6e;
            border-bottom: 3px solid #1a3c6e;
            padding-bottom: 15px;
            margin-bottom: 30px;
        }

        .info-block {
            margin-bottom: 30px;
        }

        .info-block h2 {
            color: #1a3c6e;
            margin-bottom: 10px;
            font-size: 1.2rem;
        }

        .info-block p {
            line-height: 1.6;
            color: #333;
        }

        .info-block ul {
            list-style: none;
            padding: 0;
        }

        .info-block ul li {
            padding: 8px 0;
            border-bottom: 1px solid #eee;
            color: #333;
        }

        .info-block ul li strong {
            color: #1a3c6e;
        }

        /* Секция с примерами шрифтов */
        .font-examples {
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #e0e0e0;
        }

        .font-examples h2 {
            text-align: center;
            color: #1a3c6e;
            margin-bottom: 20px;
        }

        .font-card {
            background-color: #f9f9fc;
            border-radius: 8px;
            padding: 15px 20px;
            margin-bottom: 15px;
            border-left: 4px solid #1a3c6e;
        }

        .font-card .font-name {
            font-size: 0.85rem;
            color: #666;
            margin-bottom: 5px;
        }

        .font-card .sample-text {
            font-size: 1.2rem;
            color: #222;
        }

        /* Стили для каждого шрифта */
        .font-official {
            font-family: 'Raleway', sans-serif;
        }

        .font-1 {
            font-family: 'Times New Roman', serif;
        }

        .font-2 {
            font-family: 'Courier New', monospace;
        }

        .font-3 {
            font-family: Georgia, serif;
        }

        .font-4 {
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }

        .font-5 {
            font-family: 'Trebuchet MS', sans-serif;
        }

        /* Адаптивность */
        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Университет «Синергия»</h1>

        <div class="info-block">
            <h2>Об организации</h2>
            <p>
                <strong>Университет «Синергия»</strong> (Московский финансово-промышленный университет «Синергия») — 
                российское частное высшее учебное заведение, основанное в 1995 году в Москве.
            </p>
        </div>

        <div class="info-block">
            <h2>Основные сведения</h2>
            <ul>
                <li><strong>Полное наименование:</strong> Автономная некоммерческая организация высшего образования «Московский университет «Синергия»</li>
                <li><strong>Сокращенное наименование:</strong> Университет «Синергия»</li>
                <li><strong>Год основания:</strong> 1995</li>
                <li><strong>Территориальное размещение:</strong> г. Москва, ул. Мещанская, д. 9/14, стр. 1</li>
            </ul>
        </div>

        <div class="info-block">
            <h2>Деятельность</h2>
            <p>
                Университет предлагает образовательные программы 
                по направлениям бакалавриата, магистратуры, специалитета, аспирантуры, 
                а также программы среднего профессионального образования и дополнительного 
                профессионального образования.
            </p>
        </div>

        <!-- Секция с примерами шрифтов -->
        <div class="font-examples">
            <h2>Примеры шрифтов</h2>

            <div class="font-card">
                <div class="font-name">Официальный шрифт Raleway</div>
                <div class="sample-text font-official">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>

            <div class="font-card">
                <div class="font-name">Вариант 1: Times New Roman</div>
                <div class="sample-text font-1">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>

            <div class="font-card">
                <div class="font-name">Вариант 2: Courier New</div>
                <div class="sample-text font-2">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>

            <div class="font-card">
                <div class="font-name">Вариант 3: Georgia</div>
                <div class="sample-text font-3">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>

            <div class="font-card">
                <div class="font-name">Вариант 4: Comic Sans MS</div>
                <div class="sample-text font-4">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>

            <div class="font-card">
                <div class="font-name">Вариант 5: Trebuchet MS</div>
                <div class="sample-text font-5">
                    Университет «Синергия» — образование для успешной карьеры.
                </div>
            </div>
        </div>
    </div>
</body>
</html>
    """

    # Сохраняем файл
    with open("university_synergy.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ HTML-страница успешно создана: university_synergy.html")
    print("📂 Откройте этот файл в любом браузере для просмотра.")


if __name__ == "__main__":
    generate_html()

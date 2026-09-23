# Є відкритий офіційний API NASA Images and Video Library ( https://images-api.nasa.gov ), який дозволяє виконувати пошук медіа та отримувати список файлів (assets) для кожного знайденого медіа-елемента.
#
# Ваше завдання - за допомогою модуля requests:
#
#     Виконати пошук зображень, пов’язаних з ровером Curiosity на Марсі.
#     З JSON відповіді витягнути nasa_id для знайдених елементів.
#     Для кожного nasa_id зробити додатковий запит до endpoint-а /asset/{nasa_id}, щоб отримати список URL-ів файлів.
#     Обрати з цього списку посилання на JPG-зображення (наприклад, перший .jpg або “найкращий” варіант, якщо їх кілька).
#     Скачати 2 зображення і зберегти локально як:
#     mars_photo1.jpg
#     mars_photo2.jpg
#
# Важливо: потрібно виконати мінімум 3 HTTP-запити:
#
# 1 запит /search + 2 запити /asset/{nasa_id} (і ще 2 запити на скачування jpg-файлів).
#
# Доступні endpoint-и (Images API)
#
#     GET /search?q={q} - пошук медіа
#     GET /asset/{nasa_id} - список файлів (URL) для вибраного медіа

import requests

BASE_URL = "https://images-api.nasa.gov"

# Параметри пошуку
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}


# Функція пошуку зображень
def search_images(search_params):
    search_url = f"{BASE_URL}/search"

    response = requests.get(
        search_url,
        params=search_params
    )
    response.raise_for_status()

    data = response.json()
    items = data['collection']['items']

    return items


# Функція отримання URL оригінального зображення
def get_original_image_url(nasa_id):
    asset_url = f"{BASE_URL}/asset/{nasa_id}"

    picture = requests.get(asset_url)
    picture.raise_for_status()

    picture_json = picture.json()
    picture_items = picture_json['collection']['items']

    for picture_orig in picture_items:
        picture_href = picture_orig.get("href")

        if picture_href is not None and picture_href.endswith("~orig.jpg"):
            return picture_href

    return None


# Функція завантаження зображення
def download_image(picture_href, filename):
    picture_download = requests.get(picture_href)
    picture_download.raise_for_status()

    with open(filename, "wb") as f:
        f.write(picture_download.content)


# Пошук зображень
search_images_items = search_images(search_params)


# Обробка перших двох результатів
for index, item in enumerate(search_images_items[:2], start=1):
    item_data = item['data']
    nasa_id = item_data[0]['nasa_id']

    download_picture_link = get_original_image_url(nasa_id)

    filename = f"mars_photo{index}.jpg"

    download_image(download_picture_link, filename)
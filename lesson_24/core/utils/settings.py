from dynaconf import Dynaconf

from lesson_24.definitions import BASE_FOLDER


# Завантажуємо налаштування проєкту з конфігураційних файлів.
d_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        BASE_FOLDER / ".settings.toml",
        BASE_FOLDER / ".secrets.toml",
    ],
    environments=True,
    load_dotenv=True,
)
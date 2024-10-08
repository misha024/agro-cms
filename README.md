# AgroCMS

## О проекте

**AgroCMS** - это CMS-система для легковесных сайтов.

## Функциональность

- **Управление** - весь контейнт на сайте можно изменить (картинки, названия, имя сайта, иконка, каталоги, товары, контакты).
- **Оптимизация** - за счет шаблонизатора сайт работает очень быстро, следственно выше подымается в топе.
- **Интерфейс** - очень просто и понятный каждому пользователю.
- **Качество кода** - кода очень мало, этот репозиторий может выступать как начало вашего проекта, начало структуры уже положено, не составит особого труда переписать под ваши нужды.

### Данные по умолчанию:

<details open>
<summary>Админ-панель</summary>

    Логин: admin
    Пароль: admin
</details>

## Установка и настройка

Для запуска **AgroCMS** в режиме разработки выполните следующий скрипт:

    docker-compose -f deployment/dev/docker-compose.dev.yml up --build

## Деплой


- **1.** В файле **"main/settings/prod.py"** и измените в **ALLOWED_HOSTS** и **CSRF_TRUSTED_ORIGINS** "domain.com" на свой домен
- **2.** Далее в **"deployment/prod/nginx.conf"** впишите в **server_name** свой домен.
- **3.** Сгенерируйте сертификаты и перенести их в папку **deployment/prod/certificates**.
- **4.** Для запуска **AgroCMS** в "боевой готовности" выполните следующий скрипт:

    
    docker-compose -f deployment/dev/docker-compose.prod.yml up --build


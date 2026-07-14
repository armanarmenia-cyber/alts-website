# Настройка Make для форм ALTS

Все три формы (Buyer, Exhibitor, Contact) шлют JSON на один webhook. Поле `form` различает источник: `buyer-registration`, `exhibitor-registration`, `contact`.

## Шаг 1. Создать webhook

1. make.com → Scenarios → **Create a new scenario**
2. Первый модуль: **Webhooks → Custom webhook** → Add → имя, например `ALTS Site Forms` → Save
3. Скопировать URL вида `https://hook.eu2.make.com/xxxxxxxxx`
4. **Прислать URL мне** — я вставлю его в три страницы (константа `MAKE_WEBHOOK_URL` внизу каждого файла). Или вставить самим: найти строку `PASTE_MAKE_WEBHOOK_URL_HERE` в `alts-buyer-registration.html`, `alts-exhibitor-registration.html`, `alts-contact.html`.

## Шаг 2. Обучить webhook структуре

В сценарии нажать **Run once**, затем открыть любую форму на сайте, заполнить и отправить. Make поймает запрос и запомнит поля.

Поля buyer-формы: `form, first_name, last_name, position, company, country_city, website, email, phone, events[], question, page, submitted_at`
Exhibitor: `form, first_name, last_name, email, phone, brand, website, events[], question, page, submitted_at`
Contact: `form, role, name, email, message, page, submitted_at`
Full-buyer: всё из buyer + `city, country, description, business_started, business_type, employees, client_spend, turnover, five_star_share, consortia, trade_shows, regions, products, clients_based, top_hotels, recent_bookings` (каждый ответ анкеты — отдельный ключ; `question` дублирует всё одним текстом для совместимости)
Full-exhibitor: `first_name, last_name, company, position, country_city, website, email, phone, events[]` + `package_baltic, package_lisbon, extras_lisbon, package_warsaw, extras_warsaw, legal_name, vat, invoice_address, attendee2, catalogue, materials` (+ `question` — дубль одним текстом)

**Важно:** после добавления новых полей в форму нужно в Make открыть модуль Webhook → **Redetermine data structure** → отправить тестовую заявку с сайта, иначе новые поля не появятся в маппинге.

## Шаг 3. Добавить получателей (после webhook)

### Email
Модуль **Email → Send an Email** (или Gmail/Outlook — что используете).
- To: ваш адрес заявок
- Subject: `Новая заявка ALTS: {{form}} — {{first_name}} {{last_name}}`
- Body: перечислить поля из webhook.

### Google Sheets
Модуль **Google Sheets → Add a Row**.
- Создать таблицу «ALTS Leads» с колонками: Date, Form, Name, Email, Phone, Company/Brand, Events, Question, Page
- Смэпить: `{{submitted_at}}`, `{{form}}`, `{{first_name}} {{last_name}}`, `{{email}}` и т.д.
- Events — массив: использовать `join(events; ", ")`

### Flowlu CRM
Модуль **Flowlu → Create an Opportunity** (или Create CRM Account/Contact — как ведёте лиды).
- Подключение: Flowlu → Портал → Settings → API → создать ключ → вставить в Make (нужен домен портала `*.flowlu.com` и API key)
- Name: `ALTS {{form}} — {{first_name}} {{last_name}}`
- Description: question + events + page
- Контакт: email, phone

### Разветвление (опционально)
Если contact-форму нужно слать только на почту (без CRM), после webhook добавить **Router** и в ветке Flowlu поставить фильтр `form ≠ contact`.

## Шаг 4. Включить

Save → тумблер **Scheduling ON** (Immediately). Готово: заявки идут на почту, в таблицу и в CRM одновременно.

## Проверка
Отправить тестовую заявку с каждой формы, убедиться что: пришло письмо, появилась строка в Sheets, создался лид во Flowlu.

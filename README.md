# ALTS — Access Luxury Travel Show (редизайн сайта)

Статический сайт: чистый HTML/CSS/JS, без сборки и без зависимостей. Открой `index.html` в браузере — это весь «запуск» проекта.

## Структура

```
index.html                        — главная (копия alts-redesign-home.html)
alts-redesign-home.html           — главная
alts-events.html                  — все события (upcoming + past)
alts-event-*.html                 — страницы будущих ивентов (Baltics, Lisbon, Warsaw)
alts-past-*.html                  — страницы прошедших ивентов (14 шт.)
alts-about.html                   — о компании
alts-contact.html                 — контакты + форма
alts-buyer-registration.html      — короткая заявка Buyer
alts-exhibitor-registration.html  — короткая заявка Exhibitor
alts-full-buyer-registration.html     — полная анкета Buyer
alts-full-exhibitor-registration.html — полная анкета Exhibitor (пакеты, цены)
assets/
  alts.css          — общие стили (для всех страниц, кроме двух: см. ниже)
  wave-a/b/c.svg    — фирменные волны (вектор)
  wordmark-white.png, tagline-white.png, logo-white.svg — лого Access
  gen_past.py, gen_past2.py — генераторы страниц прошедших ивентов
MAKE-SETUP.md       — как устроен приём заявок через Make.com
```

Особенность: `alts-redesign-home.html`/`index.html` и `alts-event-uk-eu-lisbon.html` несут стили внутри себя (тег `<style>`), остальные страницы подключают `assets/alts.css`. Меняешь общий стиль — правь и css-файл, и эти две страницы.

Картинки и видео грузятся с CDN текущего сайта (cdn.prod.website-files.com). Пока Webflow-сайт жив — всё работает; при полном отказе от Webflow медиа нужно будет перенести в `assets/` (или на свой CDN) и заменить пути.

## Формы и заявки (Make.com)

Все 5 форм шлют JSON в один webhook Make:
`https://hook.eu1.make.com/awvokqplkq7yc69hc7s5a641qfs46e7v`

Поле `form` различает источник: `buyer-registration`, `exhibitor-registration`, `contact`, `full-buyer-registration`, `full-exhibitor-registration`. Сценарий в Make: Webhook → Gmail (+ опционально Google Sheets, Flowlu). Подробности и маппинг полей — в `MAKE-SETUP.md`. URL вебхука задаётся константой `MAKE_WEBHOOK_URL` внизу каждой страницы с формой.

## Деплой

**Вариант A (просто):** app.netlify.com → сайт → вкладка Deploys → перетащить всю папку проекта. Обновление за ~30 сек.

**Вариант B (автомат, рекомендуется):**
1. Репозиторий на GitHub (git уже инициализирован, первый коммит сделан)
2. Netlify → Add new site → Import an existing project → GitHub → выбрать репозиторий
3. Build settings: build command — пусто, publish directory — `/` (корень)
4. Дальше каждый `git push` в main автоматически выкатывает сайт

**Боевой домен:** Netlify → Domain settings → Add custom domain → altsevents.com → у регистратора прописать CNAME/A по инструкции Netlify. До переключения DNS старый Webflow-сайт продолжает работать.

## Как вносить правки

Текст/контент: открыть нужный .html, найти текст, поправить. Страницы прошедших ивентов удобнее регенерировать: данные лежат в `assets/gen_past.py` и `gen_past2.py` (python3 gen_past.py из папки assets).

Чеклист после правок: открыть локально, проверить страницу + мобильную ширину, отправить тест с формы (если трогал формы), задеплоить.

## Известные TODO

- Страницы ALTS Exhibitors, Privacy Policy, Cookie Policy пока не перенесены (ссылки ведут на старый сайт)
- Полная анкета exhibitor: фото для каталога просим прислать на email (webhook не принимает файлы)
- В агенде Warsaw 2026 на старом сайте даты противоречат шапке (20–21 vs 21–22 окт) — у нас 21–22, уточнить у команды

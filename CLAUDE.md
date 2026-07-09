# ALTS Website — инструкции для Claude

Это редизайн сайта altsevents.com (Access Luxury Travel Show) — статический HTML/CSS/JS сайт, задеплоенный на Netlify через GitHub. Полная документация — в README.md, прочитай его перед работой.

## Ключевые правила

1. **Стили.** Общие стили — в `assets/alts.css`. НО две страницы несут стили внутри себя (тег `<style>`): `alts-redesign-home.html` (и его копия `index.html`) и `alts-event-uk-eu-lisbon.html`. Меняя общий стиль (цвета, кнопки, шапку, футер) — правь и css, и эти две страницы.

2. **index.html — копия alts-redesign-home.html.** После правок главной обнови копию: `cp alts-redesign-home.html index.html`.

3. **Дизайн-система:** Montserrat + Playfair Display (italic для акцентов), periwinkle #8A8FD4, navy #2F3460, градиент var(--grad), волны assets/wave-a/b/c.svg по краям секций, кнопки-пилюли. Новые страницы строй из существующих секций-паттернов (hero, numbers, agenda, apply, next).

4. **Формы** (buyer, exhibitor, contact, full-buyer, full-exhibitor) шлют JSON в webhook Make.com — константа MAKE_WEBHOOK_URL внизу каждой страницы с формой. Поле `form` в payload различает формы — не менять существующие имена полей, иначе сломается сценарий в Make (email/CRM). Детали — MAKE-SETUP.md.

5. **Страницы прошедших ивентов** (alts-past-*.html) генерируются скриптами `assets/gen_past.py` и `gen_past2.py`. Для правок этих страниц лучше править данные в скрипте и перегенерировать (python3 из папки assets), а не HTML руками.

6. **Медиа** грузятся с CDN Webflow (cdn.prod.website-files.com) — старый сайт ещё жив. Новые картинки клади в assets/.

7. **Деплой:** git commit + push в main → Netlify выкатывает автоматически (~1 мин). Перед началом работы — git pull. Не трогай git remote и netlify.toml без необходимости.

8. **Проверка после правок:** открыть страницу локально, проверить мобильную ширину (бургер-меню ≤1080px), при изменении форм — тестовая отправка.

## Известные TODO
- ALTS Exhibitors, Privacy/Cookie Policy — не перенесены (ссылки на старый сайт)
- Файлы (фото каталога) в full-exhibitor форме — просим на email, webhook не принимает файлы

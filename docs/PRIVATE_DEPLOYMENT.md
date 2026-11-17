# Приватний онлайн-доступ до Betonarka-Manager

**Поточний стан:** код у приватному GitHub-репозиторії `TechSite-Solutions/Betonarka-Manager`. Сайт ще **не розгорнуто**, запрошення не налаштовані. Не вважайте GitHub Pages приватним через те, що репозиторій приватний.

## Рекомендована архітектура на першому етапі

- Вихідний код: приватний GitHub-репозиторій.
- Статичний сайт: Cloudflare Pages, підключений до гілки `main` цього репозиторію.
- Авторизація **перед сайтом**: Cloudflare Access, політика `Allow` лише для конкретних адрес e-mail.
- Вхід запрошених: One-time PIN на дозволену електронну адресу.
- **Увага:** нинішня програма зберігає замовлення локально у браузері. Cloudflare Access захищає відкриття сайту, але **не** забезпечує спільну базу замовлень або синхронізацію між користувачами.

## Кроки налаштування

1. Увійдіть у [Cloudflare Dashboard](https://dash.cloudflare.com/). Створіть Workers & Pages → Pages → Connect to Git.
2. Підключіть GitHub до Cloudflare (надайте доступ тільки до `TechSite-Solutions/Betonarka-Manager`), виберіть цей приватний репозиторій.
3. Оберіть гілку `main`. Проєкт — статичний HTML/CSS/JS: не потрібна команда збірки, вихідна директорія — корінь репозиторію (`.`). Переконайтеся, що `index.html` у корені.
4. **Важливо:** Cloudflare Pages за замовчуванням видає публічну URL після розгортання. Не використовуйте програму з реальними контактами клієнтів, доки не буде налаштовано Access і перевірено всі адреси сайту.
5. У Cloudflare Zero Trust → Access controls → Applications створіть політику Access для production-адреси `<назва>.pages.dev`: `Allow` → `Emails` → конкретні запрошені адреси. Не використовуйте правило `Everyone`, `Everyone on Internet` або `Email domain` замість поіменного переліку.
6. У Zero Trust → Integrations → Identity providers увімкніть `One-time PIN`, якщо його ще немає. Користувач з дозволеним e-mail отримуватиме разовий код.
7. За інструкцією Cloudflare **Enable Access on your `*.pages.dev` domain** потрібно захистити **production** `<назва>.pages.dev` окремо від `*.<назва>.pages.dev` preview-адрес. Вбудована кнопка «Enable access policy» для preview **сама по собі не закриває production**.
8. Якщо додаєте власний домен, створіть **окрему** політику Access для нього та перевірте, що немає доступу через обхідну `pages.dev` URL.
9. Перевірте з нового приватного вікна браузера: незапрошена адреса не отримує доступ; запрошена проходить OTP; і production, і preview, і власний домен захищені.
10. Лише після перевірки можна передавати посилання запрошеним. Виключення e-mail із політики має блокувати нові входи; за потреби відкликайте активні Access-сесії.

## Важливі обмеження поточної версії

- Автозбереження відбувається у сховищі конкретного браузера та конкретного origin (`http://127.0.0.1:8765` і `https://<назва>.pages.dev` **не поділяють** localStorage).
- Один запрошений співробітник **не побачить** замовлень, які інший додав у своєму браузері. Це наступний окремий етап: серверна БД, авторизація по користувачах, права доступу, журнал змін, резервні копії.
- Дані клієнтів не потрібно комітити в GitHub або вбудовувати в код HTML.
- Для безпеки не покладайтеся на пароль у JavaScript, приховану URL або `robots.txt` — вони не обмежують доступ.

## Джерела

- [GitHub: About privately published GitHub Pages sites](https://docs.github.com/en/enterprise-cloud@latest/pages/getting-started-with-github-pages/about-privately-published-github-pages-sites)
- [Cloudflare Pages: Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
- [Cloudflare Pages: Known issues — Enable Access on pages.dev](https://developers.cloudflare.com/pages/platform/known-issues/)
- [Cloudflare Pages: Preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/)
- [Cloudflare: One-time PIN login](https://developers.cloudflare.com/cloudflare-one/integrations/identity-providers/one-time-pin/)

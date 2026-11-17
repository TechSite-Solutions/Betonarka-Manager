# GitHub Pages: публічна демоверсія «Бетонарка»

**Статус:** гілка `gh-pages` підготовлена, але публікація **не ввімкнена автоматично**.

## Що опублікуємо

Гілка `gh-pages` містить лише статичні файли `index.html`, `weekboard.css`, `concrete.css`, `.nojekyll` та короткий README. Вигадані замовники: `DEMO · Stavba Alfa`, `DEMO · Beton Beta`, `DEMO · Hala Gama`. У демо є попередження не вводити реальні клієнтські дані. Для демо використовується окремий ключ у `sessionStorage`, не робочий `localStorage`.

Гілка `main` залишається приватною і НЕ повинна ставати публічною лише заради демонстрації.

## Варіант 1: якщо організація має GitHub Team/Enterprise та доступні Pages у приватному репозиторії

1. Відкрити: https://github.com/TechSite-Solutions/Betonarka-Manager/settings/pages
2. У `Build and deployment` обрати `Source: Deploy from a branch`.
3. `Branch: gh-pages`, `Folder: /(root)`, натиснути `Save`.
4. Дочекатися повідомлення GitHub про успішне розгортання; відкрити відображену у Pages Settings адресу.
5. Перевірити сайт в анонімному вікні, що він позначений `ПУБЛІЧНА ДЕМО-ВЕРСІЯ`, містить лише вигаданих клієнтів, а імпорт резервної копії відключено.

У цьому сценарії репозиторій лишається приватним, але **сайт публічний**. За замовчуванням Pages із приватного репозиторію не обмежує доступ запрошеними.

## Варіант 2: GitHub Free для організацій (безкоштовно)

У GitHub Free Pages доступний для публічних репозиторіїв. Щоб зберегти основний репозиторій приватним:

1. Створити **окремий публічний репозиторій** `Betonarka-Manager-Demo` під `TechSite-Solutions`.
2. Скопіювати в корінь **тільки 5 файлів** з гілки `gh-pages` приватного репозиторію: `index.html`, `weekboard.css`, `concrete.css`, `.nojekyll`, `README.md`. НЕ копіювати дані/експорти/резервні копії.
3. У `Settings → Pages → Build and deployment` обрати `Deploy from a branch → main → /(root)` та `Save`.
4. Відкрити адресу, яку покаже GitHub Pages, і перевірити в анонімному режимі.

Типова адреса для окремого репозиторію: `https://techsite-solutions.github.io/Betonarka-Manager-Demo/` (поки не перевірено, це **лише очікувана адреса**, не підтверджений онлайн-сайт).

## Важливо

- Не вводьте справжні телефони, адреси чи e-mail клієнтів у публічну демоверсію.
- Дані інших користувачів **не синхронізуються**: демо працює тільки в браузері.
- Публікацію треба підтвердити саме в Settings → Pages, після чого перевірити URL.
- Ніколи не робіть `TechSite-Solutions/Betonarka-Manager` публічним заради Pages.
- Документація GitHub: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

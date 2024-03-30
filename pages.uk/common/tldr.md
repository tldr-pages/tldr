# tldr

> Відображає прості сторінки допомоги для інструментів командного рядка з проекту tldr-pages.
> Більше інформації: <https://github.com/tldr-pages/tldr/blob/main/CLIENT-SPECIFICATION.md#command-line-interface>.

- Показує типове використання команди (підказка: це те, як ви потрапили сюди!):

`tldr {{команда}}`

- Показує tldr сторінку для команди `cd` на вказаній платформі:

`tldr -p {{android|linux|osx|sunos|windows}} {{cd}}`

- Показує tldr сторінку для підкоманди Git `git checkout`:

`tldr {{git-checkout}}`

- Оновлює локальні tldr сторінки (якщо клієнт підтримує кешування):

`tldr -u`

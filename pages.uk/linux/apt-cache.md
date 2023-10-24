# apt-cache

> Інструмент запиту пакетів Debian і Ubuntu.
> Більше інформації: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Шукати пакет у ваших поточних джерелах:

`apt-cache search {{запит}}`

- Показати інформацію про пакет:

`apt-cache show {{пакет}}`

- Показати, чи встановлено та оновлено пакет:

`apt-cache policy {{пакет}}`

- Показати залежності для пакета:

`apt-cache depends {{пакет}}`

- Показати пакети, які залежать від конкретного пакета:

`apt-cache rdepends {{пакет}}`

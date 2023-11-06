# systemctl

> Керуйте системою systemd і диспетчером служб.
> Більше інформації: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Відобразити всі запущені служби:

`systemctl status`

- Відобразити список служб, які не запустилися через помилки:

`systemctl --failed`

- Запуск/зупинка/перезапуск/перезавантаження служби:

`systemctl {{start|stop|restart|reload}} {{служба}}`

- Показати статус служби:

`systemctl status {{служба}}`

- Увімкнути/вимкнути запуск служби під час завантаження:

`systemctl {{enable|disable}} {{служба}}`

- Маскування/розкриття служби, щоб запобігти ввімкненню та ручній активації:

`systemctl {{mask|unmask}} {{служба}}`

- Перезавантажити systemd, шукати нові або змінені пристрої:

`systemctl daemon-reload`

- Перевірити, чи ввімкнено службу до автозавантаження:

`systemctl is-enabled {{служба}}`

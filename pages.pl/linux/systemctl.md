# systemctl

> Kontroluj systemd i menedżera usług.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Wyświetl wszystkie działające usługi:

`systemctl status`

- Wyświetl nieudane jednostki:

`systemctl --failed`

- Uruchom/Zatrzymaj/Zrestartuj/Przeładuj usługę:

`systemctl {{start|stop|restart|reload}} {{jednostka}}`

- Wyświetl status jednostki:

`systemctl status {{jednostka}}`

- Włącz/Wyłącz automatyczne uruchamianie jednostki przy starcie systemu:

`systemctl {{enable|disable}} {{jednostka}}`

- Zamaskuj/Zdemaskuj jednostkę, aby uniemożliwić włączanie i ręczną aktywację:

`systemctl {{mask|unmask}} {{jednostka}}`

- Przeładuj systemd, skanując w poszukiwaniu nowych lub zmienionych jednostek:

`systemctl daemon-reload`

- Sprawdź, czy jednostka jest włączona:

`systemctl is-enabled {{jednostka}}`

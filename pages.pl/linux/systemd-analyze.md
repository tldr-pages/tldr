# systemd-analyze

> Analizuj i debuguj menedżera systemu.
> Wyświetl szczegóły dotyczące czasiu procesu uruchamiania jednostek (usług, punktów montowania, urządzeń, gniazd):
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- Wyświetl wszystkie uruchomione jednostki, uporządkowane według czasu ich inicjalizacji:

`systemd-analyze blame`

- Wyświetl drzewo krytycznego czasowo łańcucha jednostek:

`systemd-analyze critical-chain`

- Utwórz plik SVG pokazujący kiedy każda usługa wystartowała, zaznaczając czas wykorzystany na inicjalizację:

`systemd-analyze plot > {{ścieżka/do/pliku.svg}}`

- Sporządź wykres zależności i przekonwertuj go do pliku SVG:

`systemd-analyze dot | dot -T{{svg}} > {{ścieżka/do/pliku.svg}}`

- Wyświetl wyniki bezpieczeństwa działających jednostek:

`systemd-analyze security`

# bootctl

> Kontroluj ustawienia oprogramowania układowego EFI i zarządzaj programem rozruchowym.
> Więcej informacji: <https://manned.org/bootctl>.

- Wyświetl informacje o oprogramowaniu układowym i programach rozruchowych:

`bootctl status`

- Wyświetl wszystkie dostępne wpisy programu rozruchowego:

`bootctl list`

- Ustaw opcję, aby uruchomić oprogramowanie układowe przy następnym rozruchu (podobne do `sudo systemctl reboot --firmware-setup`):

`sudo bootctl reboot-to-firmware true`

- Podaj ścieżkę do partycji systemowej EFI (domyślnie `/efi/`, `/boot/` lub `/boot/efi`):

`bootctl --esp-path={{/ścieżka/do/partycji_systemowej_efi/}}`

- Zainstaluj `systemd-boot` do partycji systemowej EFI:

`sudo bootctl install`

- Usuń wszystkie zainstalowane wersje `systemd-boot` z partycji systemowej EFI:

`sudo bootctl remove`

# pio account

> A PlatformIO-fiók kezelése a parancssorban. További információ: <https://docs.platformio.org/en/latest/core/userguide/account/>.

- Új PlatformIO-fiók regisztrálása:

`pio account register --username {{username}} --email {{email}} --password {{password}} --firstname {{firstname}} --lastname {{lastname}}`

- A PlatformIO-fiók és a kapcsolódó adatok végleges törlése:

`pio account destroy`

- Jelentkezzen be a PlatformIO-fiókjába:

`pio account login --username {{username}} --password {{password}}`

- Kijelentkezés a PlatformIO-fiókból:

`pio account logout`

- PlatformIO profiljának frissítése:

`pio account update --username {{username}} --email {{email}} --firstname {{firstname}} --lastname {{lastname}} --current-password {{password}}`

- Részletes információk megjelenítése PlatformIO-fiókjáról:

`pio account show`

- Jelszó-visszaállítás a felhasználónév vagy az e-mail cím használatával:

`pio account forgot --username {{username_or_email}}`

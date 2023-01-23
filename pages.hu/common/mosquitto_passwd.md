# mosquitto_passwd

> Jelszófájlok kezelése a mosquitto számára. Lásd még: `mosquitto`, az MQTT szerver, amelyet ez kezel. További információ: <https://mosquitto.org/man/mosquitto_passwd-1.html>.

- Új felhasználó hozzáadása egy jelszófájlhoz (a jelszó megadására szólít fel):

`mosquitto_passwd {{path/to/password_file}} {{username}}`

- Létrehozza a jelszófájlt, ha még nem létezik:

`mosquitto_passwd -c {{path/to/password_file}} {{username}}`

- Ehelyett törli a megadott felhasználónevet:

`mosquitto_passwd -D {{path/to/password_file}} {{username}}`

- Egy régi egyszerű szöveges jelszófájl frissítése hashed jelszófájlra:

`mosquitto_passwd -U {{path/to/password_file}}`

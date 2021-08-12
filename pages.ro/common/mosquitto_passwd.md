# mosquitto_passwd

> Gestionați fișierele de parolă pentru țânțar.
> A se vedea, de asemenea, `tantit`, serverul MQTT care gestionează acest lucru.
> Mai multe informaţii: <https://mosquitto.org/man/mosquitto_passwd-1.html>

- Adăugați un utilizator nou la un fișier de parolă (vă va solicita să introduceți parola):

`mosquitto_passwd {{path/to/password_file}} {{username}}`

- Creați fișierul parolă dacă acesta nu există deja:

`mosquitto_passwd -c {{path/to/password_file}} {{username}}`

- Ștergeți numele de utilizator specificat în schimb:

`mosquitto_passwd -D {{path/to/password_file}} {{username}}`

- Upgrade-ul unui vechi fișier de parolă simplu text la un fișier de parolă hash:

`mosquitto_passwd -U {{path/to/password_file}}`

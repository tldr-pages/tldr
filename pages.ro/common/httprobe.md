# httprobe

> Luați o listă de domenii și sonde pentru serverele HTTP și HTTPS.
> Mai multe informaţii: <https://github.com/tomnomnom/httprobe>

- Proba o listă de domenii dintr-un fișier text:

`cat {{input_file}} | httprobe`

- Verificați numai pentru HTTP dacă HTTPS nu funcționează:

`cat {{input_file}} | httprobe --prefer-https`

- Sonde porturi suplimentare cu un anumit protocol:

`cat {{input_file}} | httprobe -p {{https:2222}}`

- Ieșire toate opțiunile disponibile:

`httprobe --help`

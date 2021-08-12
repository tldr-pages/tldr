# mailx

> Trimiteți și primiți corespondență.

- Trimiteți poșta (conținutul trebuie tastat după comandă și se termină cu `Ctrl+D`):

`mailx -s "{{subject}}" {{to_addr}}`

- Trimiteți e-mail cu conținut trecut de la o altă comandă:

`echo "{{content}}" | mailx -s "{{subject}}" {{to_addr}}`

- Trimiteți e-mail cu conținut citit dintr-un fișier:

`mailx -s "{{subject}}" {{to_addr}} < {{content.txt}}`

- Trimite e-mail la un destinatar și CC la o altă adresă:

`mailx -s "{{subject}}" -c {{cc_addr}} {{to_addr}}`

- Trimite e-mail specificând adresa expeditorului:

`mailx -s "{{subject}}" -r {{from_addr}} {{to_addr}}`

- Trimiteți e-mail cu un atașament:

`mailx -a {{file}} -s "{{subject}}" {{to_addr}}`

# sendmail

> Trimiteți mesaje de e-mail din linia de comandă.

- Trimiteți un mesaj cu conținutul `message.txt` în directorul de poștă electronică al utilizatorului local `username`:

`sendmail {{username}} < {{message.txt}}`

- Trimiteți un e-mail de la you@yourdomain.com (presupunând că serverul de e-mail este configurat pentru aceasta) către test@gmail.com care conține mesajul în `message.txt`:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}`

- Trimiteți un e-mail de la you@yourdomain.com (presupunând că serverul de poștă electronică este configurat pentru aceasta) către test@gmail.com care conține fișierul `file.zip`:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}`

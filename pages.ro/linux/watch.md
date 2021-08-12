# watch

> Executați o comandă în mod repetat și monitorizați ieșirea în modul ecran complet.

- Monitor fișiere în directorul curent:

`watch {{ls}}`

- Monitorizați spațiul pe disc și evidențiați modificările:

`watch -d {{df}}`

- Monitorizați procesele „nod”, reîmprospătând la fiecare 3 secunde:

`watch -n {{3}} "{{ps aux | grep node}}"`

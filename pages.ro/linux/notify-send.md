# notify-send

> Utilizează sistemul de notificare al mediului desktop curent pentru a crea o notificare.

- Afișați o notificare cu titlul „Test” și conținutul „Acesta este un test”:

`notify-send "{{Test}}" "{{This is a test}}"`

- Afișează o notificare cu o pictogramă personalizată:

`notify-send -i {{icon.png}} "{{Test}}" "{{This is a test}}"`

- Afișați o notificare timp de 5 secunde:

`notify-send -t 5000 "{{Test}}" "{{This is a test}}"`

- Afișează o notificare cu pictograma unei aplicații:

`notify-send "{{Test}}" --icon={{google-chrome}}`

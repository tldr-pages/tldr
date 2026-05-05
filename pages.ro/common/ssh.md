# ssh

> Secure Shell este un protocol folosit pentru a te conecta în siguranță la sisteme la distanță.
> Poate fi folosit pentru autentificare sau pentru a rula comenzi pe un server la distanță.
> Mai multe informații: <https://man.openbsd.org/ssh>.

- Conectare la un server la distanță:

`ssh {{nume_utilizator}}@{{server_distant}}`

- Conectare la un server la distanță cu o [i]dentitate specifică (cheie privată):

`ssh -i {{cale/către/fișier_cheie}} {{nume_utilizator}}@{{server_distant}}`

- Conectare la un server la distanță cu IP-ul `10.0.0.1` folosind un [p]ort specific (Notă: `10.0.0.1` poate fi scurtat la `10.1`):

`ssh {{nume_utilizator}}@10.0.0.1 -p {{2222}}`

- Rulează o comandă pe un server la distanță cu alocare [t]ty pentru a permite interacțiunea cu comanda:

`ssh {{nume_utilizator}}@{{server_distant}} -t {{comandă}} {{argumente_comandă}}`

- Tunelare SSH: redirecționare [D]inamică de port (proxy SOCKS pe `localhost:1080`):

`ssh -D {{1080}} {{nume_utilizator}}@{{server_distant}}`

- Tunelare SSH: redirecționează un port specific (`localhost:9999` către `example.org:80`) dezactivând alocarea de pseudo-[T]ty și execuți[N]a comenzilor la distanță:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{nume_utilizator}}@{{server_distant}}`

- Salt SSH ([J]umping): conectare printr-un jumphost către un server la distanță (mai multe salturi pot fi specificate separate prin virgulă):

`ssh -J {{nume_utilizator}}@{{jump_host}} {{nume_utilizator}}@{{server_distant}}`

- Închide o sesiune blocată:

`<Enter><~><.>`

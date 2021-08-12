# socat

> Releu multifuncțional (Socket CAT).

- Ascultați un port, așteptați o conexiune de intrare și transferați date către STDIO:

`socat - TCP-LISTEN:8080,fork`

- Creați o conexiune la o gazdă și port, transferați date în STDIO la gazda conectată:

`socat - TCP4:www.example.com:80`

- Redirecționați datele de intrare ale unui port local către o altă gazdă și port:

`socat TCP-LISTEN:80,fork TCP4:www.example.com:80`

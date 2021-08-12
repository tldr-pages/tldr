# uncrustify

> C, C++, C#, D, Java și formator de cod sursă pion.
> Mai multe informaţii: <https://github.com/uncrustify/uncrustify>

- Formatarea unui singur fișier:

`uncrustify -f {{path/to/file.cpp}} -o {{path/to/output.cpp}}`

- Citiți numele fișierelor din stdin și faceți copii de rezervă înainte de a scrie ieșirea înapoi la căile de fișiere originale:

`find . -name "*.cpp" | uncrustify -F - --replace`

- Nu faceți copii de rezervă (utile dacă fișierele sunt sub controlul versiunii):

`find . -name "*.cpp" | uncrustify -F - --no-backup`

- Utilizați un fișier de configurare personalizat și scrieți rezultatul la stdout:

`uncrustify -c {{path/to/uncrustify.cfg}} -f {{path/to/file.cpp}}`

- Setați în mod explicit valoarea unei variabile de configurare:

`uncrustify --set {{option}}={{value}}`

- Generați un nou fișier de configurare:

`uncrustify --update-config -o {{path/to/new.cfg}}`

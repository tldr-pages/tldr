# zmv

> Mutați sau redenumiți fișiere care corespund unui model glob extins specificat.
> A se vedea, de asemenea, `zcp` și `zln`.
> Mai multe informaţii: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>

- Mutați fișierele utilizând un model obișnuit de expresie:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- Previzualizați rezultatul unei mutări, fără a efectua modificări efective:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Mutarea interactivă a fișierelor, cu o solicitare înainte de fiecare modificare:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- Tipăriți verbosely fiecare acțiune în timp ce este executată:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`

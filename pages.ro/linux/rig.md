# rig

> Utilitate pentru a pune împreună un nume aleator, nume de familie, numărul străzii și adresa, împreună cu un punct de vedere geografic coerent (adică, toate se potrivesc cu aceeași zonă) oraș, stat, cod poștal, și prefixul.
> Mai multe informaţii: <https://manpages.ubuntu.com/manpages/focal/man6/rig.6.html>

- Afișează un nume aleatoriu (bărbat sau femeie) și adresa:

`rig`

- Afișează un nume și o adresă aleatoare [m] ale (sau [f] emale):

`rig -{{m|f}}`

- Utilizați fișiere de date dintr-un anumit director (implicit este `/usr/share/rig`):

`rig -d {{path/to/directory}}`

- Afișează un anumit număr de identități:

`rig -c {{number}}`

- Afișează un anumit număr de identități feminine:

`rig -f -c {{number}}`

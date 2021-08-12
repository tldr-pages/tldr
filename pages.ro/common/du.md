# du

> Utilizare disc: estimați și rezumați utilizarea spațiului de fișiere și director.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/du>

- Listați dimensiunile unui director și orice subdirectoare, în unitatea dată (B/KB/MB):

`du -{{b|k|m}} {{path/to/directory}}`

- Listați dimensiunile unui director și ale oricăror subdirectoare, în formă lizibilă de om (adică selectarea automată a unității corespunzătoare pentru fiecare dimensiune):

`du -h {{path/to/directory}}`

- Arată dimensiunea unui singur director, în unități lizibile umane:

`du -sh {{path/to/directory}}`

- Listați dimensiunile care pot fi citite de om ale unui director și ale tuturor fișierelor și directoarelor din acesta:

`du -ah {{path/to/directory}}`

- Listați dimensiunile lizibile de om ale unui director și orice subdirectoare, până la nivelurile N adâncime:

`du -h --max-depth=N {{path/to/directory}}`

- Listați dimensiunea lizibilă de om a tuturor fișierelor `.jpg` din subdirectoarele directorului curent și afișați un total cumulativ la sfârșit:

`du -ch */*.jpg`

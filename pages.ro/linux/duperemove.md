# duperemove

> Găsește extinderile duplicate ale sistemului de fișiere și, opțional, le programează pentru eliminarea duplicatelor.
> O măsură este o parte mică a unui fișier din interiorul sistemului de fișiere.
> Pe unele sisteme de fișiere o măsură poate fi menționată de mai multe ori, când părți ale conținutului fișierelor sunt identice.
> Mai multe informaţii: <https://markfasheh.github.io/duperemove/>

- Căutați extinderile duplicate într-un director și arătați-le:

`duperemove -r {{path/to/directory}}`

- Eliminarea duplicatelor extents pe un sistem de fișiere Btrfs sau XFS (experimental):

`duperemove -r -d {{path/to/directory}}`

- Utilizați un fișier hash pentru a stoca hash-uri de măsură (mai puțin de utilizare a memoriei și poate fi reutilizat pe rulări ulterioare):

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- Limita I/O fire (pentru hash și etapa dedupe) și fire CPU (pentru etapa de constatare duplicat măsură):

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{N}} --cpu-threads={{N}} {{path/to/directory}}`

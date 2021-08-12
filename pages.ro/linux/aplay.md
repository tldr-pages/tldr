# aplay

> Player de sunet în linie de comandă pentru driverul de placă de sunet ALSA.
> Mai multe informaţii: <https://manned.org/aplay>

- Redați un anumit fișier (rata de eșantionare, adâncimea de biți etc. vor fi determinate automat pentru formatul fișierului):

`aplay {{path/to/file}}`

- Redați primele 10 secunde ale unui anumit fișier la 2500Hz:

`aplay --duration={{10}} --rate={{2500}} {{path/to/file}}`

- Redați fișierul brut ca fișier 22050Hz, mono, 8 biți, Mu-Law `.au`:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{path/to/file}}`

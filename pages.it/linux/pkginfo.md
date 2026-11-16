# pkginfo

> Interroga il database dei pacchetti su un sistema CRUX.
> Maggiori informazioni: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- Elenca i pacchetti installati e le loro versioni:

`pkginfo {{[-i|--installed]}}`

- Elenca i file posseduti da un pacchetto:

`pkginfo {{[-l|--list]}} {{pacchetto}}`

- Elenca i proprietari di file corrispondenti a un pattern:

`pkginfo {{[-o|--owner]}} {{pattern}}`

- Stampa l'impronta di un file:

`pkginfo -f {{percorso/del/file}}`

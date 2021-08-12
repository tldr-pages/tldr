# pgrep

> Găsirea sau semnalizarea proceselor după nume.
> Mai multe informaţii: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>

- Returnați PID-urile oricăror procese care rulează cu un șir de comandă care se potrivește:

`pgrep {{process_name}}`

- Căutați procese, inclusiv opțiunile lor de linie de comandă:

`pgrep --full "{{process_name}} {{parameter}}"`

- Căutați procese rulate de un anumit utilizator:

`pgrep --euid root {{process_name}}`

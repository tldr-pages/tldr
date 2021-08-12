# lvextend

> Măriți dimensiunea unui volum logic.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvextend.8.html>

- Măriți dimensiunea unui volum la 120GB:

`lvextend --size {{120G}} {{logical_volume}}`

- Măriți dimensiunea unui volum cu 40GB, precum și sistemul de fișiere subiacent:

`lvextend --size +{{40G}} -r {{logical_volume}}`

- Măriți dimensiunea unui volum la 100% din spațiul liber al volumului fizic:

`lvextend --size {{100}}%FREE {{logical_volume}}`

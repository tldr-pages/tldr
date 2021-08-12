# lvreduce

> Reduceți dimensiunea unui volum logic.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvreduce.8.html>

- Reduceți dimensiunea unui volum la 120GB:

`lvreduce --size {{120G}} {{logical_volume}}`

- Reduceți dimensiunea unui volum cu 40GB, precum și sistemul de fișiere subiacent:

`lvreduce --size -{{40G}} -r {{logical_volume}}`

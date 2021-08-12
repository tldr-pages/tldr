# lvresize

> Modificați dimensiunea unui volum logic.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvresize.8.html>

- Modificați dimensiunea unui volum logic la 120GB:

`lvresize --size {{120G}} {{volume_group}}/{{logical_volume}}`

- Extindeți dimensiunea unui volum logic, precum și sistemul de fișiere subiacent cu 120GB:

`lvresize --size +{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

- Extindeți dimensiunea unui volum logic la 100% din spațiul liber al volumului fizic:

`lvresize --size {{100}}%FREE {{volume_group}}/{{logical_volume}}`

- Reduceți dimensiunea unui volum logic, precum și sistemul de fișiere subiacent cu 120GB:

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

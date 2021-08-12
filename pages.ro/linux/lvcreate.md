# lvcreate

> Creează un volum logic într-un grup de volum existent. Un grup de volum este o colecție de volume logice și fizice.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvcreate.8.html>

- Creați un volum logic de 10 gigaocteți în grupul de volum vg1:

`lvcreate -L {{10G}} {{vg1}}`

- Creați un volum logic liniar de 1500 megabyte numit mylv în grupul de volum vg1:

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- Creați un volum logic numit mylv care utilizează 60% din spațiul total din grupul de volum vg1:

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- Creați un volum logic numit mylv care utilizează tot spațiul nealocat din grupul de volum vg1:

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`

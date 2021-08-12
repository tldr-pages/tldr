# vgcreate

> Creați grupuri de volum care combină mai multe dispozitive de stocare în masă.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/vgcreate.8.html>

- Creați un nou grup de volum numit vg1 utilizând dispozitivul `/dev/sda1`:

`vgcreate {{vg1}} {{/dev/sda1}}`

- Creați un nou grup de volum numit vg1 utilizând mai multe dispozitive:

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`

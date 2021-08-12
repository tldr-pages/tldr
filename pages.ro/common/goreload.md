# goreload

> Live reload utilitar pentru programele Go.
> Mai multe informaţii: <https://github.com/acoshift/goreload>

- Setați numele fișierului binar pentru a viziona (implicit la `.goreload`):

`goreload -b {{path/to/binary}} {{file}}.go`

- Setați un prefix de jurnal personalizat (implicit la `goreload`):

`goreload --logPrefix {{prefix}} {{file}}.go`

- Reîncărcați ori de câte ori orice fișier se schimbă:

`goreload --all`

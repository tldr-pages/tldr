# f3probe

> Szondázzon meg egy blokkos eszközt (pl. egy flash meghajtót vagy egy microSD-kártyát) hamisított flashmemória után. Lásd még: `f3read`, `f3write`, `f3fix`. További információ: <https://github.com/AltraMayor/f3>.

- Szondázzon meg egy blokkos eszközt:

`sudo f3probe {{path/to/block_device}}`

- Használja a lehető legkevesebb RAM-ot:

`sudo f3probe --min-memory {{path/to/block_device}}`

- Időzítse a lemezműveleteket:

`sudo f3probe --time-ops {{path/to/block_device}}`

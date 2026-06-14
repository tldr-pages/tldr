# xz

> Սեղմեք կամ ապասեղմեք XZ և LZMA ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xz>:.

- Կոմպրես ֆայլը XZ ձևաչափով.:

`xz {{path/to/file}}`

- Ապասեղմեք XZ ֆայլը.:

`xz {{[-d|--decompress]}} {{path/to/file.xz}}`

- Կոմպրես ֆայլը օգտագործելով lzma:

`xz {{[-F|--format]}} lzma {{path/to/file}}`

- Ապասեղմեք LZMA ֆայլը.:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{path/to/file.lzma}}`

- Ապասեղմեք ֆայլը և գրեք `stdout` (ենթադրում է `--keep`):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{path/to/file.xz}}`

- Սեղմեք ֆայլը, բայց մի ջնջեք բնօրինակը.:

`xz {{[-k|--keep]}} {{path/to/file}}`

- Սեղմեք ֆայլը՝ օգտագործելով ամենաարագ սեղմումը.:

`xz -0 {{path/to/file}}`

- Սեղմեք ֆայլը, օգտագործելով լավագույն սեղմումը.:

`xz -9 {{path/to/file}}`

# ppmtoilbm

> Փոխարկել PPM պատկերը ILBM ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtoilbm.html>:.

- Փոխարկել PPM պատկերը ILBM ֆայլի.:

`ppmtoilbm {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- ILBM ֆայլում գրեք առավելագույնը `n` հարթություն և ստեղծեք HAM/24bit/ուղղակի գունավոր ֆայլ, եթե այս թիվը գերազանցվի.:

`ppmtoilbm {{[-mp|-maxplanes]}} {{n}} -{{hamif|24if|dcif}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- Ստեղծեք ILBM ֆայլ հենց `n` հարթություններով.:

`ppmtoilbm {{[-fp|-fixplanes]}} {{n}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

- Ընտրեք սեղմման մեթոդը, որը պետք է օգտագործվի.:

`ppmtoilbm -{{compress|nocompress|savemem}} {{path/to/file.ppm}} > {{path/to/file.ilbm}}`

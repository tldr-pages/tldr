# pnmtoxwd

> Փոխարկեք PNM ֆայլը X11 պատուհանի աղբանոց ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtoxwd.html>:.

- Փոխարկել PNM պատկերի ֆայլը XWD:

`pnmtoxwd {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- Արտադրեք արդյունքը DirectColor ձևաչափով.:

`pnmtoxwd {{[-d|-directcolor]}} {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- Սահմանեք ելքի գույնի խորությունը b բիթ.:

`pnmtoxwd {{[-ps|-pseudodepth]}} {{b}} {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

# pnmreap

> Փոխարինեք գույները PNM պատկերում:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmremap.html>:.

- Փոխարինեք պատկերի գույները նշված գույների գունապնակով.:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Օգտագործեք Floyd-Steinberg dithering-ը գունային գունապնակում բացակայող գույները ներկայացնելու համար.:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-fs|-floyd]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Գունապնակում բացակայող գույները ներկայացնելու համար օգտագործեք գունապնակում առաջին գույնը.:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-fi|-firstisdefault]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Օգտագործեք նշված գույնը գունային գունապնակում բացակայող գույները ներկայացնելու համար.:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-m|-missingcolor]}} {{color}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

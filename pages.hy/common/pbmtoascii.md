# pbmtoascii

> Փոխարկել PBM պատկերը ASCII գրաֆիկայի:.
> Տես նաև՝ `ppmtoascii`, `asciitopgm`, `ppmtoterm`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtoascii.html>:.

- Կարդացեք PBM ֆայլը որպես մուտքագրում և արտադրեք ASCII ելք.:

`pbmtoascii {{path/to/input_file.pbm}}`

- Կարդացեք PBM ֆայլը որպես մուտքագրում և պահեք ASCII ելքը ֆայլի մեջ.:

`pbmtoascii {{path/to/input_file.pbm}} > {{path/to/output_file}}`

- Կարդացեք PBM ֆայլը որպես մուտքագրում՝ պիքսելային քարտեզագրումը սահմանելիս (կանխադրված է 1x2):

`pbmtoascii -{{1x2|2x4}} {{path/to/input_file.pbm}}`

- Ցուցադրման տարբերակը:

`pbmtoascii {{[-v|-version]}}`

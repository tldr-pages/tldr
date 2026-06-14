# pamtotiff

> Փոխարկել PAM պատկերը TIFF ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamtotiff.html>:.

- Փոխակերպեք PAM պատկերը TIFF պատկերի.:

`pamtotiff {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`

- Հստակորեն նշեք ելքային ֆայլի սեղմման մեթոդը.:

`pamtotiff -{{none|packbits|lzw|g3|g4|flate|adobeflate}} {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`

- Միշտ ստեղծեք գունավոր TIFF պատկեր, նույնիսկ եթե մուտքագրված պատկերը մոխրագույն է.:

`pamtotiff {{[-c|-color]}} {{path/to/input_file.pam}} > {{path/to/output_file.tiff}}`

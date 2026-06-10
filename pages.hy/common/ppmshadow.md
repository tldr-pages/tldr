# ppmshadow

> Ավելացրեք նմանակված ստվերներ PPM պատկերին:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmshadow.html>:.

- Մոդելացված ստվերներ ավելացրեք PPM պատկերին.:

`ppmshadow {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- [b]պատկերը խեղդել նշված թվով պիքսելներով.:

`ppmshadow -b {{n}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

- Նշեք մոդելավորված լույսի աղբյուրի տեղաշարժը պատկերի ձախ և վերևում.:

`ppmshadow -x {{left_offset}} -y {{top_offset}} {{path/to/input_file.ppm}} > {{path/to/output_file.ppm}}`

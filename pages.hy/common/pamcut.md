# pamcut

> Netpbm պատկերից կտրեք ուղղանկյուն հատված:.
> Տես նաև՝ `pamdice`, `pamcomp`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamcut.html>:.

- Վերացրեք պատկերի յուրաքանչյուր կողմում նշված թվով սյունակներ/տողեր.:

`pamcut {{[-cropl|-cropleft]}} {{value}} {{[-cropr|-cropright]}} {{value}} {{[-cropt|-croptop]}} {{value}} {{[-cropb|-cropbottom]}} {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Պահպանեք միայն սյունակները նշված սյունակների միջև (ներառյալ).:

`pamcut {{[-l|-left]}} {{value}} {{[-ri|-right]}} {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Լրացրեք բացակայող տարածքները սև պիքսելներով, եթե նշված ուղղանկյունն ամբողջությամբ չի գտնվում մուտքագրված պատկերի մեջ.:

`pamcut {{[-t|-top]}} {{value}} {{[-b|-bottom]}} {{value}} -pad {{path/to/image.ppm}} > {{path/to/output.ppm}}`

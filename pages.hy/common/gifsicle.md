#գիֆսիկլ

> Ստեղծեք, խմբագրեք, շահարկեք և տեղեկություններ ստացեք GIF ֆայլերի մասին:.
> Լրացուցիչ տեղեկություններ. <https://www.lcdf.org/gifsicle/>:.

- Օպտիմիզացրեք GIF-ը որպես նոր ֆայլ.:

`gifsicle {{path/to/input.gif}} {{[-O|--optimize=]}}3 {{[-o|--output]}} {{path/to/output.gif}}`

- Օգտագործեք խմբաքանակի ռեժիմ (փոփոխեք յուրաքանչյուր ֆայլ տեղում) և ապաօպտիմիզացրեք GIF-ը.:

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} {{[-U|--unoptimize]}}`

- Քաղեք շրջանակը GIF-ից.:

`gifsicle {{path/to/input.gif}} '#{{0}}' > {{path/to/first_frame.gif}}`

- Ստեղծեք GIF անիմացիա ընտրված GIF-ներից.:

`gifsicle {{*.gif}} {{[-d|--delay]}} {{10}} {{[-l|--loop]}} > {{path/to/output.gif}}`

- Նվազեցրեք ֆայլի չափը, օգտագործելով կորուստների սեղմումը.:

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} {{[-O|--optimize=]}}3 --lossy={{100}} {{[-k|--colors]}} {{16}} {{[-f|--dither]}}`

- Ջնջեք առաջին 10 կադրերը և 20-րդ շրջանակից հետո բոլոր կադրերը GIF-ից.:

`gifsicle {{[-b|--batch]}} {{path/to/input.gif}} --delete '#{{0-9}}' '#{{20-}}'`

- Փոփոխեք բոլոր շրջանակները՝ կտրելով դրանք ուղղանկյունի, փոխելով դրանց մասշտաբները, շրջելով և պտտելով դրանք.:

`gifsicle {{[-b|--batch]}} --crop {{starting_x}},{{starting_y}}+{{rect_width}}x{{rect_height}} --scale {{0.25}} --flip-horizontal --rotate-{{90|180|270}} {{path/to/input.gif}}`

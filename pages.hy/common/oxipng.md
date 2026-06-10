# oxipng

> Անկորուստ բարելավել PNG ֆայլերի սեղմումը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/oxipng>:.

- Սեղմեք PNG ֆայլը (լռելյայն վերագրանցում է ֆայլը).:

`oxipng {{path/to/file.png}}`

- Սեղմեք PNG ֆայլը և ելքը պահեք նոր ֆայլում.:

`oxipng --out {{path/to/output.png}} {{path/to/file.png}}`

- Սեղմեք բոլոր PNG ֆայլերը ընթացիկ գրացուցակում, օգտագործելով բազմաթիվ թելեր.:

`oxipng "*.png"`

- Սեղմեք ֆայլը սահմանված օպտիմալացման մակարդակով (կանխադրվածը 2 է):

`oxipng {{[-o|--opt]}} {{0|1|2|3|4|5|6|max}} {{path/to/file.png}}`

- Սահմանեք PNG interlacing տեսակը (`off`-ը հեռացնում է interlacing-ը, `on`-ը կիրառում է Adam7 interlacing, `keep` պահպանում է գոյություն ունեցող interlacing. լռելյայն `off`):

`oxipng {{[-i|--interlace]}} {{off|on|keep}} {{path/to/file.png}}`

- Կատարեք լրացուցիչ օպտիմիզացում ալֆա ալիքով պատկերների վրա.:

`oxipng {{[-a|--alpha]}} {{path/to/file.png}}`

- Օգտագործեք շատ ավելի դանդաղ, բայց ավելի ուժեղ Zopfli կոմպրեսորը առավելագույն օպտիմալացումով.:

`oxipng {{[-z|--zopfli]}} {{[-o|--opt]}} max {{path/to/file.png}}`

- Հեռացրեք բոլոր ոչ կարևոր մետատվյալների կտորները.:

`oxipng --strip all {{path/to/file.png}}`

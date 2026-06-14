# ascii-image-converter

> Փոխակերպեք պատկերը ASCII-ի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/TheZoraiz/ascii-image-converter#cli-usage>:.

- Փոխակերպեք պատկերը ASCII-ի.:

`ascii-image-converter {{path/to/image|url}}`

- Գունավորեք ելքը.:

`ascii-image-converter {{[-C|--color]}} {{path/to/image|url}}`

- Ստեղծեք շեղված պատկեր՝ օգտագործելով Բրայլը (եթե պատկերը հազիվ տեսանելի է, փորձեք փոխել տերմինալի տառատեսակը).:

`ascii-image-converter {{[-b|--braille]}} {{path/to/image|url}}`

- Ստեղծեք շեղված պատկեր՝ օգտագործելով Բրայլը (եթե պատկերը հազիվ տեսանելի է, փորձեք փոխել տերմինալի տառատեսակը).:

`ascii-image-converter {{[-b|--braille]}} --dither {{path/to/image|url}}`

- Ցուցադրել պատկերը բացասական գույներով.:

`ascii-image-converter {{[-Cn|--color --negative]}} {{path/to/image|url}}`

- Պատկերը ցուցադրելու համար օգտագործեք նիշերի ավելի լայն շրջանակ (կարող է բարելավել պատկերի ճշգրտությունը).:

`ascii-image-converter {{[-c|--complex]}} {{path/to/image|url}}`

#լպր

> Տպել ֆայլերը:.
> Տես նաև՝ `lpstat`, `lpadmin`:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-lpr.html>:.

- Տպել ֆայլը լռելյայն տպիչի մեջ.:

`lpr {{path/to/file}}`

- Տպել 2 օրինակ.:

`lpr -# {{2}} {{path/to/file}}`

- Տպել անունով տպիչի վրա.:

`lpr -P {{printer}} {{path/to/file}}`

- Տպել կամ մեկ էջ (օրինակ՝ 2) կամ մի շարք էջեր (օրինակ՝ 2-16):

`lpr -o page-ranges={{2|2-16}} {{path/to/file}}`

- Տպեք երկկողմանի կամ դիմանկարային (երկար) կամ լանդշաֆտային (կարճ).:

`lpr -o sides={{two-sided-long-edge|two-sided-short-edge}} {{path/to/file}}`

- Սահմանեք էջի չափը (կախված կարգավորումից կարող են հասանելի լինել ավելի շատ տարբերակներ).:

`lpr -o media={{a4|letter|legal}} {{path/to/file}}`

- Տպել մի քանի էջ մեկ թերթիկի համար.:

`lpr -o number-up={{2|4|6|9|16}} {{path/to/file}}`

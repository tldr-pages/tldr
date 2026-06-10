#նկ

> Նկարների նախնական պրոցեսոր groff (GNU Troff) փաստաթղթերի ձևաչափման համակարգի համար:.
> Տես նաև՝ `groff`, `troff`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pic>:.

- Ընթացակարգի մուտքագրումը նկարներով՝ պահպանելով ելքը հետագա շարադրման համար գրոֆով PostScript-ում.:

`pic {{path/to/input.pic}} > {{path/to/output.roff}}`

- Մուտքագրեք նկարներով մուտքագրումը PDF-ին՝ օգտագործելով [me] մակրո փաթեթը.:

`pic -T {{pdf}} {{path/to/input.pic}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`

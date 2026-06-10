# թբ

> Աղյուսակի նախնական պրոցեսոր groff (GNU Troff) փաստաթղթերի ձևաչափման համակարգի համար:.
> Տես նաև՝ `groff`, `troff`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/tbl>:.

- Գործընթացի մուտքագրումը աղյուսակներով՝ պահպանելով ելքը հետագա շարադրման համար գրոֆով PostScript-ում:

`tbl {{path/to/input_file}} > {{path/to/output.roff}}`

- Տիպեք մուտքագրումը աղյուսակներով PDF-ում, օգտագործելով [me] մակրո փաթեթը.:

`tbl -T {{pdf}} {{path/to/input.tbl}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`

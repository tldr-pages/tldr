#բռնակ

> Գրաֆֆ (GNU Troff) փաստաթղթերի ձևաչափման համակարգի գծագրման նախնական պրոցեսոր:.
> Տես նաև՝ `pic`, `groff`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/grap>:.

- Մշակեք `grap` ֆայլը և պահեք ելքային ֆայլը հետագա մշակման համար `pic` և `groff`-ով:

`grap {{path/to/input.grap}} > {{path/to/output.pic}}`

- Մուտքագրեք `grap` ֆայլը PDF-ի՝ օգտագործելով [me] մակրոփաթեթը՝ ելքը պահելով ֆայլում՝:

`grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`

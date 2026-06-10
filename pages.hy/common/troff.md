# troff

> Գրաֆֆ (GNU Troff) փաստաթղթերի ձևաչափման համակարգի համար տեքստային պրոցեսոր:.
> Տես նաև՝ `groff`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/troff>:.

- Ձևաչափեք ելքը PostScript տպիչի համար՝ ելքը պահելով ֆայլում.:

`troff {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- Ձևաչափեք ելքը PostScript տպիչի համար՝ օգտագործելով me մակրո փաթեթը՝ ելքը պահելով ֆայլում.:

`troff -{{me}} {{path/to/input.roff}} | grops > {{path/to/output.ps}}`

- Ձևաչափեք ելքը որպես ASCII տեքստ՝ օգտագործելով մարդ մակրո փաթեթը.:

`troff -T {{ascii}} -{{man}} {{path/to/input.roff}} | grotty`

- Ձևաչափեք ելքը որպես pdf ֆայլ՝ ելքը պահելով ֆայլում.:

`troff -T {{pdf}} {{path/to/input.roff}} | gropdf > {{path/to/output.pdf}}`

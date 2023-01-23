# exrex

> Generálja az összes/véletlenszerű egyező karakterláncokat egy reguláris kifejezéshez. Egyszerűsítheti a reguláris kifejezéseket. További információ: <https://github.com/asciimoo/exrex>.

- Az összes lehetséges karakterlánc generálása, amely megfelel egy reguláris kifejezésnek:

`exrex '{{regular_expression}}'`

- Egy reguláris kifejezésnek megfelelő véletlenszerű karakterlánc generálása:

`exrex --random '{{regular_expression}}'`

- Legfeljebb 100 olyan karakterlánc generálása, amely megfelel egy reguláris kifejezésnek:

`exrex --max-number {{100}} '{{regular_expression}}'`

- Az összes lehetséges karakterlánc generálása, amely megfelel egy reguláris kifejezésnek, egy egyéni elválasztó karakterlánccal összekötve:

`exrex --delimiter "{{, }}" '{{regular_expression}}'`

- A szabályos kifejezésnek megfelelő összes lehetséges karakterlánc számának kiírása:

`exrex --count '{{regular_expression}}'`

- A reguláris kifejezés egyszerűsítése:

`exrex --simplify '{{ab|ac}}'`

- Szemek nyomtatása:

`exrex '{{[oO0](_)[oO0]}}'`

- Hajó nyomtatása:

`exrex '{{( {20}(\| *\\|-{22}|\|)|\.={50}| ( ){0,5}\\\.| {12}~{39})}}'`

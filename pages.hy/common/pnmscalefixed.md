# pnmscale ամրագրված է

> Սանդղակավորեք PNM ֆայլը արագ՝ հնարավոր ցածր որակով:.
> Տես նաև՝ `pamscale`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmscalefixed.html>:.

- Սանդղակավորեք պատկերն այնպես, որ արդյունքը ունենա նշված չափերը.:

`pnmscalefixed {{[-w|-width]}} {{width}} {{[-h|-height]}} {{height}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Սանդղակավորեք պատկերն այնպես, որ արդյունքը ունենա նշված լայնությունը՝ պահպանելով կողմի հարաբերակցությունը.:

`pnmscalefixed {{[-w|-width]}} {{width}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Սանդղակավորեք պատկերն այնպես, որ դրա լայնությունը և բարձրությունը փոխվեն նշված գործոններով.:

`pnmscalefixed {{[-xsc|-xscale]}} {{x_factor}} {{[-ysc|-yscale]}} {{y_factor}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

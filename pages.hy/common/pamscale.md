# pamscale

> Սանդղակավորեք Netpbm պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamscale.html>:.

- Սանդղակավորեք պատկերն այնպես, որ արդյունքը ունենա նշված չափերը.:

`pamscale {{[-wid|-width]}} {{width}} {{[-h|-height]}} {{height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Սանդղակավորեք պատկերն այնպես, որ արդյունքը ունենա նշված լայնությունը՝ պահպանելով կողմի հարաբերակցությունը.:

`pamscale {{[-wid|-width]}} {{width}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Սանդղակավորեք պատկերն այնպես, որ դրա լայնությունը և բարձրությունը փոխվեն նշված գործոններով.:

`pamscale {{[-xsc|-xscale]}} {{x_factor}} {{[-ysc|-yscale]}} {{y_factor}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Սանդղակավորեք պատկերն այնպես, որ այն տեղավորվի նշված սահմանային վանդակում՝ պահպանելով դրա հարաբերակցությունը.:

`pamscale -xyfit {{bbox_width}} {{bbox_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Սանդղակավորեք պատկերն այնպես, որ այն ամբողջությամբ լրացնի նշված վանդակը՝ պահպանելով դրա հարաբերակցությունը.:

`pamscale -xyfill {{box_width}} {{box_height}} {{path/to/input.pam}} > {{path/to/output.pam}}`

# pngtopam

> Փոխարկել PNG պատկերը Netpbm պատկերի:.
> Տես նաև՝ `pamtopng`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pngtopam.html>:.

- Նշված PNG պատկերը փոխարկեք Netpbm պատկերի.:

`pngtopam {{path/to/image.png}} > {{path/to/output.pam}}`

- Ստեղծեք ելքային պատկեր, որը ներառում է մուտքային պատկերի և՛ հիմնական պատկերը, և՛ թափանցիկության դիմակը.:

`pngtopam -alphapam {{path/to/image.png}} > {{path/to/output.pam}}`

- Փոխարինեք թափանցիկ պիքսելները նշված գույնով.:

`pngtopam {{[-m|-mix]}} {{[-ba|-background]}} {{color}} {{path/to/image.png}} > {{path/to/output.pam}}`

- Նշված տեքստային ֆայլում գրեք մուտքագրված պատկերում հայտնաբերված տեքստի կտորները.:

`pngtopam {{[-te|-text]}} {{path/to/file.txt}} {{path/to/image.png}} > {{path/to/output.pam}}`

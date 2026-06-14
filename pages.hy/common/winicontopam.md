# winicontopam

> Վերափոխեք Windows ICO ֆայլը PAM ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/winicontopam.html>:.

- Կարդացեք ICO ֆայլը և փոխարկեք դրա մեջ պարունակվող լավագույն որակի պատկերը PAM ձևաչափի.:

`winicontopam {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- Մուտքային ֆայլի բոլոր պատկերները փոխարկեք PAM-ի.:

`winicontopam {{[-al|-allimages]}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- Մուտքային ֆայլի n'-րդ պատկերը փոխարկեք PAM-ի.:

`winicontopam {{[-i|-image]}} {{n}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

- Եթե արդյունահանվող պատկեր(ներ)ը պարունակում է թափանցիկության աստիճանավորված տվյալներ և AND դիմակ, գրեք AND դիմակը ելքային PAM ֆայլի հինգերորդ ալիքում.:

`winicontopam {{[-an|-andmasks]}} {{path/to/input_file.ico}} > {{path/to/output.pam}}`

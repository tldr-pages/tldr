# pamflip

> Շրջեք կամ պտտեք PAM կամ PNM պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pamflip.html>:.

- Պտտեք մուտքագրված պատկերը ժամացույցի սլաքի հակառակ ուղղությամբ որոշակի աստիճանի համար.:

`pamflip {{[-r|-rotate]}}{{90|180|270}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Թեքեք ձախից աջ.:

`pamflip {{[-lr|-leftright]}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Շրջեք վերևից ներքևի համար.:

`pamflip {{[-tb|-topbottom]}} {{path/to/input.pam}} > {{path/to/output.pam}}`

- Շրջեք մուտքագրված պատկերը հիմնական անկյունագծով.:

`pamflip {{[-xy|-transpose]}} {{path/to/input.pam}} > {{path/to/output.pam}}`

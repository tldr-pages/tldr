# install-tl

> TeX Live միջպլատֆորմային տեղադրող:.
> Լրացուցիչ տեղեկություններ. <https://tug.org/texlive/>:.

- Սկսեք տեքստի վրա հիմնված տեղադրիչը (կանխադրված Unix համակարգերում).:

`install-tl -no-gui`

- Սկսեք GUI տեղադրիչը (կանխադրված macOS-ում և Windows-ում, պահանջում է Tcl/Tk):

`install-tl -gui`

- Տեղադրեք TeX Live-ը, ինչպես սահմանված է հատուկ պրոֆիլային ֆայլում.:

`install-tl -profile {{path/to/texlive.profile}}`

- Սկսեք տեղադրիչը որոշակի պրոֆիլային ֆայլի կարգավորումներով.:

`install-tl -init-from-file {{path/to/texlive.profile}}`

- Գործարկեք տեղադրիչը շարժական սարքի վրա տեղադրելու համար, օրինակ՝ USB կրիչ.:

`install-tl -portable`

- Ցուցադրել օգնությունը.:

`install-tl -help`

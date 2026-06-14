# git կիրառվում է

> Կիրառեք կարկատել ֆայլերի և/կամ ինդեքսի վրա՝ առանց commit ստեղծելու:.
> Տես նաև՝ `git am`:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-apply>:.

- Տպել հաղորդագրություններ կարկատված ֆայլերի մասին.:

`git apply {{[-v|--verbose]}} {{path/to/file}}`

- Կիրառել և ավելացնել կարկատված ֆայլերը ինդեքսում.:

`git apply --index {{path/to/file}}`

- Կիրառել հեռավոր կարկատել ֆայլ.:

`curl {{[-L|--location]}} {{https://example.com/file.patch}} | git apply`

- Արտադրեք դիֆստատ մուտքի համար և կիրառեք կարկատելը.:

`git apply --stat --apply {{path/to/file}}`

- Կիրառեք կարկատակը հակառակ ուղղությամբ.:

`git apply {{[-R|--reverse]}} {{path/to/file}}`

- Պահպանեք կարկատման արդյունքը ինդեքսում՝ առանց աշխատանքային ծառը փոփոխելու.:

`git apply --cache {{path/to/file}}`

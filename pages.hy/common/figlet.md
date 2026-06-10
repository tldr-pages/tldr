# թզուկ

> Ստեղծեք ASCII պաստառներ օգտվողի մուտքագրումից:.
> Տես նաև՝ `showfigfonts`:.
> Լրացուցիչ տեղեկություններ. <https://www.figlet.org/figlet-man.html>:.

- Ստեղծեք ուղղակիորեն տեքստ մուտքագրելով.:

`figlet {{input_text}}`

- Օգտագործեք հատուկ [f]ont ֆայլ.:

`figlet -f {{path/to/font_file.flf}} {{input_text}}`

- Օգտագործեք [f]ont լռելյայն տառատեսակի գրացուցակից (ընդլայնումը կարող է բաց թողնել).:

`figlet -f {{font_filename}} {{input_text}}`

- Խողովակի հրամանի ելք FIGlet-ի միջոցով.:

`{{command}} | figlet`

- Ցույց տալ հասանելի FIGlet տառատեսակները.:

`showfigfonts {{optional_string_to_display}}`

- Օգտագործեք [t] տերմինալի ամբողջ լայնությունը և [c] մուտքագրեք մուտքագրված տեքստը.:

`figlet -t -c {{input_text}}`

- Ցուցադրել բոլոր նիշերը լրիվ [W] լայնությամբ՝ համընկնումից խուսափելու համար.:

`figlet -W {{input_text}}`

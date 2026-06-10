#հարուստ

> Գործիքների տուփ տերմինալում շքեղ արդյունքի համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Textualize/rich-cli>:.

- Ցուցադրել ֆայլ շարահյուսական ընդգծմամբ.:

`rich {{path/to/file.py}}`

- Ավելացրեք տողերի համարները և ներքևի ուղեցույցները.:

`rich {{path/to/file.py}} --line-numbers --guides`

- Կիրառել թեմա.:

`rich {{path/to/file.py}} --theme {{monokai}}`

- Ցուցադրել ֆայլը ինտերակտիվ փեյջերում.:

`rich {{path/to/file.py}} --pager`

- Ցուցադրել բովանդակությունը URL-ից.:

`rich {{https://raw.githubusercontent.com/Textualize/rich-cli/main/README.md}} --markdown --pager`

- Արտահանել ֆայլը որպես HTML:

`rich {{path/to/file.md}} --export-html {{path/to/file.html}}`

- Ցուցադրել տեքստը ֆորմատավորման պիտակներով, հարմարեցված հավասարեցմամբ և տողի լայնությամբ.:

`rich --print "{{Hello [green on black]Stylized[/green on black] [bold]World[/bold]}}" --{{left|center|right}} --width {{10}}`

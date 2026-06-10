#տարբերություն

> Համեմատեք ֆայլերը կամ գրացուցակները՝ հիմնված ծրագրավորման լեզվի շարահյուսության վրա:.
> Տես նաև՝ `delta`, `diff`:.
> Լրացուցիչ տեղեկություններ. <https://difftastic.wilfred.me.uk/introduction.html>:.

- Համեմատեք երկու ֆայլ կամ գրացուցակ.:

`difft {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Հաղորդեք միայն ֆայլերի միջև տարբերությունների առկայության մասին.:

`difft --check-only {{path/to/file1}} {{path/to/file2}}`

- Նշեք ցուցադրման ռեժիմը (կանխադրված է `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{path/to/file1}} {{path/to/file2}}`

- Անտեսեք մեկնաբանությունները համեմատելիս.:

`difft --ignore-comments {{path/to/file1}} {{path/to/file2}}`

- Միացնել/անջատել սկզբնական կոդի շարահյուսական ընդգծումը (կանխադրվածը `on` է):

`difft --syntax-highlight {{on|off}} {{path/to/file1}} {{path/to/file2}}`

- Ընդհանրապես ոչինչ մի թողարկեք, եթե ֆայլերի միջև տարբերություններ չկան.:

`difft --skip-unchanged {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Տպեք գործիքի կողմից աջակցվող բոլոր ծրագրավորման լեզուները՝ դրանց ընդլայնումների հետ միասին.:

`difft --list-languages`

# rubocop

> Lint Ruby ֆայլեր:.
> Լրացուցիչ տեղեկություններ. <https://docs.rubocop.org/rubocop/latest/usage/cli_reference.html>:.

- Ստուգեք ընթացիկ գրացուցակի բոլոր ֆայլերը (ներառյալ ենթագրքերները).:

`rubocop`

- Ստուգեք մեկ կամ ավելի կոնկրետ ֆայլեր կամ գրացուցակներ.:

`rubocop {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Արդյունք գրեք ֆայլում՝:

`rubocop --out {{path/to/file}}`

- Դիտեք ոստիկանների ցուցակը (լինտերի կանոնները).:

`rubocop --show-cops`

- Բացառել ոստիկանին.:

`rubocop --except {{cop1 cop2 ...}}`

- Գործարկել միայն նշված ոստիկանները.:

`rubocop --only {{cop1 cop2 ...}}`

- Ֆայլերի ավտոմատ ուղղում (փորձարարական).:

`rubocop --auto-correct`

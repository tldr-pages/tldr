# xgettext

> Կոդային ֆայլերից հանեք gettext տողերը:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gettext/manual/gettext.html#xgettext-Invocation>:.

- Սկանավորեք ֆայլը և ելքային տողերը `messages.po`:

`xgettext {{path/to/input_file}}`

- Օգտագործեք այլ ելքային ֆայլի անուն.:

`xgettext {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- Նոր տողեր ավելացրեք գոյություն ունեցող ֆայլին.:

`xgettext {{[-j|--join-existing]}} {{[-o|--output]}} {{path/to/output_file}} {{path/to/input_file}}`

- Ելքային ֆայլին մի ավելացրեք մետատվյալներ պարունակող վերնագիր.:

`xgettext --omit-header {{path/to/input_file}}`

- Ցուցադրել օգնությունը.:

`xgettext {{[-h|--help]}}`

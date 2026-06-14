#պր

> Տպագրման համար էջադրել կամ սյունակավոր ֆայլեր:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>:.

- Տպեք բազմաթիվ ֆայլեր լռելյայն վերնագրի և ստորագրի հետ.:

`pr {{path/to/file1 path/to/file2 ...}}`

- Տպել հատուկ կենտրոնացված վերնագրով.:

`pr {{[-h|--header]}} "{{header}}" {{path/to/file1 path/to/file2 ...}}`

- Տպել համարակալված տողերով և հատուկ ամսաթվի ձևաչափով.:

`pr {{[-n|--number-lines]}} {{[-D|--date-format]}} "{{format}}" {{path/to/file1 path/to/file2 ...}}`

- Տպեք բոլոր ֆայլերը միասին, յուրաքանչյուր սյունակում մեկը, առանց վերնագրի կամ ստորագրի:

`pr {{[-m|--merge]}} {{[-T|--omit-pagination]}} {{path/to/file1 path/to/file2 ...}}`

- Տպել՝ սկսած 2-րդ էջից մինչև 5-րդ էջը, տրված էջի երկարությամբ (ներառյալ վերնագիրն ու ստորագիրը).:

`pr +2:5 {{[-l|--length]}} {{page_length}} {{path/to/file1 path/to/file2 ...}}`

- Տպեք յուրաքանչյուր տողի օֆսեթով և հատուկ էջի ընդհատվող լայնությամբ.:

`pr {{[-o|--indent]}} {{offset}} {{[-W|--page_width]}} {{width}} {{path/to/file1 path/to/file2 ...}}`

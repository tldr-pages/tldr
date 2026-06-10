# պոչ

> Ցուցադրել ֆայլի վերջին մասը:.
> Տես նաև՝ `head`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>:.

- Ցույց տալ վերջին 10 տողերը ֆայլում.:

`tail {{path/to/file}}`

- Ցույց տալ բազմաթիվ ֆայլերի վերջին 10 տողերը.:

`tail {{path/to/file1 path/to/file2 ...}}`

- Ցույց տալ վերջին 5 տողերը ֆայլում.:

`tail {{[-5|--lines 5]}} {{path/to/file}}`

- Տպել ֆայլ որոշակի տողի համարից.:

`tail {{[-n|--lines]}} +{{count}} {{path/to/file}}`

- Տպեք բայթերի որոշակի քանակ տվյալ ֆայլի վերջից.:

`tail {{[-c|--bytes]}} {{count}} {{path/to/file}}`

- Տպեք տվյալ ֆայլի վերջին տողերը և շարունակեք կարդալ այն մինչև `<Ctrl c>`:

`tail {{[-f|--follow]}} {{path/to/file}}`

- Շարունակեք կարդալ ֆայլը մինչև `<Ctrl c>`, նույնիսկ եթե ֆայլն անհասանելի է.:

`tail {{[-F|--retry --follow]}} {{path/to/file}}`

- Ցույց տալ վերջին `count` տողերը ֆայլում և թարմացնել ամեն `seconds` վայրկյանը մեկ՝:

`tail {{[-n|--lines]}} {{count}} {{[-s|--sleep-interval]}} {{seconds}} {{[-f|--follow]}} {{path/to/file}}`

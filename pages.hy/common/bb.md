#բբ

> Native Clojure թարգմանիչ սցենարի համար:.
> Լրացուցիչ տեղեկություններ. <https://book.babashka.org/#usage>:.

- Գնահատեք արտահայտությունը.:

`bb {{[-e|--eval]}} "(+ 1 2 3)"`

- Գնահատեք սցենարի ֆայլը.:

`bb {{[-f|--file]}} {{path/to/script.clj}}`

- Կցեք [i]nput-ը `stdin`-ից տողերի հաջորդականությանը.:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Կցեք [I]nput-ը EDN (Extensible Data Notation) արժեքների հաջորդականությանը `stdin`-ից:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`

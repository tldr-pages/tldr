# bb

> Native Clojure interpreter for scripting.
> More information: <https://book.babashka.org/#usage>.

- [e]valuate an expression:

`bb -e "(+ 1 2 3)"`

- Evaluate a script [f]ile:

`bb -f {{path/to/script.clj}}`

- Bind input to a sequence of lines from stdin:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Bind input to a sequence of EDN(Extensible Data Notation) values from stdin:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`

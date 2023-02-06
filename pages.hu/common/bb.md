# bb

> Natív Clojure-értelmező szkripteléshez. További információ: <https://book.babashka.org/#usage>.

- \[e\]valuate an expression:

`bb -e "(+ 1 2 3)"`

- Egy szkript \[f\]ile kiértékelése:

`bb -f {{path/to/script.clj}}`

- Bemenet kötése az stdin-ből származó sorok sorozatához:

`printf "first\nsecond" | bb -i "(map clojure.string/capitalize *input*)"`

- Input kötése EDN(Extensible Data Notation) értékek sorozatához az stdin-ből:

`echo "{:key 'val}" | bb -I "(:key (first *input*))"`

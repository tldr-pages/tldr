# expr

> Kifejezések kiértékelése és karakterláncok manipulálása. További információ: <https://www.gnu.org/software/coreutils/expr>.

- A karakterlánc hosszának lekérdezése:

`expr length {{string}}`

- Logikai vagy matematikai kifejezés kiértékelése operátorral ('+', '-', '\*', '&', '|' stb.). A speciális szimbólumokat el kell szedni:

`expr {{first_argument}} {{operator}} {{second_argument}}`

- A "string"-ben lévő első olyan karakter pozíciójának kinyerése, amely megfelel a "substring"-nek:

`echo $(expr index {{string}} {{substring}})`

- A karakterlánc egy részének kivonása:

`echo $(expr substr {{string}} {{position_to_start}} {{number_of_characters}}`

- A karakterlánc azon részének kivonása, amely megfelel egy reguláris kifejezésnek:

`echo $(expr {{string}} : '\({{regular_expression}}\)')`

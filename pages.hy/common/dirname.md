# dirname

> Հեռացրեք ֆայլի անվանման վերջնամասը ուղուց:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>:.

- Հաշվեք տվյալ ճանապարհի մայր գրացուցակը.:

`dirname {{path/to/file_or_directory}}`

- Հաշվեք բազմաթիվ ուղիների մայր գրացուցակը.:

`dirname {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Սահմանազատեք ելքը NUL նիշով նոր տողի փոխարեն (օգտակար `xargs`-ի հետ համադրելիս):

`dirname {{[-z|--zero]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

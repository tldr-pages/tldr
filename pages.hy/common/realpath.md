# իրական ուղի

> Ցուցադրել լուծված բացարձակ ուղին ֆայլի կամ գրացուցակի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>:.

- Ցուցադրել բացարձակ ուղին ֆայլի կամ գրացուցակի համար.:

`realpath {{path/to/file_or_directory}}`

- Պահանջել, որ գոյություն ունենան ճանապարհի բոլոր բաղադրիչները.:

`realpath {{[-e|--canonicalize-existing]}} {{path/to/file_or_directory}}`

- Սիմհղումներից առաջ լուծեք `..` բաղադրիչները.:

`realpath {{[-L|--logical]}} {{path/to/file_or_directory}}`

- Անջատել symlink ընդլայնումը:

`realpath {{[-s|--no-symlinks]}} {{path/to/file_or_directory}}`

- Չեղարկել սխալի հաղորդագրությունները.:

`realpath {{[-q|--quiet]}} {{path/to/file_or_directory}}`

# շտեմարան

> Symlink կառավարիչ:.
> Հաճախ օգտագործվում է dotfiles կառավարելու համար:.
> Տես նաև՝ `chezmoi`, `tuckr`, `vcsh`, `homeshick`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/stow/manual/stow.html#Invoking-Stow>:.

- Բոլոր ֆայլերը ռեկուրսիվ կերպով միացրեք տվյալ գրացուցակին.:

`stow {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ջնջել սիմհղումները ռեկուրսիվ կերպով տվյալ գրացուցակից.:

`stow {{[-D|--delete]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Մոդելավորեք՝ տեսնելու, թե ինչպիսին կլինի արդյունքը.:

`stow {{[-n|--simulate]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ջնջել և վերաիմաստավորել հղումը՝:

`stow {{[-R|--restow]}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Բացառել `regex`-ին համապատասխանող ֆայլերը.:

`stow --ignore={{regex}} {{[-t|--target]}} {{path/to/target_directory}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

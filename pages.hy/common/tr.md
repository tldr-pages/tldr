# տր

> Թարգմանել նիշերը. գործարկել փոխարինումներ՝ հիմնված առանձին նիշերի և նիշերի հավաքածուների վրա:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>:.

- Փոխարինեք նիշերի բոլոր երևույթները ֆայլում և տպեք արդյունքը.:

`tr < {{path/to/file}} {{find_character}} {{replace_character}}`

- Փոխարինեք նիշերի բոլոր դեպքերը մեկ այլ հրամանի ելքից.:

`echo {{text}} | tr {{find_character}} {{replace_character}}`

- Առաջին հավաքածուի յուրաքանչյուր նիշը քարտեզագրեք երկրորդ հավաքածուի համապատասխան նիշին.:

`tr < {{path/to/file}} '{{abcd}}' '{{jkmn}}'`

- Ջնջել նշված նիշերի հավաքածուի բոլոր երևույթները մուտքագրումից.:

`tr < {{path/to/file}} {{[-d|--delete]}} '{{input_characters}}'`

- Կոմպրես մի շարք նույնական նիշերի մեկ նիշի.:

`tr < {{path/to/file}} {{[-s|--squeeze-repeats]}} '{{input_characters}}'`

- Թարգմանեք ֆայլի բովանդակությունը մեծատառով.:

`tr < {{path/to/file}} "[:lower:]" "[:upper:]"`

- Հեռացրեք ոչ տպագրվող նիշերը ֆայլից.:

`tr < {{path/to/file}} {{[-cd|--complement --delete]}} "[:print:]"`

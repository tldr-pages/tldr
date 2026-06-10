#ժամանակ

> Պարզ կեղևի հանգույց, որը կրկնվում է, մինչդեռ վերադարձի արժեքը մնում է զրո:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-while>:.

- Կարդացեք `stdin` և կատարեք գործողություն յուրաքանչյուր տողում.:

`while read line; do {{echo "$line"}}; done`

- Կատարեք հրաման ընդմիշտ ամեն վայրկյան մեկ անգամ.:

`while :; do {{command}}; sleep 1; done`

- Կատարեք հրաման, մինչև այն չհաջողվի.:

`while {{command}}; do :; done`

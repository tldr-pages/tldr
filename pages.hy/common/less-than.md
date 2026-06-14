# <

> Վերահղեք տվյալները `stdin`:.
> Լրացուցիչ տեղեկություններ. <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>:.

- Վերահղեք ֆայլը `stdin` (հասնում է նույն էֆեկտին, ինչ `cat file.txt |`):

`{{command}} < {{path/to/file.txt}}`

- Ստեղծեք այստեղ փաստաթուղթ և փոխանցեք այն `stdin`-ին (պահանջում է բազմագիծ հրաման).:

`{{command}} << {{EOF}} <Enter> {{multiline_text}} <Enter> {{EOF}}`

- Ստեղծեք այստեղ տող և փոխանցեք այն `stdin` (հասնում է նույն էֆեկտին, ինչ `echo string |`):

`{{command}} <<< {{string}}`

- Վերամշակեք տվյալները ֆայլից և ելքը գրեք մեկ այլ ֆայլում.:

`{{command}} < {{path/to/file.txt}} > {{path/to/file2.txt}}`

- Գրեք այստեղ փաստաթուղթը ֆայլի մեջ.:

`cat << {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- Անտեսեք առաջատար ներդիրները (լավ է նահանջով սկրիպտների համար, բայց չի աշխատում բացատների համար).:

`cat <<- {{EOF}} > {{path/to/file.txt}} <Enter> {{multiline_data}} <Enter> {{EOF}}`

- Փոխանցեք հրամանի ելքը ծրագրին որպես ֆայլի նկարագրիչ (Նշում. ի տարբերություն մնացածի, սա փոխարինում է արգումենտը տեղում ֆայլի ճանապարհով, ինչպիսին է `/dev/fd/63`):

`diff <({{command1}}) <({{command2}})`

- Բացեք մշտական ֆայլի նկարագրիչ.:

`exec {{3}}<{{path/to/file}}`

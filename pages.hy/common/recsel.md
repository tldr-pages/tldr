#վերադարձնել

> Տպել գրառումները recfile-ից. մարդու կողմից խմբագրվող, պարզ տեքստային տվյալների բազա:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/recutils/manual/recutils.html#Invoking-recsel>:.

- Քաղեք անունը և տարբերակի դաշտը.:

`recsel {{[-p|--print]}} name,version {{data.rec}}`

- Օգտագործեք «~» տողը տրված `regex`-ին համապատասխանելու համար:

`recsel {{[-e|--expression]}} "{{field_name}} ~ '{{regex}}' {{data.rec}}"`

- Օգտագործեք պրեդիկատ՝ անվանը և տարբերակին համապատասխանելու համար.:

`recsel {{[-e|--expression]}} "name ~ '{{regex}}' && version ~ '{{regex}}'" {{data.rec}}`

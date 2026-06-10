# todo.sh

> Պարզ և ընդարձակելի shell script՝ ձեր `todo.txt` ֆայլը կառավարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/todotxt/todo.txt-cli>:.

- Թվարկեք յուրաքանչյուր տարր.:

`todo.sh ls`

- Ավելացրեք նյութ նախագծի և համատեքստի պիտակներով.:

`todo.sh add '{{description}} +{{project}} @{{context}}'`

- Նշեք տարրը որպես [do]ne:

`todo.sh do {{item_no}}`

- Հեռացնել տարրը.:

`todo.sh rm {{item_no}}`

- Սահմանեք տարրի [առաջնահերթություն] (A-Z):

`todo.sh pri {{item_no}} {{priority}}`

- Փոխարինեք տարրը.:

`todo.sh replace {{item_no}} '{{new_description}}'`

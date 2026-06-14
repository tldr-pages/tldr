# msgcat

> Միավորել և միավորել բազմաթիվ `.po` թարգմանական ֆայլեր:.
> Օգտակար է ծրագրային ապահովման տեղայնացման խողովակաշարերում՝ հաղորդագրությունների կատալոգները զտման տարբերակների հետ համատեղելու համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gettext/manual/gettext.html#msgcat-Invocation>:.

- Միավորել մի քանի `.po` ֆայլ մեկում՝:

`msgcat {{file1.po file2.po ...}} {{[-o|--output-file]}} {{combined.po}}`

- Միավորել տեքստային ֆայլում թվարկված մուտքային ֆայլերը.:

`msgcat {{[-f|--files-from]}} {{path/to/file_list.txt}} {{[-o|--output-file]}} {{combined.po}}`

- Սահմանեք ելքային կոդավորումը (օրինակ՝ UTF-8):

`msgcat {{[-t|--to-code]}} {{UTF-8}} {{input.po}} {{[-o|--output-file]}} {{output.po}}`

- Արտադրեք միայն եզակի հաղորդագրություններ (հայտնվում են միայն մեկ ֆայլում).:

`msgcat {{[-u|--unique]}} {{file1.po file2.po ...}} {{[-o|--output-file]}} {{unique.po}}`

- Օգտագործեք առաջին հասանելի թարգմանությունը կրկնօրինակ գրառումների համար.:

`msgcat --use-first {{file1.po file2.po ...}} {{[-o|--output-file]}} {{output.po}}`

- Ցուցադրել օգնությունը.:

`msgcat {{[-h|--help]}}`

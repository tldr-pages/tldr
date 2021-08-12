# jrnl

> O aplicație simplă de jurnal pentru linia de comandă.
> Mai multe informaţii: <http://jrnl.sh>

- Introduceți o nouă intrare cu editorul dvs.:

`jrnl`

- Introduceți rapid o nouă intrare:

`jrnl {{today at 3am}}: {{title}}. {{content}}`

- Vezi ultimele zece intrări:

`jrnl -n {{10}}`

- Vezi tot ce sa întâmplat de la începutul anului trecut până la începutul lunii martie trecut:

`jrnl -from "{{last year}}" -until {{march}}`

- Editați toate intrările etichetate cu „texas” și „istorie”:

`jrnl {{@texas}} -and {{@history}} --edit`

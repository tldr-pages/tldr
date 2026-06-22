# cp

> Kopier filer og mapper.
> Mer informasjon: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Kopier en fil til et annet sted:

`cp {{sti/til/kildefil}} {{sti/til/målfil}}`

- Kopier en fil til en annen mappe, og behold filnavnet:

`cp {{sti/til/kildefil}} {{sti/til/overordnet_målmappe}}`

- Kopier innholdet i en mappe rekursivt til et annet sted (hvis målet finnes, kopieres mappen inn i det):

`cp {{[-r|--recursive]}} {{sti/til/kildemappe}} {{sti/til/målmappe}}`

- Kopier en mappe rekursivt, i detaljert modus (viser filer etter hvert som de kopieres):

`cp {{[-vr|--verbose --recursive]}} {{sti/til/kildemappe}} {{sti/til/målmappe}}`

- Kopier flere filer samtidig til en mappe:

`cp {{[-t|--target-directory]}} {{sti/til/målmappe}} {{sti/til/fil1 sti/til/fil2 ...}}`

- Kopier alle filer med en bestemt filendelse til et annet sted, i interaktiv modus (spør brukeren før overskriving):

`cp {{[-i|--interactive]}} {{*.ext}} {{sti/til/målmappe}}`

- Følg symbolske lenker før kopiering:

`cp {{[-L|--dereference]}} {{lenke}} {{sti/til/målmappe}}`

- Bruk hele stien til kildefilene, og opprett eventuelle manglende mellomliggende mapper ved kopiering:

`cp --parents {{kilde/sti/til/fil}} {{sti/til/målfil}}`

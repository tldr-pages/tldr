# groff

> Tastare program care citește text simplu amestecat cu comenzi de formatare și produce ieșire formatat.
> Este înlocuirea GNU pentru comenzile `troff` și `nroff` Unix pentru formatarea textului.
> Mai multe informaţii: <https://www.gnu.org/software/groff>

- Randați o pagină om ca text simplu și afișați rezultatul:

`groff -man -T utf8 {{manpage.1}}`

- Randați o pagină de om utilizând dispozitivul de ieșire ASCII și afișați-l utilizând un pager:

`groff -man -T ascii {{manpage.1}} | less`

- Randați o pagină om într-un fișier HTML:

`groff -man -T html {{manpage.1}} > {{page.html}}`

- Procesați un fișier roff utilizând preprocesoarele `tbl` și `pic` și setul de macrocomenzi `me`:

`groff -t -p -me -T utf8 {{foo.me}}`

- Rulați o comandă `groff` cu preprocesor și opțiuni macro ghicite de utilitarul `grog”:

`eval "$(grog -T utf8 {{foo.me}})"`

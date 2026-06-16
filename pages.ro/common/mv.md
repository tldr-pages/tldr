# mv

> Mută sau redenumește fișiere și foldere.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Redenumește un fișier sau folder atunci când destinația nu este un folder existent:

`mv {{cale/către/sursă}} {{cale/către/destinație}}`

- Mută un fișier sau folder într-un folder existent:

`mv {{cale/către/sursă}} {{cale/către/folder_existent}}`

- Mută mai multe fișiere într-un folder existent, păstrând numele fișierelor:

`mv {{cale/către/sursă1 cale/către/sursă2 ...}} {{cale/către/folder_existent}}`

- Nu cere confirmare înainte de a suprascrie fișierele existente:

`mv {{[-f|--force]}} {{cale/către/sursă}} {{cale/către/destinație}}`

- Cere confirmare interactiv înainte de a suprascrie fișierele existente, indiferent de permisiuni:

`mv {{[-i|--interactive]}} {{cale/către/sursă}} {{cale/către/destinație}}`

- Nu suprascrie fișierele existente la destinație:

`mv {{[-n|--no-clobber]}} {{cale/către/sursă}} {{cale/către/destinație}}`

- Mută fișiere în mod detaliat, afișându-le după ce sunt mutate:

`mv {{[-v|--verbose]}} {{cale/către/sursă}} {{cale/către/destinație}}`

- Specifică folderul de destinație pentru a putea folosi instrumente externe care colectează fișiere mutabile:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{cale/către/folder_destinație}}`

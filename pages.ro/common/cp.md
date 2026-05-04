# cp

> Copiază fișiere și foldere.
> Mai multe informații: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Copiază un fișier într-o altă locație:

`cp {{cale/către/fișier_sursă}} {{cale/către/fișier_destinație}}`

- Copiază un fișier într-un alt folder, păstrând numele fișierului:

`cp {{cale/către/fișier_sursă}} {{cale/către/folder_destinație}}`

- Copiază recursiv conținutul unui folder într-o altă locație (dacă destinația există, folderul este copiat în interiorul acesteia):

`cp {{[-r|--recursive]}} {{cale/către/folder_sursă}} {{cale/către/folder_destinație}}`

- Copiază recursiv un folder în mod detaliat (afișează fișierele pe măsură ce sunt copiate):

`cp {{[-vr|--verbose --recursive]}} {{cale/către/folder_sursă}} {{cale/către/folder_destinație}}`

- Copiază mai multe fișiere simultan într-un folder:

`cp {{[-t|--target-directory]}} {{cale/către/folder_destinație}} {{cale/către/fișier1 cale/către/fișier2 ...}}`

- Copiază toate fișierele cu o extensie specifică în altă locație, în mod interactiv (cere confirmare înainte de a suprascrie):

`cp {{[-i|--interactive]}} {{*.ext}} {{cale/către/folder_destinație}}`

- Urmărește link-urile simbolice înainte de copiere:

`cp {{[-L|--dereference]}} {{link}} {{cale/către/folder_destinație}}`

- Folosește calea completă a fișierelor sursă, creând orice foldere intermediare lipsă în timpul copierii:

`cp --parents {{sursă/cale/către/fișier}} {{cale/către/fișier_destinație}}`

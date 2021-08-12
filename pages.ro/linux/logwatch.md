# logwatch

> Rezumă multe jurnale diferite pentru servicii comune (de exemplu, apache, pam_unix, sshd, etc.) într-un singur raport.

- Analizați jurnalele pentru o serie de date la un anumit nivel de detaliu:

`logwatch --range {{yesterday|today|all|help}} --detail {{low|medium|others}}'`

- Restricționați raportul pentru a include doar informații pentru un serviciu selectat:

`logwatch --range {{all}} --service {{apache|pam_unix|etc}}`

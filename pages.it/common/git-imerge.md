# git-imerge

> Esegui un'unione (merge) o rebase tra due rami git in modo incrementale.
> Eventuali conflitti tra i due rami sono tracciati in coppie di commit distinti, per semplificarne la risoluzione.
> Maggiori informazioni: <https://github.com/mhagger/git-imerge>.

- Avvia un rebase usando imerge (dopo aver fatto il checkout del ramo di lavoro):

`git imerge rebase {{ramo_su_cui_eseguire_il_rebase}}`

- Avvia un'unione usando imerge (dopo aver fatto il checkout dal ramo di lavoro):

`git imerge merge {{ramo_su_cui_eseguire_l_unione}}`

- Mostra con un diagramma ASCII lo stato di esecuzione dell'unione o rebase:

`git imerge diagram`

- Continua con l'operazione di imerge dopo aver risolto i conflitti (ricorda di aggiungere i file in conflitto con `git add`):

`git imerge continue --no-edit`

- Concludi l'operazione di imerge dopo aver risolto tutti i conflitti:

`git imerge finish`

- Interrompi l'operazione di imerge e ritorna al ramo precedente:

`git-imerge remove && git checkout {{ramo_precedente}}`

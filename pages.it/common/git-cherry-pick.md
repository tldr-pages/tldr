# git cherry-pick

> Applica al ramo corrente le modifiche introdotte da commit esistenti.
> Per applicare le modifiche ad un altro ramo, usa prima `git checkout` per passare al ramo desiderato.
> Maggiori informazioni: <https://git-scm.com/docs/git-cherry-pick>.

- Applica un commit al ramo corrente:

`git cherry-pick {{commit}}`

- Applica una sequenza di commit al ramo corrente (vedi anche `git rebase --onto`):

`git cherry-pick {{commit_iniziale}}~..{{commit_finale}}`

- Applica un insieme di commit non sequenziali al ramo corrente:

`git cherry-pick {{commit_1}} {{commit_2}}`

- Aggiungi le modifiche introdotte da un commit alla directory di lavoro, ma senza creare un nuovo commit:

`git cherry-pick -n {{commit}}`

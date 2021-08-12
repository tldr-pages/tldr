# git cherry-pick

> Aplicați modificările introduse de angajamentele existente la ramura curentă.
> Pentru a aplica modificări la o altă ramură, utilizați mai întâi `git checkout` pentru a comuta la ramura dorită.
> Mai multe informaţii: <https://git-scm.com/docs/git-cherry-pick>

- Aplică o angajare sucursalei curente:

`git cherry-pick {{commit}}`

- Aplicați o gamă de angajări ramurii curente (a se vedea, de asemenea, `git rebase —onto`):

`git cherry-pick {{start_commit}}~..{{end_commit}}`

- Aplicați mai multe angajamente (non-secvențiale) la ramura curentă:

`git cherry-pick {{commit_1}} {{commit_2}}`

- Adăugați modificările unui angajament în directorul de lucru, fără a crea o comite:

`git cherry-pick -n {{commit}}`

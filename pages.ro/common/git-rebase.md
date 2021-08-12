# git rebase

> Reaplică angajările de la o ramură deasupra altei sucursale.
> Utilizat în mod obișnuit pentru a „muta” o întreagă ramură într-o altă bază, creând copii ale angajărilor în noua locație.
> Mai multe informaţii: <https://git-scm.com/docs/git-rebase>

- Rebasează ramura curentă deasupra unei alte sucursale specificate:

`git rebase {{new_base_branch}}`

- Începeți o rebase interactivă, care permite reordonarea, omise, combinate sau modificate:

`git rebase -i {{target_base_branch_or_commit_hash}}`

- Continuați o revenire care a fost întreruptă de un eșec de îmbinare, după editarea fișierelor conflictuale:

`git rebase --continue`

- Continuați o relasare care a fost întreruptă din cauza conflictelor de îmbinare, sărind peste angajamente conflictuale:

`git rebase --skip`

- Abandonați o relasare în curs de desfășurare (de exemplu, dacă este întreruptă de un conflict de îmbinare):

`git rebase --abort`

- Mutați o parte a ramurii curente pe o bază nouă, oferind baza veche pentru a începe de la:

`git rebase --onto {{new_base}} {{old_base}}`

- reaplicați ultimele 5 angajări pe loc, oprind pentru a le permite să fie reordonate, omise, combinate sau modificate:

`git rebase -i {{HEAD~5}}`

- Rezolvarea automată a conflictelor prin favorizarea versiunii ramurii de lucru (cuvântul cheie „lor' a inversat sensul în acest caz):

`git rebase -X theirs {{branch_name}}`

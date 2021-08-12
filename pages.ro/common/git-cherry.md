# git cherry

> Găsiți angajări care nu au fost încă aplicate în amonte.
> Mai multe informaţii: <https://git-scm.com/docs/git-cherry>

- Afișați angajările (și mesajele lor) cu angajări echivalente în amonte:

`git cherry -v`

- Specificați o ramură diferită în amonte și subiect:

`git cherry {{origin}} {{topic}}`

- Limita se angajează celor într-o anumită limită:

`git cherry {{origin}} {{topic}} {{base}}`

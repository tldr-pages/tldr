# git merge-one-file

> Rezolvă fuziunea unui singur fișier după o fuziune trivială.
> Mai multe informații: <https://git-scm.com/docs/git-merge-one-file>.

- Rezolvă un conflict de fuziune simplu pentru un fișier:

`git merge-one-file {{cale/către/fișier}}`

- Folosește ca ajutor în merge-index pentru un fișier:

`git merge-index git-merge-one-file {{cale/către/fișier}}`

- Gestionează fuziunea unui fișier binar:

`git merge-one-file -p {{cale/către/fișier}}`

- Aplică după read-tree într-o fuziune scriptată:

`git read-tree -m {{branch1}} {{branch2}} && git merge-index git-merge-one-file {{cale/către/fișier}}`

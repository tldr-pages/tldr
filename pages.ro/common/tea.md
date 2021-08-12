# tea

> Un instrument de linie de comandă pentru a interacționa cu serverele Gitea.
> Mai multe informaţii: <https://gitea.com/gitea/tea>

- Loghează-te pe un server Gitea:

`tea login add --name "{{name}}" --url "{{url}}" --token "{{token}}"`

- Afișează toate depozitele:

`tea repos ls`

- Afișează o listă de probleme:

`tea issues ls`

- Afișează o listă de probleme pentru un anumit depozit:

`tea issues ls --repo "{{repository}}"`

- Creați o nouă problemă:

`tea issues create --title "{{title}}" --body "{{body}}"`

- Afișează o listă de cereri deschise de tragere:

`tea pulls ls`

- Deschideți depozitul curent într-un browser:

`tea open`

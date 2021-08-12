# bw

> Un CLI pentru accesarea și gestionarea unui seif Bitwarden.
> Mai multe informaţii: <https://help.bitwarden.com/article/cli/>

- Conectați-vă la un cont de utilizator Bitwarden:

`bw login`

- Deconectați-vă de la un cont de utilizator Bitwarden:

`bw logout`

- Căutați și afișați elemente din seif Bitwarden:

`bw list items --search {{github}}`

- Afișează un anumit element din bolta Bitwarden:

`bw get item {{github}}`

- Creați un dosar în seiful Bitwarden:

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`

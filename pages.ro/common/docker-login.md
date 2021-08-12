# docker login

> Conectați-vă la un registru de andocare.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/login/>

- Conectați-vă interactiv într-un registru:

`docker login`

- Conectați-vă la un registru cu un anumit nume de utilizator (utilizatorul va fi solicitat pentru o parolă):

`docker login --username {{username}}`

- Conectați-vă la un registru cu nume de utilizator și parolă:

`docker login --username {{username}} --password {{password}} {{server}}`

- Conectați-vă la un registru cu parolă de la stdin:

` echo "{{password}}" | docker login --username {{username}} --password-stdin`

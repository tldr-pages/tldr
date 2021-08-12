# ibmcloud login

> Conectați-vă la IBM Cloud.
> Mai multe informaţii: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>

- Autentificare utilizând un prompt interactiv:

`ibmcloud login`

- Conectați-vă la un anumit punct final API (implicit este `cloud.ibm.com`):

`ibmcloud login -a {{api_endpoint}}`

- Conectați-vă prin furnizarea numelui de utilizator, a parolei și a regiunii vizate ca parametri:

`ibmcloud login -u {{username}} -p {{password}} -r {{us-south}}`

- Conectați-vă cu o cheie API, trecând-o ca argument:

`ibmcloud login --apikey {{api_key_string}}`

- Conectați-vă cu o cheie API, trecând-o ca fișier:

`ibmcloud login --apikey @{{path/to/api_key_file}}`

- Conectați-vă cu un ID federalizat (sign-on unic):

`ibmcloud login --sso`

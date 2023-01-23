# ibmcloud login

> Jelentkezzen be az IBM Cloudba. További információ: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- Jelentkezzen be interaktív prompt használatával:

`ibmcloud login`

- Jelentkezzen be egy adott API végpontra (alapértelmezett: `cloud.ibm.com`):

`ibmcloud login -a {{api_endpoint}}`

- Jelentkezzen be a felhasználónév, a jelszó és a célterület paraméterként történő megadásával:

`ibmcloud login -u {{username}} -p {{password}} -r {{us-south}}`

- Bejelentkezés egy API-kulccsal, azt argumentumként átadva:

`ibmcloud login --apikey {{api_key_string}}`

- Bejelentkezés API-kulccsal, fájlként átadva:

`ibmcloud login --apikey @{{path/to/api_key_file}}`

- Bejelentkezés szövetségi azonosítóval (egyszeri bejelentkezés):

`ibmcloud login --sso`

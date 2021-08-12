# oc

> Platforma de containere OpenShift CLI.
> Permite gestionarea aplicațiilor și a containerelor.
> Mai multe informaţii: <https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html>

- Conectați-vă la serverul OpenShift Container Platform:

`oc login`

- Creați un nou proiect:

`oc new-project {{project_name}}`

- Comutarea la un proiect existent:

`oc project {{project_name}}`

- Adăugați o nouă aplicație la un proiect:

`oc new-app {{repo_url}} --name {{application}}`

- Deschideți o sesiune shell la distanță într-un container:

`oc rsh {{pod_name}}`

- Lista păstăi într-un proiect:

`oc get pods`

- Deconectați-vă din sesiunea curentă:

`oc logout`

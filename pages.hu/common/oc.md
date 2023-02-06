# oc

> Az OpenShift Container Platform CLI. Lehetővé teszi az alkalmazások és konténerek kezelését. További információ: <https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html>.

- Jelentkezzen be az OpenShift Container Platform kiszolgálóra:

`oc login`

- Hozzon létre egy új projektet:

`oc new-project {{project_name}}`

- Váltás egy meglévő projektre:

`oc project {{project_name}}`

- Új alkalmazás hozzáadása egy projekthez:

`oc new-app {{repo_url}} --name {{application}}`

- Távoli shell munkamenet megnyitása egy konténerhez:

`oc rsh {{pod_name}}`

- Podok listázása egy projektben:

`oc get pods`

- Kijelentkezés az aktuális munkamenetből:

`oc logout`

# oc

> The OpenShift Container Platform CLI exposes commands for managing your applications. 
> More information: https://docs.openshift.com/container-platform/3.11/cli_reference/get_started_cli.html.

- Log in to the OpenShift Container Platform server:

`oc login`

- Create a new project:

`oc new-project {{project_name}}`

- Add a new app to project

`oc new-app {{git_link_or_docker_hub}} --name {{app_name}}`

- Open a remote shell session to a container:

`oc rsh {{pod}}`

- List pods in project

`oc get pods`

- End the current session

`oc logout`
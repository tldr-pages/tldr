# oc

> The OpenShift Container Platform CLI.
> Allows for application and container management.
> More information: <https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/cli_tools/index>.

- Log in to the OpenShift Container Platform server:

`oc login`

- Create a new project:

`oc new-project {{project_name}}`

- Switch to an existing project:

`oc project {{project_name}}`

- Add a new application to a project:

`oc new-app {{repo_url}} --name {{application}}`

- Open a remote shell session to a container:

`oc rsh {{pod_name}}`

- List pods in a project:

`oc get pods`

- Log out from the current session:

`oc logout`

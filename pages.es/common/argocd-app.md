# argocd app

> Interfaz de línea de comandos para gestionar aplicaciones por CD Argo.
> Más información: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- Lista aplicaciones:

`argocd app list --output {{json|yaml|wide}}`

- Obtén los detalles de la aplicación:

`argocd app get {{nombre_de_la_aplicacion}} --output {{json|yaml|wide}}`

- Despliega la aplicación internamente (en el mismo clúster en el que se ejecuta Argo CD):

`argocd app create {{nombre_de_la_aplicación}} --repo {{git_repo_url}} --path {{ruta/al/repo}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- Elimina una aplicación:

`argocd app delete {{nombre_de_la_aplicación}}`

- Activa la sincronización automática de aplicaciones:

`argocd app set {{nombre_de_la_aplicacion}} --sync-policy auto --auto-prune --self-heal`

- Previsualiza la sincronización de aplicaciones sin afectar al clúster:

`argocd app sync {{nombre_de_la_aplicacion}} --dry-run --prune`

- Muestra el historial de despliegue de aplicaciones:

`argocd app history {{nombre_de_la_aplicacion}} --output {{wide|id}}`

- Retrocede la aplicación a una versión anterior desplegada por ID de historial (eliminando recursos inesperados):

`argocd app rollback {{nombre_de_la_aplicacion}} {{history_id}} --prune`

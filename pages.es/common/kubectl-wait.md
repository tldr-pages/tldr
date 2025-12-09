# kubectl wait

> Espera a que los recursos alcancen un estado determinado.
> Más información: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_wait>.

- Espera a que un despliegue esté disponible:

`kubectl wait --for=condition=available deployment/{{nombre_del_despliegue}}`

- Espera a que todos los pods con una determinada etiqueta ([l]) estén listos:

`kubectl wait --for=condition=ready pod -l {{etiqueta_clave}}={{etiqueta_valor}}`

- Espera a que se elimine un pod:

`kubectl wait --for=delete pod {{nombre_del_pod}}`

- Espera a que se complete un trabajo, en un plazo de 120 segundos (si la condición no se cumple a tiempo, el estado de salida será fallido):

`kubectl wait --for=condition=complete job/{{nombre_del_trabajo}} --timeout 120s`

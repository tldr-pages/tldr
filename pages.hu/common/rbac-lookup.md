# rbac-lookup

> A Kubernetes fürtben lévő bármely felhasználóhoz, szolgáltatásfiókhoz vagy csoportnévhez kapcsolódó szerepek és fürtszerepek keresése. További információ: <https://github.com/reactiveops/rbac-lookup>.

- Az összes RBAC-kötés megtekintése:

`rbac-lookup`

- Az adott kifejezésnek megfelelő RBAC-kötések megtekintése:

`rbac-lookup {{search_term}}`

- Az összes RBAC-kötés megtekintése a forrásszerep-kötéssel együtt:

`rbac-lookup -o wide`

- Az összes RBAC-kötés megtekintése tárgy szerint szűrve:

`rbac-lookup -k {{user|group|serviceaccount}}`

- Az összes RBAC-kötés megtekintése az IAM-szerepekkel együtt (ha GKE-t használ):

`rbac-lookup --gke`

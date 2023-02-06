# cs resolve

> A Resolve egy vagy több másik függőség tranzitív függőségeit listázza. További információ: <https://get-coursier.io/docs/cli-resolve>.

- Két függőség tranzitív függőségi listájának feloldása:

`cs resolve {{group_id1}}:{{artifact_id1}}:{{artifact_version1}} {{group_id2}}:{{artifact_id2}}:{{artifact_version2}}`

- Egy csomag tranzitív függőségi listáinak feloldása a függőségi fa alapján:

`cs resolve --tree {{group_id}}:{{artifact_id}}:{{artifact_version}}`

- Függőségi fa feloldása fordított sorrendben (egy függőségtől a függőségek felé):

`cs resolve --reverse-tree {{group_id}}:{{artifact_id}}:{{artifact_version}`

- Az összes olyan könyvtár kinyomtatása, amely egy adott könyvtár függvénye:

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}`

- Az összes olyan könyvtár kiírása, amely egy adott könyvtárverziótól függ:

`cs resolve {{group_id}}:{{artifact_id}}:{{artifact_version}} --what-depends-on {{searched_group_id}}:{{searched_artifact_id}}{{searched_artifact_version}}`

- Egy csomagkészlet közötti esetleges konfliktusok kiírása:

`cs resolve --conflicts {{group_id1:artifact_id1:artifact_version1 group_id2:artifact_id2:artifact_version2 ...}}`

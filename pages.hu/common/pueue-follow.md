# pueue follow

> Kövesse az éppen futó feladat kimenetét. Lásd még: `pueue log`. További információ: <https://github.com/Nukesor/pueue>.

- Egy feladat kimenetének követése (`stdout` + `stderr`):

`pueue follow {{task_id}}`

- Kövesse egy feladat kimenetét: `stderr`:

`pueue follow --err {{task_id}}`

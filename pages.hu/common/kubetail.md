# kubetail

> Segédprogram több Kubernetes pod naplójának egyidejű követésére. További információ: <https://github.com/johanhaleby/kubetail>.

- Több pod (amelyek neve "my_app"-mal kezdődik) naplóinak egy menetben történő követése:

`kubetail {{my_app}}`

- Több podból csak egy adott konténer naplójának tailelése:

`kubetail {{my_app}} -c {{my_container}}`

- Több pod több konténerének tailelése:

`kubetail {{my_app}} -c {{my_container_1}} -c {{my_container_2}}`

- Egyszerre több alkalmazás taileléséhez vesszővel válassza szét őket:

`kubetail {{my_app_1}},{{my_app_2}}`

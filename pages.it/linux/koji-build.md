# koji build

> Compila un pacchetto RPM.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Compila un pacchetto da `src.rpm`:

`koji build {{target}} {{percorso/al/src.rpm}}`

- Compila un pacchetto da un URL SCM (Source Code Management):

`koji build {{target}} {{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}`

- Esegue una build di prova:

`koji build {{target}} {{percorso/al/src.rpm}} --scratch`

- Attende la build, anche se è in esecuzione in background:

`koji build {{target}} {{percorso/al/src.rpm}} --wait`

- Non attende la build:

`koji build {{target}} {{percorso/al/src.rpm}} --nowait`

- Mostra aiuto:

`koji build {{[-h|--help]}}`

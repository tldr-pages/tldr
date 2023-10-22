# docker cp

> Copia file o directory tra il filesystem di un container e quello locale (host).
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/cp>.

- Copia un file o una directory dall'host a un container:

`docker cp {{percorso/del/file_o_directory_su_host}} {{nome_container}}:{{percorso/del/file_o_directory_su_container}}`

- Copia un file o una directory da un container all'host:

`docker cp {{nome_container}}:{{percorso/del/file_o_directory_su_container}} {{percorso/del/file_o_directory_su_host}}`

- Copia un file o una directory dall'host a un container, seguendo un link simbolico (non copiare il link simbolico, ma direttamente il file da lui referenziato):

`docker cp --follow-link {{percorso/del/link_simbolico_su_host}} {{nome_container}}:{{percorso/del/file_o_directory_su_container}}`

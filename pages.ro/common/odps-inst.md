# odps inst

> Gestionați instanțele în ODPS (Serviciul de procesare a datelor deschise).
> A se vedea, de asemenea, `odps`.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Arată instanțele create de utilizatorul curent:

`show instances;`

- Descrieți detaliile unei instanțe:

`desc instance {{instance_id}};`

- Verificați starea unei instanțe:

`status {{instance_id}};`

- Așteptați la terminarea unei instanțe, jurnalul de imprimare și informațiile de progres până atunci:

`wait {{instance_id}};`

- Omoară o instanţă:

`kill {{instance_id}};`

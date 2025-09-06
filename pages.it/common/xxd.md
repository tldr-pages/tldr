# xxd

> Mostra la rappresentazione esadecimale (hexdump) di un file binario e viceversa.
> Maggiori informazioni: <https://manned.org/xxd>.

- Creare l'hexdump di un file binario e mostrare l'output:

`xxd {{file_di_input}}`

- Creare l'hexdump di un file binario e salvare il risultato in un file:

`xxd {{file_di_input}} {{file_di_output}}`

- Mostrare un output in una versione un po' più compatta, dove gli zero consegutivi vengono sostituiti da un asterisco:

`xxd -a {{file_di_input}}`

- Mostrare l'output in 10 colonne di un ottetto (byte) ciascuna:

`xxd -c {{10}} {{file_di_input}}`

- Mostrare l'output solo fino ad una lunghezza massima di 32 bytes:

`xxd -l {{32}} {{file_di_input}}`

- Mostrare l'output in modalità normale, senza spazi tra le colonne:

`xxd -p {{file_di_input}}`

- Eseguire l'operazione inversa, ovvero da un hexdump creare il binario e salvarlo in un file:

`xxd -r -p {{file_di_input}} {{file_di_output}}`

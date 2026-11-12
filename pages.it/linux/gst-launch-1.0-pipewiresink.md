# gst-launch-1.0 pipewiresink

> Crea un nodo PipeWire da cui inviare dati.
> Maggiori informazioni: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- Invia video di test:

`gst-launch-1.0 videotestsrc ! pipewiresink mode=provide`

- Assegna un nome al nodo PipeWire:

`gst-launch-1.0 {{videotestsrc}} ! pipewiresink mode=provide client-name={{nome_nodo}}`

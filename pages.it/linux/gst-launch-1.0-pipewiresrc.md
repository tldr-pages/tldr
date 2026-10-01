# gst-launch-1.0 pipewiresrc

> Legge dati da un nodo PipeWire.
> Maggiori informazioni: <https://github.com/PipeWire/pipewire/tree/master/src/gst>.

- Ascolta il microfono predefinito:

`gst-launch-1.0 pipewiresrc ! autoaudiosink`

- Specifica il nodo da registrare e visualizza il video in una finestra:

`gst-launch-1.0 pipewiresrc target-object={{nome_nodo}} ! autovideosink`

- Registra video in un file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{matroskamux}} ! filesink location={{percorso/al/file.mkv}}`

- Cattura uno screenshot da un nodo video:

`gst-launch-1.0 pipewiresrc num-buffers=1 ! videoconvert ! {{pngenc}} ! filesink location={{percorso/al/file.png}}`

- Registra audio in un file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc ! {{opusenc}} ! {{oggmux}} ! filesink location={{percorso/al/file.ogg}}`

- Registra il monitor di un dispositivo:

`gst-launch-1.0 pipewiresrc target-object={{nome_nodo}} stream-properties=props,stream.capture.sink=true ! {{audioconvert ! fakesink}}`

- Multiplexa audio e video in un file:

`gst-launch-1.0 {{[-e|--eos-on-shutdown]}} pipewiresrc do-timestamp=true ! videoconvert ! {{x264enc}} ! {{h264parse}} ! {{mux}}. pipewiresrc do-timestamp=true ! {{opusenc}} ! {{mux}}. {{matroskamux}} name={{mux}} ! filesink location={{percorso/al/file.mkv}}`

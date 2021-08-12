# iperf3

> Generator trafic pentru testarea lățimii de bandă a rețelei
> Mai multe informaţii: <https://iperf.fr>

- Rulați iperf3 ca server:

`iperf3 -s`

- Rulați un server iperf3 pe un anumit port:

`iperf3 -s -p {{port}}`

- Începeți testul de lățime de bandă:

`iperf3 -c {{server}}`

- Rulați iperf3 în mai multe fluxuri paralele:

`iperf3 -c {{server}} -P {{streams}}`

- Direcția inversă a testului. Serverul trimite date clientului:

`iperf3 -c {{server}} -R`

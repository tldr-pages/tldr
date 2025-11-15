# snort

> Open-source network intrusion detection system.
> More information: <https://www.snort.org/#documents>.

- Capture packets with verbose output:

`sudo snort -v -i {{interface}}`

- Capture packets and dump application layer data with verbose output:

`sudo snort -vd -i {{interface}}`

- Capture packets and display link layer packet headers with verbose output:

`sudo snort -ve -i {{interface}}`

- Capture packets and save them in the specified directory:

`sudo snort -i {{interface}} -l {{path/to/directory}}`

- Capture packets according to rules and save offending packets along with alerts:

`sudo snort -i {{interface}} -c {{path/to/rules.conf}} -l {{path/to/directory}}`

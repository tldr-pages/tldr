# netstat

> Zeige netzwerkbezogene Informationen wie offene Verbindungen, offene Socket-Ports etc.
> Siehe auch: `ss`.
> Weitere Informationen: <https://manned.org/netstat>.

- Liste alle Ports auf:

`netstat {{[-a|--all]}}`

- Liste alle lauschenden Ports auf:

`netstat {{[-l|--listening]}}`

- Liste lauschende TCP-Ports auf:

`netstat {{[-t|--tcp]}}`

- Zeige PID und Programmnamen:

`netstat {{[-p|--program]}}`

- Liste Informationen kontinuierlich auf:

`netstat {{[-c|--continuous]}}`

- Liste Routen auf und löse IP-Adressen nicht in Hostnamen auf:

`netstat {{[-rn|--route --numeric]}}`

- Liste lauschende TCP- und UDP-Ports auf (+ Benutzer und Prozess wenn Sie root sind):

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`

# tshark

> Packet analysis tool, CLI version of Wireshark.
> More information: <https://tshark.dev/>.

- Monitor everything on localhost:

`tshark`

- Only capture packets matching a specific capture filter:

`tshark -f '{{udp port 53}}'`

- Only show packets matching a specific output filter:

`tshark -Y '{{http.request.method == "GET"}}'`

- Decode a TCP port using a specific protocol (e.g. HTTP):

`tshark -d tcp.port=={{8888}},{{http}}`

- Specify the format of captured output:

`tshark -T {{json|text|ps|…}}`

- Select specific fields to output:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{ip.src}}`

- Write captured packet to a file:

`tshark -w {{path/to/file}}`

- Analyze packets from a file:

`tshark -r {{filename}}.pcap`

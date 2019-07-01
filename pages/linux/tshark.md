# tshark

> Packet analysis tool, CLI version of wireshark.

- Monitor everything on localhost:

`tshark`

- Only output captured packets matching a specific wireshark filter:

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

`tshark -r {{file_name}}.pcap`

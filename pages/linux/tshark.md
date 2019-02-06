# tshark

> Packet analysis tool, CLI version of wireshark.

- Monitor everything on localhost:

`tshark`

- Filter captured packets by method:

`tshark -Y 'http.request.method == "GET"'`

- Decode the current port with a specific protocol (ex: http):

`tshark -d tcp.port=={{8888}},{{http}}`

- Specify the format of captured output:

`tshark -T {{json|text|ps|…}}`

- Select specific fields to output:

`tshark -T {{fields|ek|json|pdml}} -e {{http.request.method}} -e {{http.request.uri}} -e {{ip.src}} -e {{tcp.srcport}} -e {{ip.dst}} -e {{tcp.dstport}}`

- Write captured packet to a file:

`tshark -w {{path/to/file}}`

- Analyze packets from a file:

`tshark -r {{file_name}}.pcap`

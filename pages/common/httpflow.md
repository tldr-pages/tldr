# httpflow

> A utility to capture and dump HTTP streams.
> More information: <https://github.com/six-ddc/httpflow>.

- Capture traffic on all interfaces:

`httpflow -i {{any}}`

- Use a bpf-style capture to filter the results:

`httpflow {{host httpbin.org or host baidu.com}}`

- Use a `regex` to filter requests by URLs:

`httpflow -u '{{regex}}'`

- Read packets from PCAP format binary file:

`httpflow -r {{out.cap}}`

- Write the output to a directory:

`httpflow -w {{path/to/directory}}`

# vegeta

> A command line utility and a library for HTTP load testing.
> See also `ab`.
> More information: <https://github.com/tsenart/vegeta>.

- Launch an attack lasting 30 seconds:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- Launch an attack on a server with a self-signed https certificate:

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- Launch an attack with a rate of 10 requests per second:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- Launch an attack and display a report:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- Launch an attack and plot the results on a graph (latency over time):

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{path/to/results.html}}`

- Launch an attack against multiple URLs from a file:

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`

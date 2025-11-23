# locust

> Load-testing tool to determine number of concurrent users a system can handle.
> More information: <https://docs.locust.io/en/stable/configuration.html#configuration>.

- Load-test "example.com" with web interface using locustfile.py:

`locust {{[-H|--host]}} {{http://example.com}}`

- Use a different test file:

`locust {{[-H|--host]}} {{http://example.com}} {{[-f|--locustfile]}} {{test_file.py}}`

- Run test without web interface, spawning 1 user a second until there are 100 users:

`locust {{[-H|--host]}} {{http://example.com}} --headless {{[-u|--users]}} 100 {{[-r|--spawn-rate]}} 1`

- Start Locust in master mode:

`locust {{[-H|--host]}} {{http://example.com}} --master`

- Connect Locust slave to master:

`locust {{[-H|--host]}} {{http://example.com}} --slave`

- Connect Locust slave to master on a different machine:

`locust {{[-H|--host]}} {{http://example.com}} --slave --master-host {{master_hostname}}`

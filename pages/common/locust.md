# locust

> Load-testing tool to determine number of concurrent users a system can handle.

- Load-test "example.com" with web interface using locustfile.py:

`locust --host={{http://example.com}}`

- Use a different test file:

`locust --locustfile={{test_file.py}} --host={{http://example.com}}`

- Run test without web interface, spawning 1 user a second until there are 100 users:

`locust --no-web --clients={{100}} --hatch-rate={{1}} --host={{http://example.com}}`

- Start locust in master mode:

`locust --master --host={{http://example.com}}`

- Connect locust slave to master:

`locust --slave --host={{http://example.com}}`

- Connect locust slave to master on a different machine:

`locust --slave --master-host={{master_hostname}} --host={{http://example.com}}`

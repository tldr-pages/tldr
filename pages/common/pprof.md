# pprof

> Command-line tool for visualization and analysis of profile data.
> More information: <https://github.com/google/pprof>.

- Generate a text report from a specific profiling file, on fibbo binary:

`pprof -top {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Generate a graph and open it on a web browser:

`pprof -svg {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Run pprof in interactive mode to be able to manually launch `pprof` on a file:

`pprof {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Run a web server that serves a web interface on top of `pprof`:

`pprof -http={{localhost:8080}} {{./fibbo}} {{./fibbo-profile.pb.gz}}`

- Fetch a profile from an HTTP server and generate a report:

`pprof {{http://localhost:8080/debug/pprof}}`

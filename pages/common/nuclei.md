# nuclei

> Fast and customizable vulnerability scanner using a simple YAML-based DSL.
> More information: <https://docs.projectdiscovery.io/tools/nuclei/running>.

- [u]pdate `nuclei` [t]emplates to the latest released version (downloaded to `~/nuclei-templates` on macOS/Linux or `%USERPROFILE%\nuclei-templates` on Windows):

`nuclei {{[-ut|-update-templates]}}`

- [l]ist all [t]emplates by specific [p]rotocol [t]ype:

`nuclei -tl {{[-pt|-type]}} {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Run an [a]utomatic web [s]can using Wappalyzer technology detection for a specific target [u]RL/host:

`nuclei {{[-as|-automatic-scan]}} {{[-u|-target]}} {{scanme.nmap.org}}`

- Run HTTP [p]rotocol [t]ype templates of specific severity, [e]xporting results to [m]arkdown files inside a specific directory:

`nuclei {{[-s|-severity]}} {{high,critical,...}} {{[-pt|-type]}} http {{[-u|-target]}} {{https://example.com}} {{[-me|-markdown-export]}} {{path/to/directory}}`

- Run all templates with a custom [r]ate [l]imit, maximum [b]ulk [s]ize, and silent output (only findings shown):

`nuclei {{[-rl|-rate-limit]}} {{150}} {{[-bs|-bulk-size]}} {{25}} {{[-c|-concurrency]}} {{25}} -silent {{[-u|-target]}} {{https://example.com}}`

- Run a specific nuclei-bundled [w]orkflow against a target:

`nuclei {{[-w|-workflows]}} {{workflows/wordpress-workflow.yaml}} {{[-u|-target]}} {{https://example.com}}`

- Run one or more specific [t]emplates or directory with [t]emplates with [v]erbose output in `stderr` and [o]utput detected issues/vulnerabilities to a file:

`nuclei {{[-t|-templates]}} {{path/to/nuclei-templates/http}} {{[-u|-target]}} {{https://example.com}} {{[-v|-verbose]}} {{[-o|-output]}} {{path/to/results}}`

- Run a scan based on one or more [t]emplate [c]onditions:

`nuclei {{[-tc|-template-condition]}} "{{contains(tags, 'xss') && contains(tags, 'cve')}}" {{[-u|-target]}} {{https://example.com}}`

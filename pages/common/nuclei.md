# nuclei

> Fast and customizable vulnerability scanner using a simple YAML-based DSL.
> More information: <https://docs.projectdiscovery.io/tools/nuclei/running>.

- Update `nuclei` templates to the latest released version (downloaded to `~/nuclei-templates` on macOS/Linux or `%USERPROFILE%\nuclei-templates` on Windows):

`nuclei {{[-ut|-update-templates]}}`

- [l]ist all [t]emplates by specific [p]rotocol [t]ype:

`nuclei -tl {{[-pt|-type]}} {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Run an automatic web scan using Wappalyzer technology detection for a specific target [u]RL/host:

`nuclei {{[-as|-automatic-scan]}} {{[-u|-target]}} {{example.com}}`

- Run HTTP [p]rotocol [t]ype templates of specific severity, exporting results to markdown files inside a specific directory:

`nuclei {{[-s|-severity]}} {{high,critical,...}} {{[-pt|-type]}} http {{[-u|-target]}} {{https://example.com}} {{[-me|-markdown-export]}} {{path/to/directory}}`

- Run all templates with a custom rate limit, maximum bulk size, and silent output (only findings shown):

`nuclei {{[-rl|-rate-limit]}} {{150}} {{[-bs|-bulk-size]}} {{25}} {{[-c|-concurrency]}} {{25}} -silent {{[-u|-target]}} {{https://example.com}}`

- Run a specific nuclei-bundled workflow against a target:

`nuclei {{[-w|-workflows]}} {{workflows/wordpress-workflow.yaml}} {{[-u|-target]}} {{https://example.com}}`

- Run one or more specific templates or directory with templates with verbose output in `stderr` and output detected issues/vulnerabilities to a file:

`nuclei {{[-t|-templates]}} {{path/to/nuclei-templates/http}} {{[-u|-target]}} {{https://example.com}} {{[-v|-verbose]}} {{[-o|-output]}} {{path/to/results}}`

- Use an AI prompt to dynamically generate a template to scan a target (projectdiscovery cloud pdcp API key needs to be configured using `nuclei -auth`):

`nuclei {{[-u|-target]}} {{https://example.com}} {{[-ai|-prompt]}} {{"find admin login endpoints"}}`

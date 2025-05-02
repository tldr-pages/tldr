# nuclei

> Fast and customizable vulnerability scanner based on a simple YAML based DSL.
> More information: <https://docs.projectdiscovery.io/tools/nuclei/running>.

- [u]pdate `nuclei` [t]emplates to the latest released version (will be downloaded to `~/nuclei-templates`):

`nuclei {{[-ut|-update-templates]}}`

- [l]ist all [t]emplates with a specific [p]rotocol [t]ype:

`nuclei -tl {{[-pt|-type]}} {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Run an [a]utomatic web [s]can using wappalyzer technology detection specifying a target [u]RL/host to scan:

`nuclei {{[-as|-automatic-scan]}} {{[-u|-target]}} {{scanme.nmap.org}}`

- Run HTTP [p]rotocol [t]ype templates of high and critical severity, [e]xporting results to [m]arkdown files inside a specific directory:

`nuclei {{[-s|-severity]}} high,critical {{[-pt|-type]}} http {{[-u|-target]}} {{http://scanme.sh}} {{[-me|-markdown-export]}} {{markdown_directory}}`

- Run all templates using a different [r]ate [l]imit and maximum [b]ulk [s]ize with silent output (only showing the findings):

`nuclei {{[-rl|-rate-limit]}} {{150}} {{[-bs|-bulk-size]}} {{25}} {{[-c|-concurrency]}} {{25}} -silent {{[-u|-target]}} {{http://scanme.sh}}`

- Run the WordPress [w]orkflow against a WordPress site:

`nuclei {{[-w|-workflows]}} {{path/to/nuclei-templates/workflows/wordpress-workflow.yaml}} {{[-u|-target]}} {{https://sample.wordpress.site}}`

- Run one or more specific [t]emplates or directory with [t]emplates with [v]erbose output in `stderr` and [o]utput detected issues/vulnerabilities to a file:

`nuclei {{[-t|-templates]}} {{path/to/nuclei-templates/http}} {{[-u|-target]}} {{http://scanme.sh}} {{[-v|-verbose]}} {{[-o|-output]}} {{results}}`

- Run scan based on one or more [t]emplate [c]onditions:

`nuclei {{[-tc|-template-condition]}} "{{contains(tags, 'xss') && contains(tags, 'cve')}}" {{[-u|-target]}} {{https://vulnerable.website}}`

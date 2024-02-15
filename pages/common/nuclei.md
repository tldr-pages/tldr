# nuclei

> Fast and customizable vulnerability scanner based on a simple YAML based DSL.
> More information: <https://github.com/projectdiscovery/nuclei>.

- [u]pdate `nuclei` [t]emplates to the latest released version:

`nuclei -ut`

- [l]ist all [t]emplates with a specific [p]rotocol [t]ype:

`nuclei -tl -pt {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Run an [a]utomatic web [s]can using wappalyzer technology detection specifying a target [u]RL/host to scan:

`nuclei -as -u {{scanme.nmap.org}}`

- Run HTTP [p]rotocol [t]ype templates of high and critical severity, [e]xporting results to [m]arkdown files inside a specific directory:

`nuclei -severity high,critical -pt http -u {{http://scanme.sh}} -me {{markdown_directory}}`

- Run all templates using a different [r]ate [l]imit and maximum [b]ulk [s]ize with silent output (only showing the findings):

`nuclei -rl {{150}} -bs {{25}} -c {{25}} -silent -u {{http://scanme.sh}}`

- Run the WordPress [w]orkflow against a WordPress site:

`nuclei -w {{path/to/nuclei-templates/workflows/wordpress-workflow.yaml}} -u {{https://sample.wordpress.site}}`

- Run one or more specific [t]emplates or directory with [t]emplates with [v]erbose output in `stderr` and [o]utput detected issues/vulnerabilities to a file:

`nuclei -t {{path/to/nuclei-templates/http}} -u {{http://scanme.sh}} -v -o {{results}}`

- Run scan based on one or more [t]emplate [c]onditions:

`nuclei -tc {{"contains(tags, 'xss') && contains(tags, 'cve')"}} -u {{https://vulnerable.website}}`

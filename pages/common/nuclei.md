# nuclei

> Fast and customizable vulnerability scanner based on simple YAML based DSL.
> More information: <https://github.com/projectdiscovery/nuclei>.

- Update nuclei templates to the latest released version:

`nuclei -ut`

- List all templates (of protocol type dns):

`nuclei -tl {{-pt dns}}`

- Run automatic web scan using wappalyzer technology detection:

`nuclei -as -u {{scanme.nmap.org}}`

- Run http protocol type templates of high and critical severity; write results to markdown files:

`nuclei -severity high,critical -pt http -u {{http://scanme.sh}} -me {{markdown_dir}}`

- Run all templates using rate limiting options with reduced silent output:

`nuclei -rl {{150}} -bs {{25}} -c {{25}} -silent -u {{http://scanme.sh}}`

- Run (wordpress) [w]orkflow against a (wordpress) site:

`nuclei -w {{path/to/nuclei-templates/workflows/wordpress-workflow.yaml}} -u {{https://sample.wordpress.site}}`

- Run specific template collections from a directory with verbose output in STDERR and detected issues/vulns to a file:

`nuclei -t {{path/to/nuclei-templates/http}} -u {{http://scanme.sh}} -v -o {{results}}`

- Run scan based on multiple template conditions:

`nuclei -tc {{"contains(tags, 'xss') && contains(tags, 'cve')"}} -u {{https://vulnerable.website}}`

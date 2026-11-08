# nuclei

> Scanner de vulnerabilidades rápido e personalizável usando uma DSL simples baseada em YAML.
> Mais informações: <https://docs.projectdiscovery.io/opensource/nuclei/running>.

- Atualiza os templates do `nuclei` para a versão mais recente lançada (baixados em `~/nuclei-templates` no macOS/Linux ou `%USERPROFILE%\nuclei-templates` no Windows):

`nuclei {{[-ut|-update-templates]}}`

- [l]ista todos os [t]emplates por [t]ipo específico de [p]rotocolo:

`nuclei -tl {{[-pt|-type]}} {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- Executa uma varredura web automática usando detecção de tecnologias do Wappalyzer para uma [u]RL/host alvo:

`nuclei {{[-as|-automatic-scan]}} {{[-u|-target]}} {{example.com}}`

- Executa templates de [p]rotocolo do [t]ipo HTTP de severidade específica, exportando os resultados em arquivos Markdown dentro de um diretório específico:

`nuclei {{[-s|-severity]}} {{high,critical,...}} {{[-pt|-type]}} http {{[-u|-target]}} {{https://example.com}} {{[-me|-markdown-export]}} {{caminho/para/diretorio}}`

- Executa todos os templates com um limite de requisições personalizado, tamanho máximo de lote e saída silenciosa (apenas achados são exibidos):

`nuclei {{[-rl|-rate-limit]}} {{150}} {{[-bs|-bulk-size]}} {{25}} {{[-c|-concurrency]}} {{25}} -silent {{[-u|-target]}} {{https://example.com}}`

- Executa um fluxo de trabalho (workflow) específico integrado ao nuclei contra um alvo:

`nuclei {{[-w|-workflows]}} {{workflows/wordpress-workflow.yaml}} {{[-u|-target]}} {{https://example.com}}`

- Executa um ou mais templates específicos ou um diretório com templates com saída detalhada em `stderr`, gravando vulnerabilidades detectadas em um arquivo:

`nuclei {{[-t|-templates]}} {{caminho/para/nuclei-templates/http}} {{[-u|-target]}} {{https://example.com}} {{[-v|-verbose]}} {{[-o|-output]}} {{caminho/para/resultados}}`

- Usa um prompt de IA para gerar dinamicamente um template e escanear um alvo (requer a chave de API da nuvem da ProjectDiscovery configurada via `nuclei -auth`):

`nuclei {{[-u|-target]}} {{https://example.com}} {{[-ai|-prompt]}} "{{find admin login endpoints}}"`

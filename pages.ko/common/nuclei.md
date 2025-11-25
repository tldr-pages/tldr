# nuclei

> 간단한 YAML 기반 DSL을 사용하는 빠르고 커스터마이즈 가능한 취약점 스캐너.
> 더 많은 정보: <https://docs.projectdiscovery.io/tools/nuclei/running>.

- `nuclei` [t]emplates를 최신 버전으로 [u]pdate (다운로드는 `~/nuclei-templates`에 저장됨):

`nuclei -ut`

- 특정 [p]rotocol [t]ype의 모든 [t]emplates 나열:

`nuclei -tl -pt {{dns|file|http|headless|tcp|workflow|ssl|websocket|whois|code|javascript}}`

- wappalyzer 기술 감지를 사용하여 자동 웹 스캔을 수행하고 스캔할 대상 [u]RL/호스트 지정:

`nuclei -as -u {{scanme.nmap.org}}`

- 높은 및 치명적 심각도의 HTTP [p]rotocol [t]ype 템플릿을 실행하고, 결과를 특정 디렉토리 내 [m]arkdown 파일로 [e]xport:

`nuclei -severity high,critical -pt http -u {{http://scanme.sh}} -me {{마크다운_디렉토리}}`

- 다른 [r]ate [l]imit과 최대 [b]ulk [s]ize를 사용하여 모든 템플릿 실행하며, 조용한 출력(발견된 내용만 표시):

`nuclei -rl {{150}} -bs {{25}} -c {{25}} -silent -u {{http://scanme.sh}}`

- WordPress 사이트에 대해 WordPress [w]orkflow 실행:

`nuclei -w {{경로/대상/nuclei-templates/workflows/wordpress-workflow.yaml}} -u {{https://sample.wordpress.site}}`

- 하나 이상의 특정 [t]emplates 또는 [t]emplates가 있는 디렉토리를 실행하며 `stderr`에 [v]erbose 출력 및 검출된 문제/취약점을 파일로 [o]utput:

`nuclei -t {{경로/대상/nuclei-templates/http}} -u {{http://scanme.sh}} -v -o {{결과들}}`

- 하나 이상의 [t]emplate [c]onditions에 기반한 스캔 실행:

`nuclei -tc "{{contains(tags, 'xss') && contains(tags, 'cve')}}" -u {{https://vulnerable.website}}`

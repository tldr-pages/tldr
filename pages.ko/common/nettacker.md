# nettacker

> 정보 수집 자동화, 취약점 스캔 및 보고서 생성.
> 더 많은 정보: <https://nettacker.readthedocs.io/en/latest/Home/>.

- 사용 가능한 모든 모듈 나열:

`nettacker --show-all-modules`

- 대상에 포트 스캔 실행:

`nettacker {{[-m|--modules]}} port_scan {{[-i|--targets]}} {{192.168.0.1/24,owasp.org,scanme.org,...}}`

- 특정 포트 및 파일에 나열된 대상에 포트 스캔 실행 (줄바꿈으로 구분):

`nettacker {{[-m|--modules]}} port_scan {{[-g|--ports]}} {{22,80,443,...}} {{-l|--targets-list}} {{경로/대상/targets.txt}}`

- 스캔 전 핑 테스트를 실행한 후 대상에 여러 스캔 유형 실행:

`nettacker --ping-before-scan {{[-m|--modules]}} {{port_scan,subdomain_scan,waf_scan,...}} {{[-g|--ports]}} {{80,443}} {{[-i|--targets]}} {{owasp.org}}`

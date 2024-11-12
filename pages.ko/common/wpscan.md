# wpscan

> WordPress 취약점 스캐너.
> 더 많은 정보: <https://github.com/wpscanteam/wpscan>.

- 취약점 데이터베이스 업데이트:

`wpscan --update`

- WordPress 웹사이트 스캔:

`wpscan --url {{url}}`

- 무작위 사용자 에이전트와 수동 감지를 사용하여 WordPress 웹사이트 스캔:

`wpscan --url {{url}} --stealthy`

- 취약한 플러그인을 확인하고 `wp-content` 디렉터리 경로를 지정하여 WordPress 웹사이트 스캔:

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{원격/경로/대상/워드프레스-내용}}`

- 프록시를 통해 WordPress 웹사이트 스캔:

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{사용자 명:비밀번호}}`

- WordPress 웹사이트에서 사용자 식별자 열거 수행:

`wpscan --url {{url}} --enumerate {{u}}`

- WordPress 웹사이트에 대한 비밀번호 추측 공격 실행:

`wpscan --url {{url}} --usernames {{사용자 명|경로/대상/사용자 명.txt}} --passwords {{경로/대상/비밀번호.txt}} threads {{20}}`

- WPVulnDB (<https://wpvulndb.com/>)에서 취약점 데이터를 수집하여 WordPress 웹사이트 스캔:

`wpscan --url {{url}} --api-token {{토큰}}`

# hashcat

> 빠른 고급 비밀번호 복구 도구.
> 더 많은 정보: <https://hashcat.net/wiki/doku.php?id=hashcat>.

- 기본 hashcat 마스크를 사용하여 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{3}} {{hash_값}}`

- 알려진 4자리 패턴으로 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{3}} {{hash_값}} "{{?d?d?d?d}}"`

- 인쇄 가능한 모든 ASCII 문자 중 최대 8개를 사용하여 무차별 대입 공격(모드 3)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{3}} --increment {{hash_값}} "{{?a?a?a?a?a?a?a?a}}"`

- Kali Linux 상자의 단어 목록을 사용하여 사전 공격(모드 0)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{0}} {{hash_값}} {{/usr/share/wordlists/rockyou.txt}}`

- 일반적인 비밀번호 변형으로 변형된 RockYou 단어 목록을 사용하여 규칙 기반 사전 공격(모드 0)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{0}} --rules-file {{/usr/share/hashcat/rules/best64.rule}} {{hash_값}} {{/usr/share/wordlists/rockyou.txt}}`

- 두 가지 다른 사용자 정의 사전의 단어 연결을 사용하여 조합 공격(모드 1)을 수행:

`hashcat --hash-type {{hash_타입_아이디}} --attack-mode {{1}} {{hash_값}} {{/경로/대상/사전1.txt}} {{/경로/대상/사전2.txt}}`

- 이미 크랙된 해시의 결과를 표시:

`hashcat --show {{hash_값}}`

- 모든 예시 해시 표시:

`hashcat --example-hashes`

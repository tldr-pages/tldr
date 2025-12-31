# vegeta

> HTTP 부하 테스트를 위한 명령줄 도구 및 라이브러리.
> 같이 보기: `ab`.
> 더 많은 정보: <https://github.com/tsenart/vegeta#usage-manual>.

- 30초 동안 공격 시작:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}}`

- 자체 서명된 HTTPS 인증서가 있는 서버에 대한 공격 시작:

`echo "{{GET https://example.com}}" | vegeta attack -insecure -duration={{30s}}`

- 초당 10개의 요청 비율로 공격 시작:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} -rate={{10}}`

- 공격을 시작하고 보고서 표시:

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta report`

- 공격을 시작하고 결과를 그래프에 플롯(시간에 따른 지연):

`echo "{{GET https://example.com}}" | vegeta attack -duration={{30s}} | vegeta plot > {{경로/대상/결과.html}}`

- 파일에 있는 여러 URL에 대한 공격 시작:

`vegeta attack -duration={{30s}} -targets={{requests.txt}} | vegeta report`

# speedread

> 간단한 터미널 기반 오픈 소스 Spritz 유사 도구.
> 입력된 텍스트를 단어별 RSVP(빠른 연속 시각적 표시)로 최적의 읽기 지점에 맞춰 표시하여, 눈이 한 곳에 고정된 상태에서 일반적인 속도보다 훨씬 빠르게 텍스트를 읽을 수 있게 합니다.
> 더 많은 정보: <https://github.com/pasky/speedread>.

- 특정 속도로 텍스트 파일 읽기:

`cat {{경로/대상/파일.txt}} | speedread -wpm {{250}}`

- 특정 줄부터 다시 시작:

`cat {{경로/대상/파일.txt}} | speedread -resume {{5}}`

- 한 번에 여러 단어를 표시:

`cat {{경로/대상/파일.txt}} | speedread -multiword`

- 읽기 중 10% 속도 감소:

`[`

- 읽기 중 10% 속도 증가:

`]`

- 일시 정지하고 마지막 몇 줄을 컨텍스트로 표시:

`<space>`

# argos-translate

> Python으로 작성된 오픈소스 오프라인 번역 라이브러리 및 CLI 도구.
> 더 많은 정보: <https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

- 스페인어에서 영어로 번역하려면 번역 쌍을 설치:

`argospm install translate-es_en`

- 일부 텍스트를 스페인어(`es`)에서 영어(`en`)로 번역 (참고: 두 글자 언어 코드만 지원됨):

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- 텍스트 파일을 영어에서 힌디어로 번역:

`cat {{경로/대상/파일.txt}} | argos-translate --from-lang en --to-lang hi`

- 설치된 모든 번역 쌍 나열:

`argospm list`

- 설치 가능한 영어 번역 쌍 표시:

`argospm search --from-lang en`

- 설치된 언어 패키지 쌍 업데이트:

`argospm update`

- `ar`에서 `ru`로 번역 (참고: 번역 쌍 `translate-ar_en` 및 `translate-en_ru`가 설치되어 있어야 함):

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`

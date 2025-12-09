# oxipng

> PNG 파일의 압축을 무손실로 개선합니다.
> 더 많은 정보: <https://github.com/shssoichiro/oxipng>.

- PNG 파일 압축 (기본적으로 파일을 덮어씀):

`oxipng {{경로/대상/파일.png}}`

- PNG 파일을 압축하고 출력 파일을 새 파일로 저장:

`oxipng --out {{경로/대상/출력.png}} {{경로/대상/파일.png}}`

- 현재 디렉토리의 모든 PNG 파일을 다중 스레드를 사용하여 압축:

`oxipng "*.png"`

- 설정된 최적화 레벨로 파일 압축 (기본값은 2):

`oxipng --opt {{0|1|2|3|4|5|6|max}} {{경로/대상/파일.png}}`

- PNG 인터레이싱 유형 설정 (`0`은 인터레이싱 제거, `1`은 Adam7 인터레이싱 적용, `keep`은 기존 인터레이싱 유지; 기본값은 `0`):

`oxipng --interlace {{0|1|keep}} {{경로/대상/파일.png}}`

- 알파 채널이 있는 이미지에 추가 최적화 수행:

`oxipng --alpha {{경로/대상/파일.png}}`

- 더 느리지만 강력한 Zopfli 압축기를 최대 최적화로 사용:

`oxipng --zopfli --opt max {{경로/대상/파일.png}}`

- 모든 비중요 메타데이터 청크 제거:

`oxipng --strip all {{경로/대상/파일.png}}`

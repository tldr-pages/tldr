# binwalk

> 펌웨어 분석 도구.
> 더 많은 정보: <https://github.com/ReFirmLabs/binwalk>.

- 바이너리 파일 스캔:

`binwalk {{경로/대상/바이너리}}`

- 출력 디렉터리를 지정하여 바이너리에서 파일을 추출:

`binwalk {{[-e|--extract]}} {{[-C|--directory]}} {{출력_디렉토리}} {{경로/대상/바이너리}}`

- 재귀 깊이를 2로 제한하는 바이너리에서 파일을 재귀적으로 추출:

`binwalk {{[-e|--extract]}} {{[-M|--matryoshka]}} {{[-d|--depth]}} {{2}} {{경로/대상/바이너리}}`

- 지정된 파일 서명을 사용하여 바이너리에서 파일을 추출:

`binwalk {{[-D|--dd]}} '{{png image:png}}' {{경로/대상/바이너리}}`

- 바이너리의 엔트로피를 분석하여, 바이너리와 동일한 이름과 `.png` 확장자를 추가하여 플롯을 저장:

`binwalk {{[-E|--entropy]}} {{[-J|--save]}} {{경로/대상/바이너리}}`

- 엔트로피, 서명 및 opcode 분석을 단일 명령으로 결합:

`binwalk {{[-E|--entropy]}} {{[-B|--signature]}} {{[-A|--opcodes]}} {{경로/대상/바이너리}}`

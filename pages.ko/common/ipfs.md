# ipfs

> Inter Planetary File System.
> p2p기반 하이퍼미디어 프로토콜, 웹을 더 개방적으로 만드는 것을 목표로 함.
> 더 많은 정보: <https://docs.ipfs.tech/reference/kubo/cli/>.

- 로컬 파일을 추가하고, pin 처리 후 해시 출력:

`ipfs add {{경로/대상/파일}}`

- 로컬에서 파일시스템으로 디렉터리를 재귀적으로 추가하고 해시 출력:

`ipfs add {{[-r|--recursive]}} {{경로/대상/디렉터리}}`

- 원격 파일을 저장하고 이름 지정하지만, pin 하지 않음:

`ipfs get {{hash}} {{[-o|--output]}} {{경로/대상/파일}}`

- 원격 파일을 로컬에 pin:

`ipfs pin add {{hash}}`

- pin 설정된 파일 목록 출력:

`ipfs pin ls`

- 로컬 저장소에서 pin 해제:

`ipfs pin rm {{hash}}`

- 로컬 저장소에서 pin되지 않은 파일 정리:

`ipfs repo gc`

# git unpack-objects

> 압축된 아카이브에서 Git 객체를 추출하는 명령.
> 더 많은 정보: <https://git-scm.com/docs/git-unpack-objects>.

- 객체를 추출하지 않고 팩 파일 처리 과정 시뮬레이션:

`git < {{팩_파일.pack}} unpack-objects -n`

- 일반적으로 표시되는 진행률 출력 억제:

`git < {{팩_파일.pack}} unpack-objects -q`

- 손상된 팩 파일에서 첫 번째 손상 지점을 넘어 객체 추출 계속 진행:

`git < {{팩_파일.pack}} unpack-objects -r`

- 내용이나 참조가 손상된 객체는 저장하지 않음:

`git < {{팩_파일.pack}} unpack-objects --strict`

- 팩 파일 크기가 지정한 `크기`를 초과하면 오류와 함께 종료:

`git < {{팩_파일.pack}} unpack-objects --max-input-size={{크기}}`

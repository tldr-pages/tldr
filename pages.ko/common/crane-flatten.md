# crane flatten

> 이미지의 레이어를 단일 레이어로 병합.
> 태그가 지정되지 않은 경우, 다이제스트를 원본 이미지 저장소에 푸시.
> 더 많은 정보: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- 이미지 병합:

`crane flatten`

- 병합된 이미지에 새로운 태그 적용:

`crane flatten {{[-t|--tag]}} {{태그_이름}}`

- 도움말 표시:

`crane flatten {{[-h|--help]}}`

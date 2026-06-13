# apptainer sign

> SIF 컨테이너 이미지에 디지털 서명을 추가하는 도구.
> 관련 항목: `apptainer-verify`.
> 더 많은 정보: <https://apptainer.org/docs/user/main/cli/apptainer_sign.html>.

- 기본 PGP 키를 사용하여 컨테이너 이미지 서명:

`apptainer sign {{경로/대상/이미지.sif}}`

- 특정 개인 키 파일을 사용하여 서명:

`apptainer sign --key {{경로/대상/개인키.pem}} {{경로/대상/이미지.sif}}`

- 특정 PGP 키 인덱스를 사용하여 서명:

`apptainer sign {{[-k|--keyidx]}} {{키_인덱스}} {{경로/대상/이미지.sif}}`

- 이미지 내 특정 객체 그룹에 서명:

`apptainer sign {{[-g|--group-id]}} {{그룹_아이디}} {{경로/대상/이미지.sif}}`

- 이미지 내 특정 객체 ID에 서명:

`apptainer sign {{[-i|--sif-id]}} {{객체_아이디}} {{경로/대상/이미지.sif}}`

- 도움말 표시:

`apptainer sign {{[-h|--help]}}`

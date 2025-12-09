# packer

> 자동화된 머신 이미지를 빌드.
> 더 많은 정보: <https://developer.hashicorp.com/packer/docs/commands>.

- 이미지 빌드:

`packer build {{경로/대상/config.json}}`

- Packer 이미지 구성의 구문 확인:

`packer validate {{경로/대상/config.json}}`

- Packer 이미지 구성 포맷:

`packer fmt {{경로/대상/config.pkr.hcl}}`

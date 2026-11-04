# vagrant upload

> 호스트에서 게스트 machine으로 파일과 디렉터리를 업로드.
> 더 많은 정보: <https://developer.hashicorp.com/vagrant/docs/cli/upload>.

- 호스트의 파일 또는 디렉터리를 게스트 machine으로 업로드:

`vagrant upload {{경로/대상/소스_파일_또는_디렉터리}} {{경로/대상/목적지_파일_또는_디렉터리}} {{이름|id}}`

- 파일 또는 디렉터리를 압축한 후, 게스트 머신으로 업로드:

`vagrant upload --compress {{경로/대상/소스_파일_또는_디렉터리}} {{경로/대상/목적지_파일_또는_디렉터리}} {{이름|id}}`

- 사용할 압축 형식 지정. (기본값: `zip`):

`vagrant upload --compression-type {{tgz|zip}} {{경로/대상/소스_파일_또는_디렉터리}} {{경로/대상/목적지_파일_또는_디렉터리}} {{이름|id}}`

- 게스트 machine에 임시 위치를 생성하고 해당 위치로 파일 업로드:

`vagrant upload --temporary {{경로/대상/소스_파일_또는_디렉터리}} {{경로/대상/목적지_파일_또는_디렉터리}} {{이름|id}}`

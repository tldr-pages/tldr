# git force-clone

> `git clone`의 기본 기능을 제공하지만, 대상 Git 저장소가 이미 존재하는 경우 원격의 클론으로 강제 리셋합니다.
> `git-extras`의 일부입니다.
> 더 많은 정보: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- 새로운 디렉토리에 Git 저장소 클론:

`git force-clone {{원격_저장소_위치}} {{경로/대상/폴더}}`

- 특정 브랜치를 체크아웃하여 새로운 디렉토리에 Git 저장소 클론:

`git force-clone -b {{브랜치_이름}} {{원격_저장소_위치}} {{경로/대상/폴더}}`

- 기존 Git 저장소 디렉토리에 Git 저장소 클론, 원격과 유사하게 강제 리셋을 수행하고 특정 브랜치를 체크아웃:

`git force-clone -b {{브랜치_이름}} {{원격_저장소_위치}} {{경로/대상/폴더}}`

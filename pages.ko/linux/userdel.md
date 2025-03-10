# userdel

> 사용자 계정을 삭제하거나 사용자를 그룹에서 제거합니다.
> 같이 보기: `users`, `useradd`, `usermod`.
> 더 많은 정보: <https://manned.org/userdel>.

- 사용자 삭제:

`sudo userdel {{사용자명}}`

- 다른 루트 디렉토리에서 사용자 삭제:

`sudo userdel {{[-R|--root]}} {{경로/대상/다른/루트}} {{사용자명}}`

- 홈 디렉토리 및 메일 스풀과 함께 사용자 삭제:

`sudo userdel {{[-r|--remove]}} {{사용자명}}`

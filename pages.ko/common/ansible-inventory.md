# ansible-inventory

> Ansible 인벤토리를 표시하거나 덤프.
> 또한, `ansible`을 참조하세요.
> 더 많은 정보: <https://docs.ansible.com/ansible/latest/cli/ansible-inventory.html>.

- 기본 인벤토리를 표시:

`ansible-inventory --list`

- 사용자 지정 인벤토리를 표시:

`ansible-inventory --list {{[-i|--inventory-file]}} {{경로/대상/파일_또는_스크립트_또는_디렉토리}}`

- YAML에서 기본 인벤토리를 표시:

`ansible-inventory --list {{[-y|--yaml]}}`

- 기본 인벤토리를 파일에 덤프:

`ansible-inventory --list --output {{경로/대상/파일}}`

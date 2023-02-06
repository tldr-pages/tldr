# toolbox create

> Hozzon létre egy új `toolbox` konténert. További információ: <https://manned.org/toolbox-create.1>.

- Hozzon létre egy `toolbox` konténert egy adott disztribúcióhoz:

`toolbox create --distro {{distribution}}`

- Hozzon létre egy `toolbox` konténert az aktuális disztribúció egy adott kiadásához:

`toolbox create --release {{release}}`

- Hozzon létre egy `toolbox` konténert egy egyéni lemezképpel:

`toolbox create --image {{name}}`

- `toolbox` konténer létrehozása egy egyéni Fedora-képből:

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:36}}`

- Hozzon létre egy `toolbox` konténert a Fedora 36 alapértelmezett képével:

`toolbox create --distro {{fedora}} --release {{f36}}`

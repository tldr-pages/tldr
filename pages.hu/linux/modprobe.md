# modprobe

> Modulok hozzáadása vagy eltávolítása a Linux kernelből. További információ: <https://manned.org/modprobe>.

- Tegyünk úgy, mintha egy modult töltenénk be a kernelbe, de valójában nem tesszük meg:

`sudo modprobe --dry-run {{module_name}}`

- Modul betöltése a kernelbe:

`sudo modprobe {{module_name}}`

- Modul eltávolítása a kernelből:

`sudo modprobe --remove {{module_name}}`

- Egy modul és a tőle függő modulok eltávolítása a kernelből:

`sudo modprobe --remove-dependencies {{module_name}}`

- Egy kernelmodul függőségének megjelenítése:

`sudo modprobe --show-depends {{module_name}}`

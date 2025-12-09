# lynis

> Sistem ve güvenlik denetim aracı.
> Daha fazla bilgi için: <https://cisofy.com/documentation/lynis/>.

- Kullandığınız Lynis sürümünün güncelliğini denetleyin:

`sudo lynis update info`

- Sistemde güvenliğinizi denetleyin:

`sudo lynis audit system`

- Belirtilen Dockerfile'ın güvenlik denetimini yapın:

`sudo lynis audit dockerfile {{dockerfile/dizin/yolu}}`

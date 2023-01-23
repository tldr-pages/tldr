# salt-call

> A salt helyi meghívása egy salt minionon. További információ: <https://docs.saltstack.com/ref/cli/salt-call.html>.

- Végezzen egy highstate-ot ezen a minionon:

`salt-call state.highstate`

- Highstate szárazfutás végrehajtása, az összes változás kiszámítása, de valójában nem hajtja végre azokat:

`salt-call state.highstate test=true`

- Végezzen el egy highstate-et verbózus hibakijelzéssel:

`salt-call -l debug state.highstate`

- Listázza ki ennek a minionnak a szemcséit:

`salt-call grains.items`

# ip

> Ukazuje/nastavuje routování, zařízení, pravidla routování a tunely.
> Některé dílčí příkazy jako je `address` mají svou vlastní dokumentaci.
> Více informací: <https://manned.org/ip.8>.

- Vypsat rozhraní s podrobnými informacemi:

`ip {{[a|address]}}`

- Vypsat rozhraní se stručnými informacemi o síťové vrstvě:

`ip {{[-br|-brief]}} {{[a|address]}}`

- Vypsat rozhraní se stručnými informacemi o linkové vrstvě:

`ip {{[-br|-brief]}} {{[l|link]}}`

- Zobrazit routovací tabulku:

`ip {{[r|route]}}`

- Ukázat sousedy (ARP tabulka):

`ip {{[n|neighbour]}}`

- Změnit rozhraní nahoru/dolů:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{up|down}}`

- Přidat/Smazat IP adresu k rozhraní:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{maska}} dev {{ethX}}`

- Přidat výchozí cestu:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{ethX}}`

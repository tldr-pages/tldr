# Stylová Příručka

Tato stránka vypisuje specifické instrukce pro formátování `tldr` stránek.

## Obsah 

1. [Obecné rozvržení](#obecné-rozvržení)
2. [Stránky](#stránky)
3. [Obecné psaní](#obecné-psaní)
4. [Nadpisy](#nadpisy)

## Obecné rozvržení

Základní formátování každé stránky by mělo odpovídat následujicí šabloně a mít nejvýše 8 příkladů příkazů:

```md
# název příkazu

> Krátký, stručný popisek příkazu.
> Nejlépe na jeden řádek; dva řádky jsou přijatelné pokud je to nutné.
> Více informací: <https://example.com/nazev_prikazu/help/stranka>.

- Popisek kódu:

`název_příkazu možnosti`

- Popisek kódu:

`název_příkazu možnosti`

...
```

Příklad:

```md
# krita

> Skicovací a malovací program určený pro digitální umělce.
> Viz také: `gimp`.
> Více informací: <https://docs.krita.org/en/reference_manual/linux_command_line.html>.


- Spustit Krita:

`krita`

- Otevřít specifické soubory:

`krita {{cesta/k/obrazku1 cesta/k/obrazku2 ...}}`

- Spustit bez úvodní obrazovky:

`krita --nosplash`

- Spustit s konkrétní pracovná plochou:

`krita --workspace {{Animation}}`

- Spustit v režimu celé obrazovky:

`krita --fullscreen`
```

> [!NOTE]\
> Název souboru stránky a nadpisek musí přesně odpovídat název příkazu. Nadpisek stránky může být velkými i malými písmeny, zatímco názvy souborů Markdown musí být malými písmeny.

Je zde nastaven linter který vynucuje výše uvedené formátování. Spouští se automaticky při každém pull requestu, ale je možné ho instalovat pro testování vašich příspěvků lokálně před odesláním:

```sh
npm install --global tldr-lint
tldr-lint cesta/k/tldr_strance.md
```

Pro jiné způsoby jak použít `tldr-lint`, například lintování celého adresáře se podívejte na
[`tldr stránka na tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md). Případně můžete použít alias `tldrl`.

V závislosti na vašem klientu, můžete si zobrazit náhled stránky lokálně pomocí vlajky `--render`:

```sh
tldr --render cesta/k/tldr_strance.md
```
## Stránky 

### Rozdíly mezi platformami

Pokud se obáváte, že příkazy se mohou lišit mezi platformami nebo operačními systémy (např. Windows vs macOS), většina [tldr klientských stránek](https://github.com/tldr-pages/tldr/wiki/Clients) vybere nejvíce vhodnou verzi příkazu při zobrazení koncovému uživateli.

V tomto případě, informace o Windows verzi příkazu `cd` (uložené v `pages/windows/cd.md`) budou automaticky zobrazeny uživatelům Windows, a obecná/společná verze (uložena v `pages/common/cd.md`) bude zobrazena pro Linux, macOS, a uživatelům jiných platformách.

Pokuste se sladit název souboru stránky s vyvolaným příkazem. Pokud je to možné, nepoužívejte názvy projektů. Cílem je být vůči uživateli co nejvíce transparentní, když je o příkazu zvědavý.

### Alias

Pokud lze příkaz vyvolat alternativními názvy (např. `vim` lze vyvolat pomocí `vi`), alias stránky lze vytvořit pro nasměrování uživatele na původní název příkazu.

```md
# název_příkazu

> Tento příkaz je aliasem pro `původní-název-příkazu`.

- Podívejte se na dokumentaci původního příkazu:

`tldr původní-název-příkazu`
```

Příklad:

```md
# vi

> Tento příkaz je aliasem pro `vim`.

- Podívejte se na dokumentaci původního příkazu:

`tldr původní-název-příkazu`
```

- Předem přeložené šablony alias stránek můžete najít [zde](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md).

# Obecné psaní

### Důraz

Nepoužívejte *kurzívu*, **tučnost** nebo jakýkoli jiný styl textu na stránkách. Ty jsou vyhrazené pro klientské zdůraznění.

### Rozkazovací způsob

- **Všechny popisky musí být v rozkazovacím způsobu.**
- To se také vztahuje na všechny překlady pokud není jinak uvedeno v sekci pro konkrétní jazyk.

Při psaní popisků pro příklady příkazů, **zkontrolujte gramatické chyby**. `Přesun do zadaného adresáře` je preferované namísto:

- `Přecházení do zadaného adresáře` (nemělo by být v přítomném příčestí)
- `Tento příkaz přejde do zadaného adresáře` (je zřejmé, že tento příklad funguje pro *tento* komentář)
- `Přejděme do zadaného adresáře!`
- `Změna adresáře` (pokud je to možné, použijte činný rod místo trpného)

Například místo `Vypisuje všechny soubory:`, použijte následující:

```md
- Vypsat všechny soubory:

 `ls`
```

# Nadpisy

### Popisek programu

- Vyhněte se používáním nadpisu stránky v popisku (např. použijte `Skicovací a malovací program určený pro digitální umělce.` místo `Krita je skicovací a malovací program určený pro digitální umělce`)
- Pokud se název programu liší od názvu kterým se spouští, lze jej uvést na začátku nadpisu (např. `rg` a Ripgrep).
- Vyhněte se zmínkám o tom, že se program používá v příkazovém řádku (např. použijte `Ripgrep, rekurzivní řádkově-orientovaný vyhledávací nástroj` místo `Ripgrep, rekurzivní řádkově-orientovaný CLI vyhledávací nástroj`).

Například, při psaní dokumentace pro `cd`, nástroj pro přesun do jiného adresáře v Terminálu nebo Příkazovém Řádku, **nepište** zdlouhavý popisek jako:

```md
> `cd` je systémový nástroj, dostupný na Windows, macOS a Linux, pro přesun do jiného adresáře v příkazovém Řádku, Terminálu, a PowerShellu.
```

Místo toho by měl být zjednodušen pro snadnější čtení:

```md
> Přesun do jiného adresáře.
```

### Odkazy Více informací

- Na odkazovém řádku `Více informací`, uveďte přímý odkaz k dokumentaci který popisuje jak používat daný příkaz. Preferujeme odkazovat dokumentaci poskytovanou autorem, ale pokud není dostupná nebo obsahuje velmi málo informací, použijte <https://manned.org> jako výchozí záložní odkaz pro všechny platformy (s výjimkou `osx` a platformy BSD mimo FreeBSD)

Pokud stránku dokumentace nelze najít, můžete odkázat na stránku autora nebo tutoriál od třetí strany.
- Zachovejte odkaz více informací krátký. Pokud je to možné zbavte se nadbytečného textu. Například použijte https://manned.org/partclone místo https://manned.org/man/partclone.8 pokud existují dvě různé stránky manuálu pro příkaz napříč distribucemi/platformami tj. `příkaz.1` a `příkaz.8`.

- Pro `osx`: Apple distribuuje zabudováné stránky manuálu [v Xcode](https://developer.apple.com/documentation/os/reading_unix_manual_pages).

Pro příkazy zdokumentované tam, doporučujeme používat <https://keith.github.io/xcode-man-pages/>, HTML export všech Apple stránek manuálu spolu s Xcode.

> [!IMPORTANT]
> Všechny odkazy musí být uzavřené v lomených závorkách (`<` a `>`) pro správné renderování na klientech.

- Je doporučeno používat odkaz pro více informací s Anglickýcm obsahem v přeložených i Anglických stránkách. Protože se odkazy nakonec změní, ale překlady často nejsou synchronizované s Anglickými stránkami.

#### Verzované odkazy

Pokud má nástroj nebo distribuce verzované odkazy pro balíčky, odkažte nejnovější verzi dokumentace nebo žádnou pokud webová stránka automaticky přesměruje k nejnovější verzi dokumentace.

Například, použijte:

- <https://manpages.debian.org/latest/apt/apt.8.html> místo <https://manpages.debian.org/bookworm/apt/apt.8.en.html>.
- <https://docs.aws.amazon.com/cdk/latest/guide/cli.html> místo <https://docs.aws.amazon.com/cdk/v2/guide/cli.html>.

#### Odkazy s místním nastavením

Při odkazování na webové stránky které mají místní nastavení jako odkazy Microsoft Learn, odstraňte informace o místním nastavení z adresy pokud webová stránka automaticky přesměruje na preferované místní nastavení čtenáře. 
Například, použijte <https://learn.microsoft.com/windows-server/administration/windows-commands/cd> místo
<https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd>.

### Sekce Viz také

- Pro odkazování souvicejícího příkazu nebo podpříkazu použijte:

```md
> Viz také: `příkaz`.
```

- Pro odkazování souvicejících příkazů nebo podpříkazů použijte:

```md
> Viz také: `příkaz1`, `příkaz2`, `příkaz3`.
```

- Pokud má příkaz podpříkazy, tyto stránky jde odkázat následujícím řádkem. Všimněte si, že jsou vypsány pouze podpříkazy:

```md
> Některé dílčí příkazy jako je `commit`, `add`, `branch`, `switch`, `push`, atd. mají svou vlastní dokumentaci.
```

#### Pořadí nadpisů

Nadpisy by měly dodržovat následující pořadí:

```md
> Krátký popisek funkčnosti.
> Další objasnění funkčnosti.
> Poznáma: Jakákoli poznámka k používání.
> Některé dílčí příkazy jako je `podpříkaz1`, `podpříkaz2` mají svou vlastní dokumentaci.
> Viz také: `příkaz`.
> Více informací: <https://example.com>.
```

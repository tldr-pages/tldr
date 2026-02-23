# Stylová Příručka

Tato stránka vypisuje specifické instrukce pro formátování `tldr` stránek.

## Obecné rozvržení

Základní formátování každé stránky by mělo odpovídat následujicí šabloně a mít nejvýše 8 příkladů příkazů:

```md
# název příkazu

> Krátký, stručný popisek příkazu.
> Nejlépe na jeden řádek; dva řádky jsou přijatelné pokud je to nutné.
> Více informací: <https://priklad.com/nazev_prikazu/help/stranka>.

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

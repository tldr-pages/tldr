#համար

> Կատարեք հրաման մի քանի անգամ:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>:.

- Կրկնել հրամանի տողի պարամետրերի միջոցով.:

`for {{variable}}; do {{echo $variable}}; done`

- Կատարեք տրված հրամանները նշված կետերից յուրաքանչյուրի համար.:

`for {{variable}} in {{item1 item2 ...}}; do {{echo "Loop is executed"}}; done`

- Կրկնել թվերի տրված միջակայքում.:

`for {{variable}} in {{{from..to..step}}}; do {{echo "Loop is executed"}}; done`

- Կրկնել ֆայլերի տվյալ ցանկի վրա.:

`for {{variable}} in {{path/to/file1 path/to/file2 ...}}; do {{echo "Loop is executed"}}; done`

- Կրկնել դիրեկտորիաների տվյալ ցանկի վրա.:

`for {{variable}} in {{path/to/directory1/ path/to/directory2/ ...}}; do {{echo "Loop is executed"}}; done`

- Կատարեք տրված հրաման յուրաքանչյուր գրացուցակում.:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "Loop is executed"}}) done`

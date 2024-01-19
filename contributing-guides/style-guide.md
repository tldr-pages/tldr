# Style guide

This page lists specific formatting instructions for `tldr` pages.

## Layout

The basic format of each page should match the following template and have at most 8 command examples:

```md
# command name

> Short, snappy command description.
> Preferably one line; two are acceptable if necessary.
> More information: <https://example.com/command_name/help/page>.

- Code description:

`command_name options`

- Code description:

`command_name options`

...
```

Example:

```md
# krita

> A sketching and painting program designed for digital artists.
> See also: `gimp`.
> More information: <https://docs.krita.org/en/reference_manual/linux_command_line.html>.

- Start Krita:

`krita`

- Open specific files:

`krita {{path/to/image1 path/to/image2 ...}}`

- Start without a splash screen:

`krita --nosplash`

- Start with a specific workspace:

`krita --workspace {{Animation}}`

- Start in fullscreen mode:

`krita --fullscreen`
```

> [!NOTE]
> The filename and page title must match the command name exactly. The page title can be present in any case, whereas the filenames must be lowercase.

There is a linter that enforces the format above.
It is run automatically on every pull request,
but you may install it to test your contributions locally before submitting them:

```sh
npm install --global tldr-lint
tldr-lint path/to/tldr_page.md
```

For other ways to use `tldr-lint`, such as linting an entire directory, check out (what else!)
[`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md). Alternatively, you can also use its alias `tldrl`.

Your client may be able to preview a page locally using the `--render` flag:

```sh
tldr --render path/to/tldr_page.md
```

### PowerShell-Specific Rules

When documenting PowerShell commands, please take note of the following naming conventions.

- The name of the file name must be written in lowercase, such as `invoke-webrequest.md` instead of `Invoke-WebRequest.md`.
- The page title/heading must be written as-is (matching the spelling intended by Microsoft or the PowerShell module author), such as `Invoke-WebRequest` instead of `invoke-webrequest`.
- The command name and options in the examples should also be written as-is, such as `Command-Name {{input}} -CommandParameter {{value}}` instead of `command-name {{input}} -commandparameter {{value}}`.

Due to [various compatibility differences](https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell) and removed Windows-specific commands in PowerShell 6.x, Ensure that the command works on between **PowerShell 5.1** (aka. the "Legacy Windows PowerShell" as installed in Windows 10 and 11), and the **latest version of the Cross-Platform PowerShell** (formerly known as PowerShell Core). If the command or its options is unavailable or contains different behavior between each version, please kindly note them in the descriptions. For example,

```md
# Clear-RecycleBin

> Clear items from the Recycle Bin.
> This command can only be used through PowerShell versions 5.1 and below, or 7.1 and above.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/clear-recyclebin>.
```

## Aliases

If a command can be called with alternative names (like `vim` can be called by `vi`), alias pages can be created to point the user to the original command name.

```md
# command_name

> This command is an alias of `original-command-name`.
> More information: <https://example.com/original/command/help/page>.

- View documentation for the original command:

`tldr original_command_name`
```

Example:

```md
# vi

> This command is an alias of `vim`.

- View documentation for the original command:

`tldr vim`

```

- Pre-translated alias page templates can be found [here](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md).

### PowerShell-Specific Aliases

Some PowerShell commands may introduce aliases which fall into one of these three categories:

**1. Substituting an existing Windows Command Prompt (`cmd`) command**, such as `cd` aliasing to `Set-Location` with different command options. In this case, add the following alias note into the second line of the original Command Prompt command's tldr description, for example:

```md
# cd

> Display the current working directory or move to a different directory.
> In PowerShell, this command is an alias of `Set-Location`. This documentation is based on the Command Prompt (`cmd`) version of `cd`.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- View documentation of the equivalent PowerShell command:

`tldr set-location`
```

> [!TIP]
> The "View documentation of the equivalent PowerShell command" example is optional and may be excluded if the page already has the maximum number (8) of examples.

**2. Provides a new alias but only executable in PowerShell**, such as `ni` for `New-Item`. In this case, use the [standard alias template](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/translation-templates/alias-pages.md), but add the word "In Powershell," (or equivalent) to indicate that the command is exclusive to PowerShell. For example,

```md
# ni

> In PowerShell, this command is an alias of `New-Item`.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- View documentation for the original command:

`tldr new-item`
```

**3. Provides a new alias that conflicts with other programs**, most notoriously the inclusion of `curl` and `wget` as aliases of `Invoke-WebRequest` (with a non-compatible set of command options). Note that PowerShell system aliases that fall into this category are commonly exclusive to Windows.

In this case, provide a note and method to determine whether the command currently refers to a PowerShell command (by alias) or others. For example,

```md
# curl

> In PowerShell, this command may be an alias of `Invoke-WebRequest` when the original `curl` program (<https://curl.se>) is not properly installed.
> More information: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Check whether `curl` is properly installed by printing its version number. If this command evaluates into an error, PowerShell may have substituted this command with `Invoke-WebRequest`:

`curl --version`

- View documentation for the original `curl` command:

`tldr curl -p common`

- View documentation for PowerShell's `Invoke-WebRequest` command:

`tldr invoke-webrequest`
```

## Option syntax

- Use **GNU-style long options** (like `--help` rather than `-h`) when they are cross-platform compatible (intended to work the same across multiple platforms).
- When documenting PowerShell commands, use **PowerShell-style long options** (like `-Help` instead of `-H`).
- When long options aren't available for a command, use **short options** instead.
- While we prefer long options, we allow special cases in commands like `pacman` where short options are widely used and preferred over the long options (for cases like these decisions will be made by the maintainers on a case-by-case basis).
- We prefer using a space instead of the equals sign (`=`) to separate options from their arguments (i.e. use `--opt arg` instead of `--opt=arg`) unless the program does not support it.

> [!NOTE]  
> The goal of using long options is to make the commands easier to read and understand for non-technical users. While it is ideal for most users, some users prefer the short option for better ease of use. If the command supports both options, we can highlight the short options using mnemonics instead.

### Short option mnemonics

Short option mnemonics are optional hints which can be added to help users understand the meaning of these short options. The assigned mnemonics should match with the ones in the command's official documentation (e.g. from `man` or `Get-Help`). For example:

```md
- [d]isplay the ins[t]allation [i]D for the current device. Useful for offline license activation:

`slmgr.vbs /dti`

- Display the current license's e[xp]i[r]ation date and time:

`slmgr.vbs /xpr`
```

Note that, in the first example, the `[d]`, `[t]`, and `[i]` characters are enclosed with square brackets to indicate that the `/dti` option of the command is a combination of "display", "installation", and "ID", respectively. Consecutive mnemonic characters can be grouped under the same square brackets, such as `e[xp]i[r]ation` instead of `e[x][p]i[r]ation`.

**Mnemonic characters must be written in a case-sensitive manner**, even when it is placed as the first character of the sentence (i.e. use `[d]isplay` instead of `[D]isplay`). This is to avoid conflicts with GNU-style command options which may interpret uppercase options differently than the lowercase ones, such as `-v` for displaying the command's `[v]ersion` number and `-V` to run the command in `[V]erbose` mode.

Option mnemonics may also be used in translations as long as the highlighted word contains similar meanings to the language (commonly English) which the command is written for. For example, `[d]ownload` in English may be translated into `[d]escargar` in Spanish, `[i]nstall` in English may be translated to `[i]nstallieren` in German, and `[a]pp` in English may be translated into `[a]plikasi` in Indonesian and Malay.

> [!NOTE]  
> In cases where the character isn't present in the translated word, you can highlight the option before/next to the equivalent word or you can add the English work beside the translation inside a bracket. For example, `E[x]tract` in English maybe translated into `[x] ekstrak` or `ekstrak [x]` or `ekstrak (E[x]tract)` in Indonesian.

## Placeholder syntax

User-provided values should use the `{{placeholder}}` syntax
in order to allow `tldr` clients to highlight them.

Keep the following guidelines in mind when choosing placeholders:

### Naming

- Use short but descriptive placeholders,
  such as `{{path/to/source_file}}` or `{{path/to/wallet.txt}}`.
- Use [`snake_case`](https://wikipedia.org/wiki/snake_case) for multi-word placeholders.
- Use a generic placeholder rather than an actual value where a generic placeholder is available (but there is an exception to this listed below). For example, use
  `iostat {{1..infinity}}` rather than `iostat {{2}}`.
  - If there are several consecutive placeholders of the same type
  which don't allow adding arbitrary text in them (ranges), then instead of generic placeholders use descriptive ones. For example prefer `input swipe {{x_position}} {{y_position}} {{x_position}} {{y_position}} {{seconds}}`
  instead of `input swipe {{-infinity..infinity}} {{-infinity..infinity}} {{-infinity..infinity}} {{-infinity..infinity}} {{1..infinity}}`.

### Paths

- Use `{{filename}}` when just the file name is expected.
- For any reference to paths of files or directories,
  use the format `{{path/to/<placeholder>}}`,
  except when the location is implicit.
- When the path cannot be relative,
  but has to start at the root of the filesystem,
  prefix it with a slash,
  such as `get {{/path/to/remote_file}}`.
- In case of a possible reference both to a file or a directory,
  use `{{path/to/file_or_directory}}`.

> [!NOTE]  
> If the command is specific to Windows, use backslashes (`\`) instead, such as `{{path\to\file_or_directory}}`. Drive letters such as `C:` are optional unless the command input requires an absolute path or specific drive letter range, such as `cd /d {{C}}:{{path\to\directory}}`.

### Extensions

- If a particular extension is expected for the file, append it.
  For example, `unrar x {{path/to/compressed.rar}}`.
- In case a generic extension is needed, use `{{.ext}}`, but **only** if an extension is required.
  For instance, in `find.md`'s example "Find files by extension" (`find {{path/to/root}} -name '{{*.ext}}'`)
  using `{{*.ext}}` explains the command without being unnecessarily specific;
  while in `wc -l {{path/to/file}}` using `{{path/to/file}}` (without extension) is sufficient.

### Grouping placeholders

- If a command can take 0 or more arguments of the same kind, use an ellipsis: `{{placeholder1 placeholder2 ...}}`.
  For instance, if multiple paths are expected `{{path/to/directory1 path/to/directory2 ...}}` can be used.
- If a command can take 0 or more arguments of different kinds, use an ellipsis: `{{placeholder1|placeholder2|...}}`.
  If there are more than 5 possible values, you can use `|...` after the last item.
- It's impossible to restrict the minimum or (and) maximum placeholder count via `ellipsis`.

It's up to the program to decide how to handle duplicating values, provided syntax
tells no info about whether items are mutually exclusive or not.

### Special cases

- If a command performs irreversible changes to a file system or devices,
  write every example in a way that cannot be copy pasted thoughtlessly.
  For example, instead of `ddrescue --force --no-scrape /dev/sda /dev/sdb`
  write `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}`
  and use the `{{/dev/sdXY}}` placeholder for *block devices* instead of `/dev/sda1`.

In general, placeholders should make it as intuitive as possible
to figure out how to use the command and fill it in with values.

Technical wording on description lines should use the `backtick` syntax.
Use backticks on the following:

- Paths, e.g. `package.json`, `/etc/package.json`.
- Extensions, e.g. `.dll`.
- Commands, e.g. `ls`.
- Standard streams: `stdout`, `stdin`, `stderr`. **Do not** use the full names (e.g. standard output).

## Descriptions

- Avoid using the page title in the description (e.g. use `A sketching and painting program designed for digital artists` instead of `Krita is a sketching and painting program designed for digital artists`) unless the program name differs from the executable name (e.g. `rg` and Ripgrep).
- Avoid mentioning that the program is used on the command-line (e.g. use `Ripgrep is a recursive line-oriented search tool` instead of `Ripgrep is a recursive line-oriented CLI search tool`).
- Brand and project names can be capitalized in the description whenever applicable (e.g. use `A tool for interacting with a Git repository.` instead of ``A tool for interacting with a `git` repository.``).
- Acronym expansions (i.e. protocols, tools, etc) must not be translated unless there is a recognized native equivalent for them.
- When documenting keycaps or a keyboard shortcut for a utility it is suggested to wrap them in backticks to make them stand out in the description (i.e. ``Print the last lines of a given file and keep reading file until `Ctrl + C`:``). Alternatively, you can document them as a separate command and optionally highlight them as placeholders (i.e. `:wq{{Enter}}` or `:wq<Enter>` or `:wq(Enter)`).

### Imperative Mood

- **All descriptions must be concise and phrased in the imperative mood.**
- This also applies to all translations by default unless otherwise specified in the language-specific section below.
- For example, when writing documentation for `cd`, a tool to check out and work on a specific directory in the Terminal or Command Prompt, **do not** write a lengthy description such as:

```md
> `cd` is a system tool, available in Windows, macOS, and Linux, to check out a specific directory to get things done in the Command Prompt, Terminal, and PowerShell.
```

It should instead be simplified to make it easier for everyone to read:

```md
> Change the current working directory.
```

If you are afraid the commands may differ between platforms or operating systems (e.g. Windows vs macOS), most [tldr pages clients](https://github.com/tldr-pages/tldr/wiki/tldr-pages-clients) will choose the most suitable version of the command.

In this case, the information of the Windows version of `cd` (stored in `pages/windows/cd.md`) will be displayed by default to Windows users, and a generic/common version (stored in `pages/common/cd.md`) will be displayed for Linux, macOS, and other platforms.

When writing descriptions for command examples, **check for any grammatical errors**. `Go to the specified directory` is preferred instead of:

- `Going to the specified directory` (should not be in present participle form)
- `This command will go to the specified directory` (it is clear that this example works for *this* comment)
- `Let's go to the specified directory!`
- `Directory change` (use the active form instead of passive, if possible)

For instance, instead of `Listing all files:`, `List all files:` can be used as the example's description below:

```md
- Listing all files:

 `ls`
```

## Emphasis

Do not use *italics*, **boldface** or any other text styling in the pages. These are reserved for client emphasis of placeholders.

## Serial Comma

- When declaring a list of 3 or more items,
use a [serial comma](https://en.wikipedia.org/wiki/Serial_comma),
also known as the Oxford comma,
since omitting it can create ambiguity.

> Delete the Git branches, tags and remotes.

The example above does not use a serial comma, so this could mean one of two things:

- Delete the Git branches named `tags` and `remotes`.
- Delete all of the following: Git branches, Git tags, and Git remotes.

This can be resolved by inserting a comma before the "and" or "or" in the final element in the list.

> Delete the Git branches, tags, and remotes.

## See also section

- To reference a related command or subcommand, use:

```md
> See also: `command`.
```

- To reference related commands or subcommands, use:

```md
> See also: `command1`, `command2`, `command3`.
```

- Optionally, you can add a short description beside the referenced pages:

``See also: `date`, for Unix information; `umount`, for unmounting partitions.``
## More information links

- On the `More information` link line, we prefer linking to the author's provided documentation of the command line reference or the man page. When not available, use <https://manned.org> as the default fallback for all platforms (except `osx` and some BSD platforms). Alternatively, you can link to the author's website or a tutorial page if the command doesn't have a documentation page.

- **All links must be enclosed inside angular brackets (`<` and `>`) for proper rendering in clients.**

- We prefer translations to use the more information link of the English page by default.

### Versioned links

When a utility or distribution has versioned links for the packages, we prefer linking to the most recent version of documentation (i.e. `latest`) or none if the website automatically redirects to the latest version of the documentation.

For example, use:

- <https://manpages.debian.org/latest/apt/apt.8.html> instead of <https://manpages.debian.org/bookworm/apt/apt.8.en.html>.
- <https://docs.aws.amazon.com/cdk/latest/guide/cli.html> instead of <https://docs.aws.amazon.com/cdk/v2/guide/cli.html>.

### Microsoft Learn links

When linking pages to the Microsoft Learn links, remove the locale from the address as the website will automatically redirect to the reader's preferred locale setting. For example, Use <https://learn.microsoft.com/windows-server/administration/windows-commands/cd> instead of
<https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cd>.

Additionally, if the link is related to PowerShell command documentation, remove the **documentation version indicator** (in which the version of PowerShell/module that the documentation is derived from), aka. the part of the address that starts with `?view=`.

- Use <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/select-string> instead of <https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-string?view=powershell-7.4>.
- Use <https://learn.microsoft.com/powershell/module/powershellget/install-module> instead of <https://learn.microsoft.com/en-us/powershell/module/powershellget/install-module?view=powershellget-1.x>.

## Help and version commands

- We generally place the help and version commands at the **last part of the page** to highlight more practical commands at the beginning of the page.
- For consistency, we prefer generic wording `Display help` and `Display version` for these commands.

## Language-Specific Rules

The below section contains additional language-specific rules for translating pages:

### Chinese-Specific Rules

When Chinese words, Latin words and Arabic numerals are written in the same sentence, more attention must be paid to copywriting.

The following guidelines are applied to Chinese (`zh`) and traditional Chinese (`zh_TW`) pages:

1. Place one space before/after English words and numbers.

- For example, use `列出所有 docker 容器` rather than `列出所有docker容器`.
- For example, use `宽度为 50 个字` rather than `宽度为50个字`.

2. Place one space between numbers and units **except** degrees and percentages.

- For example, use `容量 50 MB` rather than `容量 50MB`.
- For instances of degree and percentage, use `50°C` and `50%` rather than `50 °C` and `50 %`.

3. No additional spaces before/after full-width punctuations.

- For example, use `开启 shell，进入交互模式` rather than `开启 shell ，进入交互模式`

4. Use full-width punctuations except for long Latin clauses.

- For example, use `嗨，你好。` rather than `嗨, 你好.`

5. Use a half-width punctuation to end a sentence when the last character is half-width.

- For example, use `将代码转化为 Python 3.` rather than `将代码转化为 Python 3。`

6. Use precise form for technical terms, and do not use unofficial Chinese abbreviations.

- For example, use `Facebook` rather than `facebook`, `fb` or `脸书`.

In order to maintain readability and normalization, please comply with the 6 rules above as much as possible when translating pages into Chinese.

For more information and examples of Chinese-specific rules, check out [*Chinese Copywriting Guidelines*](https://github.com/sparanoid/chinese-copywriting-guidelines/blob/master/README.en.md).

### Indonesian-Specific Rules

When translating pages to Indonesian, please keep in mind that we expect `tldr` pages to be easy to read for **both types of Indonesian audiences**, which are:

1. People who prefer to use standard Indonesian technical terms as possible, such as `unduh` for `download`, `awakutu` for `debugging`, and `muat ulang` for `reboot`.

- One of the most comprehensive lists of technical terms can be found under the [BlankOn Linux project](https://dev.blankonlinux.or.id/TimPengembang/Dokumentasi/Panduan/PanduanWiki/KamusBlankOn/).

2. People who prefer to use English words as-is to describe technical terms: `download` for `download`, `debugging` for `debugging`, and `reboot` for `reboot`.

The segmentation of these audiences is clearly noted on [Firefox Public Data Report](https://data.firefox.com/dashboard/usage-behavior):

> For most countries in the top 10, the majority (>90%) of users have their language set to the local language, **with a notable exception in Indonesia, which has about 80% English (US) and 20% Indonesian.**

First, command and example descriptions on pages in Indonesian must be written **without using active verb forms (i.e. those with `ber-` and `me-` prefixes)**. This means that sentences such as:

> **Mengunduh** sebuah file ke dalam suatu direktori
> (i.e. Downloading a file into a directory)

is considered incorrect. The correct form of the sentence should be:

> **Unduh** sebuah file ke dalam suatu direktori

Second, we recommend using the following forms of technical terms to make translated pages easier to read for both types of Indonesian audiences. Some of them may be used as-is, but others must be rewritten using Indonesian standard terms.

| English | Indonesian | Consideration(s) |
|---|---|---|
| App / Application | Aplikasi | The abbreviated word `apl.` is not common to some readers. |
| Boot, Reboot | Muat, Muat ulang | These words are the same for `load` and `reload`. See notes on the bottom section. |
| Client | Klien | |
| Command-line | Command-line | Using the word as-is is preferred over `baris perintah` or `alat berbasis mekanisme baris perintah` (`command-line tool`). |
| Commit (Git) | Commit | |
| Compile, Compiler | Kompilasikan, Pengompilasi | [`kompilasi`](https://kbbi.kemdikbud.go.id/entri/kompilasi) is officially considered as noun. Requires a `-kan` suffix to convert into a verb.  |
| Debugger | Debugger | Preferred over `pengawakutu` (`peng`-[`awakutu`](https://kbbi.kemdikbud.go.id/entri/awakutu)) which is unfamiliar to some readers. |
| Device | Perangkat | Preferred over [`peranti`](https://kbbi.kemdikbud.go.id/entri/peranti). |
| Disc | Disc | Preferred over [`cakram`](https://kbbi.kemdikbud.go.id/entri/cakram) which is unfamiliar by some readers. Use specific words if possible (e.g. CD or DVD).  |
| Execute / Run (a program...) | Jalankan | Preferred over [`eksekusikan`](https://kbbi.kemdikbud.go.id/entri/eksekusikan) which is longer to read and write. |
| File | Berkas | [`berkas`](https://kbbi.kemdikbud.go.id/entri/berkas) is an official term. Additionally, `jalan/menuju/file(_atau_direktori)` is deprecated in favor of `jalan/menuju/berkas(_atau_direktori)`. |
| Generate | Buat | Preferred over [`hasilkan`](https://kbbi.kemdikbud.go.id/entri/hasilkan). Example context: `Buat laporan baru`. |
| Hardware | Perangkat Keras | Preferred over [`peranti`](https://kbbi.kemdikbud.go.id/entri/peranti). |
| Image (as picture or visual image) | Gambar | Do not confuse with `image` as a means of storage. |
| Image (as means of storage, such as CD, ISO, and Docker) | Image | Another recommended word, [`citra`](https://kbbi.kemdikbud.go.id/entri/citra), is not officially recognized for computing. |
| Initialize, Reinitialize | Inisialisasikan, Inisialisasikan Ulang | The word [`inisialisasi`](https://kbbi.kemdikbud.go.id/entri/inisialisasi) is officially considered as noun. Requires a `-kan` suffix to convert into a verb. |
| Interpreter | Interpreter | Preferred over [`penerjemah`](https://kbbi.kemdikbud.go.id/entri/penerjemah) which is also commonly used to describe `translator`. |
| Install, Reinstall | Pasang, Pasang Ulang | Preferred over `instal` [which is not considered a standard word](https://kbbi.kemdikbud.go.id/entri/instal). |
| Load, Reload | Muat, Muat ulang | These words are the same for `boot` and `reboot`. See notes in the bottom section. |
| Options / Preferences (macOS) / Settings | Pengaturan | Preferred over [`opsi`](https://kbbi.kemdikbud.go.id/entri/opsi). |
| Server | Server | Preferred over [`peladen`](https://kbbi.kemdikbud.go.id/entri/peladen) or [`pelayan`](https://kbbi.kemdikbud.go.id/entri/pelayan), which are less common when used in computing contexts. |
| Service | Layanan | The Indonesian standard word is acceptable here. |
| Shell (command-line interface) | Syel | The Indonesian standard word is acceptable here. |
| Software | Perangkat Lunak | Preferred over [`peranti`](https://kbbi.kemdikbud.go.id/entri/peranti). |
| Start, Restart | Mulai, Mulai Ulang / Nyalakan, Nyalakan Ulang | See notes on the bottom section. |
| Update | Perbarui | Do not confuse with `upgrade`. |
| Upgrade | Tingkatkan | Do not confuse with `update`. |

When translating sentences that contain the word `boot` and `load` together, please add the context of the item that is being booted and/or loaded, so the use of the `muat` word may not be ambiguous. For example, when translating:

> Load configuration from a specific file after reboot

Instead of translating the sentence into:

> Muat konfigurasi dari file yang ditentukan setelah muat ulang

Add detailed contexts to remove ambiguity (notice the highlighted word):

> Muat konfigurasi dari file yang ditentukan setelah **pengguna** memuat ulang **sistem operasi**

Similarly, for the word `start` / `mulai`

> Mulai proses server web
> (Start the web server process)

To ensure that the sentence may not be confused with `start processing the web server`, you can use other words such as `nyalakan`:

> Nyalakan proses server web

### French-Specific Rules

- Command and example descriptions on pages in French must use the third person singular present indicative tense (présent de l'indicatif à la troisième personne du singulier). For example, use `Extrait une archive` rather than `Extraire une archive` or `Extrais une archive`.
- There must be a single blank space between special characters in the descriptions. For example, use `Plus d'informations : https://example.com.` instead of `Plus d'informations: https://example.com.` and use `Crée une archive à partir de fichiers :` instead of `Crée une archive à partir de fichiers:`.

### Portuguese-Specific Rules

Example descriptions on pages in Portuguese (for both European and Brazilian Portuguese) must start with verbs in the third person singular present indicative tense. This is because the descriptions must explain what the commands do, making this the correct form to express the intended meaning.

For example, use `Lista os arquivos` instead of `Listar os arquivos`, `Listando os arquivos` or any other form.

### Spanish-Specific Rules

- The descriptions of commands and examples must be conjugated in the third person singular indicative tense. Here are a couple of examples:

```md
> Crea archivos.
```

```md
- Crea un archivo en un directorio:
```

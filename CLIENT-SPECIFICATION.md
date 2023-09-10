# tldr-pages client specification

**Current Specification Version:** 2.0

This document contains the official specification for tldr-pages clients. It is _not_ a specification of the format of the pages themselves - only a specification of how a user should be able to interface with an official client. For a list of previous versions of the specification, see the [changelog section](#Changelog) below.

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


## Terminology

This section defines key terms that are relevant for understanding this specification document.

### Page

tldr-pages consists of multiple _pages_ - each of which describes a specific command.

### Platform

Pages are grouped by platform, i.e. operating systems — for example, `windows`, `linux`, `osx`.
The special platform `common` contains pages for commands that work identically across more than one platform.

If a page is common across multiple platforms, but slightly different on a given platform, then the page is still stored in the `common` directory, but a copy tailored for the differing platform is placed in that platform's specific folder.

For example, if the command `foo` is common to `mac`, `windows`, and `linux` but functions differently on `windows`, then the main page will be stored in `common`, and a copy will be placed in `windows` that's altered to match the different functionality.


## Command-line interface

This section describes the standardised command-line interface (CLI) for clients implementing one. Clients that do not provide a CLI can ignore this section.

### Arguments

The following command-line options MUST be supported (unless otherwise specified) if a CLI is implemented:

Option             | Required?   | Meaning
-------------------|-------------|----------
`-v`, `--version`  | Yes         | Shows the current version of the client, and the version of this specification that it implements.
`-p`, `--platform` | Yes         | Specifies the platform to be used to perform the action (either listing or searching) as an argument. If this option is specified, the selected platform MUST be checked first instead of the current platform as described below.
`-u`, `--update`   | Conditional | Updates the offline cache of pages. MUST be implemented if caching is supported.
`-l`, `--list`     | No          | Lists all the pages in the current platform to the standard output.
`-L`, `--language` | No          | Specifies the preferred language for the page returned. Overrides other language detection mechanisms. See the [language section](#language) for more information.

Clients MUST implement both the short and long versions of an option.

Additional decoration MAY be printed if the standard output is a [TTY](http://www.linusakesson.net/programming/tty/index.php). If not, then the output MUST not contain any additional decorations. For example, a page list MUST be formatted with one page name per line (to enable easy manipulation using standard CLI tools such as `grep` etc.).

Clients MAY support additional custom arguments and syntax not documented here.

Here are some examples of invocations using the above flags:

```bash
tldr --update
tldr --version
tldr -l
```

### Page names

The first argument that does not start with a dash (`-`), MUST be considered the page name.

Page names MAY contain spaces (e.g. `git status`), and such page names MUST be transparently concatenated with dashes (`-`). For example, the page name `git checkout` becomes `git-checkout`.

Page names MAY contain mixed capitalization, and such page names MUST be transparently lowercased. For example, the page name `eyeD3` becomes `eyed3`.

Here are some example invocations:

```bash
tldr 7za
tldr eyeD3  # equivalent to tldr eyed3
tldr git checkout  # equivalent to tldr git-checkout
tldr --platform osx bash
```

## Directory structure

This section documents the directory structure that contains the pages themselves.

The main version of every page is stored inside (but not directly) the `pages` directory. Inside this directory, there is a folder for each platform - for example `windows`, `linux`, and the special `common` platform:

 - `pages/`
   - `common/`
   - `linux/`
   - `windows/`
   - `osx/`
   - ...etc.

It is RECOMMENDED that clients support `macos` as an alias for `osx`.

While clients do not need to support new platforms automatically (though such support is RECOMMENDED), they MUST NOT break if additional platforms are added to tldr-pages.

The pages themselves reside inside the appropriate platform folder, with the extension `.md`. Here are some example mappings:

Command name    | Mapped name     | Filename
----------------|-----------------|-------------------
`7za`           | `7za`           | `7za.md`
`git checkout`  | `git-checkout`  | `git-checkout.md`
`tar`           | `tar`           | `tar.md`


### Translations

Other directories sit alongside the main `pages` directory, and contain translations of the main versions of every page - though pages MAY NOT have a translation available for a given language yet. Furthermore, a given language MAY NOT have a folder yet either. The format of these directories is `pages.<locale>`, where `<locale>` is a [POSIX Locale Name](https://www.gnu.org/software/gettext/manual/html_node/Locale-Names.html#Locale-Names) in the form of `<language>_<country>`, where:

 - `<language>` is the shortest [ISO 639](https://en.wikipedia.org/wiki/ISO_639) language code for the chosen language (see [here](https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes) for a complete list).
 - `<country>` is the two-letter [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) country code for the chosen region (see [here](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) for a complete list).

Some examples:

 - Chinese (Taiwan): `pages.zh_TW`.
 - Portuguese (Brazil): `pages.pt_BR`.
 - Italian: `pages.it`.

The structure inside these translation folders is identical to that of the main `pages` folder.


## Page structure

Although this specification is about the interface that clients must provide, it is also worth noting that pages are written in standard [CommonMark](https://commonmark.org/), which the exception of the non-standard `{{` and `}}` syntax, which surrounds values in an example that users may edit. Clients MUST NOT break if the page format is changed within the _CommonMark_ specification.


## Page resolution

This section defines the algorithm by which a client can decide which page a user has requested.

After transparently replacing spaces (` `) with dashes (`-`) and lowercasing the name, clients have several decisions to make:

 - The language of a page to display to a client
 - The platform to display a page from

### Platform

Clients MUST default to displaying the page associated with the platform on which the client is running.
For example, a client running on _Windows 11_ will default to displaying pages from the `windows` platform.
Clients MAY provide a user-configurable option to override this behaviour, however.

If a page is not available for the host platform, clients MUST fall back to the special `common` platform.

If a page is not available for either the host platform or the `common` platform, then clients SHOULD search other platforms and display a page from there - along with a warning message.

For example, a user has a client on Windows and requests the `apt` page. The client consults the platforms in the following order:

1. `windows` - Not available
2. `common` - Not available
3. `osx` - Not available
4. `linux` - Page found

Steps #3 and #4 may be done in either order.

It is possible that due to this page resolution logic, the client may show a page which does not belong to the host platform because a page can reside in `common`, and not be present on the host platform. Clients must not assume that a given command is always executable on the host platform.

#### If a page is not found

If a page cannot be found in _any_ platform, then it is RECOMMENDED that clients display an error message with a link to create a new issue against the `tldr-pages/tldr` GitHub repository. Said link might take the following form:

```url
https://github.com/tldr-pages/tldr/issues/new?title=page%20request:%20{command_name}
```

where `{command_name}` is the name of the command that was not found. Clients that have control over their exit code on the command line (i.e. clients that provide a CLI) MUST exit with a non-zero exit code in addition to showing the above message.

#### If multiple versions of a page were found

If multiple versions of a page were found for different platforms, then a client MAY choose to display a notice to the user notifying them of this.


## Language

Pages can be written in multiple languages. If a client has access to environment variables, it MUST use them to derive the preferred user language as described in the next paragraphs. If not, then clients MUST make reasonable assumptions based on the information provided by the environment in which they operate (e.g. consulting `navigator.languages` in a browser, etc.).

The [`LANG` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html) specifies the user's preferred locale (in the form `ll[_CC][.encoding]`). The [`LANGUAGE` environment variable](https://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html) specifies a priority list of locales (in the form `l1:l2:...`) that can be used if the locale defined by `LANG` is not available. Both `LANG` and `LANGUAGE` may contain the values `C` or `POSIX`, which should be ignored.

To determine the display language, a client MUST:

1. Check the value of `LANG`. If not set, then skip to step 5.
2. Extract the priority list from `LANGUAGE`. If not set, start with an empty priority list.
3. Append the value of `LANG` to the priority list.
4. Follow the priority list in order and use the first available language.
5. Fall back to English if none of the languages are available.

Examples:

 LANG  | LANGUAGE  | Result
-------|-----------|-----------------------------
 `cz`  |`it:cz:de` | `it`, `cz`, `de`, `en`
 `cz`  |`it:de:fr` | `it`, `de`, `fr`, `cz`, `en`
 `it`  |unset      | `it`, `en`
 unset |`it:cz`    | `en`
 unset |unset      | `en`

Regardless of the language determined through the environment, clients MUST always attempt to fall back to English if the page does not exist in the user's preferred language. Clients MAY notify the user when a page in their preferred language cannot be found (optionally including a link to the [translations section of the contributing guide](https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md#translations)).

It is also RECOMMENDED to make the language configurable, to not only rely on the environment. Clients SHOULD offer options to configure or override the language using configuration files or even command-line options (like `-L, --language` as suggested in the [arguments section](#arguments) above). If such a command-line option is specified, a client must strictly adhere to its value, and MUST NOT show pages in a different language, failing with an appropriate error message instead.

The [`LC_MESSAGES` environment variable](https://www.gnu.org/software/gettext/manual/html_node/Locale-Environment-Variables.html) MAY be present. If the client itself is localized and this environment variable is present, it MUST use its value to determine the language in which interface text is shown (separately from the language used for pages). In the absence of `LC_MESSAGES`, then `LANG` and `LANGUAGE` MUST be used for this purpose instead.

**Note that** for page lookup it is highly RECOMMENDED to give precedence to the platform over the language. In other words, look for a platform under each language, before checking the next preferred language. This ensures a meaningful and correct page resolution.

Here's an example of how the lookup should be done on `linux` having set `LANG=it` and `LANGUAGE="it:fr:en"`:

    1. pages.it/linux/some-page.md  -> does not exist
    2. pages.fr/linux/some-page.md  -> does not exist
    3. pages/linux/some-page.md     -> does not exist
    4. pages.it/common/some-page.md -> does not exist
    5. pages.fr/common/some-page.md -> does not exist
    6. pages/common/some-page.md    -> FOUND!

## Caching

If appropriate, it is RECOMMENDED that clients implement a cache of pages. If implemented, clients MUST download the entire archive either as a whole from **[https://tldr.sh/assets/tldr.zip](https://tldr.sh/assets/tldr.zip)** (Which redirects to [https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets/tldr.zip](https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets/tldr.zip)) or download language-specific translation archives in the format `https://tldr.sh/assets/tldr-pages.{{language-code}}.zip` (Which redirects to [https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets/tldr-pages.{{language-code}}.zip](https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets)), along with the archive for English from **[https://tldr.sh/assets/tldr-pages.zip](https://tldr.sh/assets/tldr-pages.zip)** (It redirects to [https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets/tldr-pages.zip](https://raw.githubusercontent.com/tldr-pages/tldr-pages.github.io/main/assets/tldr-pages.zip)).

Caching SHOULD be done according to the user's language configuration (if any), to not waste unneeded space for unused languages. Additionally, clients MAY automatically update the cache regularly.


## Changelog

<!--
Maintainer note:

Keep the changelog links pointing to this document under the appropriate
`/blob/<version-tag>/...` and also reference the PR which introduced the new
version. After merging an update to the client spec, tag appropriately and
create a new release under https://github.com/tldr-pages/tldr/releases
including the changes. NOTE: tagging of the commit with a new version tag (in
the form `vX.Y`) should be done immediately AFTER merging the version bump, as
the commit hash changes when merging with squash or rebase.
-->
 - Unreleased

 - [v2.0, September 10th 2023](https://github.com/tldr-pages/tldr/blob/v2.0/CLIENT-SPECIFICATION.md) ([#10148](https://github.com/tldr-pages/tldr/pull/10148))
   - Add recommendation to support `macos` alias for `osx` ([#7514](https://github.com/tldr-pages/tldr/pull/7514))
   - Drop the special "all" platform from the `--list` flag ([#7561](https://github.com/tldr-pages/tldr/pull/7561))
   - Drop the `master` branch from the assets link. ([#9668](https://github.com/tldr-pages/tldr/pull/9668))
   - Require support for long options ([#9651](https://github.com/tldr-pages/tldr/pull/9651))
   - Add recommendation to support caching individual translation archives ([#10148](https://github.com/tldr-pages/tldr/pull/10148))

 - [v1.5, March 17th 2021](https://github.com/tldr-pages/tldr/blob/v1.5/CLIENT-SPECIFICATION.md) ([#5428](https://github.com/tldr-pages/tldr/pull/5428))
   - Add requirement for converting command names to lowercase before running the page resolution algorithm.
   - Use HTTPS for archive links.

 - [v1.4, August 13th 2020](https://github.com/tldr-pages/tldr/blob/v1.4/CLIENT-SPECIFICATION.md) ([#4246](https://github.com/tldr-pages/tldr/pull/4246))
   - Add requirement for CLI clients to use non-zero exit code on failing to find a page.

 - [v1.3, June 11th 2020](https://github.com/tldr-pages/tldr/blob/v1.3/CLIENT-SPECIFICATION.md) ([#4101](https://github.com/tldr-pages/tldr/pull/4101))
   - Clarified fallback to English in the language resolution algorithm.
   - Update the `LANG` and `LANGUAGE` environment variables to conform to the GNU spec.

 - [v1.2, July 3rd 2019](https://github.com/tldr-pages/tldr/blob/v1.2/CLIENT-SPECIFICATION.md) ([#3168](https://github.com/tldr-pages/tldr/pull/3168))
   - Addition of a new `-L, --language` recommended command-line option.
   - Rewording of the language section, also encouraging the use of configuration files for language.
   - Shift from BCP-47 to POSIX style locale tags, with consequent **deprecation of previous versions of the spec**.
   - Clearer clarification about the recommended caching functionality.
   - Correction of the usage of the term "arguments" in the homonym section.

 - [v1.1, April 1st 2019](https://github.com/tldr-pages/tldr/blob/v1.1/CLIENT-SPECIFICATION.md) (deprecated) ([#2859](https://github.com/tldr-pages/tldr/pull/2859))
   - Clarified platform section.

 - [v1.0, January 23rd 2019](https://github.com/tldr-pages/tldr/blob/v1.0/CLIENT-SPECIFICATION.md) (deprecated) ([#2706](https://github.com/tldr-pages/tldr/pull/2706))
   - Initial release.

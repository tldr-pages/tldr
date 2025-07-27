# 📚 tldr-pages

<div align="center">
  <a href="https://tldr.sh/">
    <img alt="tldr-pages banner" src="images/banner.png" width="600"/>
  </a>
  
  <p><strong>📖 Simplified and community-driven man pages</strong></p>
  <p><em>Because life's too short for complex documentation</em></p>

[![Build status][github-actions-image]][github-actions-url]
[![Matrix chat][matrix-image]][matrix-url]
[![Merged PRs][prs-merged-image]][prs-merged-url]
[![GitHub contributors][contributors-image]][contributors-url]
[![license][license-image]][license-url]
[![Mastodon][mastodon-image]][mastodon-url]

[📱 **Try it now in your browser**](https://tldr.inbrowser.app) | [🐍 **Install Python client**](#-quick-start) | [🤝 **Contribute**](#-contributing)

</div>

---

## 📋 Table of Contents

- [✨ What is tldr-pages?](#-what-is-tldr-pages)
- [🚀 Quick Start](#-quick-start)
- [💻 Installation Options](#-installation-options)
- [🎯 Usage Examples](#-usage-examples)
- [🤝 Contributing](#-contributing)
- [🌍 Translations](#-translations)
- [🔗 Similar Projects](#-similar-projects)
- [❓ FAQ](#-faq)

---

## ✨ What is tldr-pages?

**tldr-pages** is a collection of **community-maintained help pages** for command-line tools that aims to be a simpler, more approachable complement to traditional man pages.

### 🤔 The Problem

Traditional man pages can be overwhelming and hard to navigate. For example, the first option in `man tar` explains:

```console
$ man tar
...
-b blocksize
   Specify the block size, in 512-byte records, for tape drive I/O.
   As a rule, this argument is only needed when reading from or writing to tape drives,
   and usually not even then as the default block size of 20 records (10240 bytes) is very common.
...
```

### 💡 Our Solution

We provide **practical, example-focused help pages** that get straight to the point:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/tldr-pages/tldr/blob/main/images/tldr-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/tldr-pages/tldr/blob/main/images/tldr-light.png">
  <img alt="Screenshot showing tldr output for tar command with practical examples" src="https://github.com/tldr-pages/tldr/blob/main/images/tldr-dark.png">
</picture>

### 🎯 What We Cover

This repository contains examples for the most common command-line tools across:

- 🐧 **Linux** & **UNIX**
- 🍎 **macOS** 
- 🔵 **Windows**
- 🔧 **FreeBSD**, **NetBSD**, **OpenBSD**
- ☀️ **SunOS**
- 🤖 **Android**

---

## 🚀 Quick Start

> 💡 **Want to try without installing?** Check out our [web client](https://tldr.inbrowser.app) with offline PWA support!

### Option 1: Python Client (Recommended)

```bash
pip3 install tldr
```

### Option 2: Rust Client (Fast & Modern)

```bash
brew install tlrc
```

### Option 3: Node.js Client

```bash
npm install -g tldr
```

### ✅ Test Your Installation

```bash
tldr tar
# Shows practical examples for the tar command
```

---

## 💻 Installation Options

<details>
<summary><strong>🐍 Python Client (Official)</strong></summary>

The most popular and feature-complete client:

```bash
# Using pip
pip3 install tldr

# Using conda
conda install tldr

# Using pipx (recommended for isolated installation)
pipx install tldr
```

**Features:**
- ✅ Full platform support
- ✅ Offline mode
- ✅ Custom themes
- ✅ Regular updates

</details>

<details>
<summary><strong>🦀 Rust Client (tlrc)</strong></summary>

A fast, modern client written in Rust:

```bash
# Using Homebrew (macOS/Linux)
brew install tlrc

# Using Cargo
cargo install tlrc

# Using Arch Linux
pacman -S tlrc
```

**Features:**
- ⚡ Lightning fast
- 🔋 Low resource usage
- 🎨 Beautiful output formatting

</details>

<details>
<summary><strong>📦 Other Package Managers</strong></summary>

```bash
# Arch Linux
pacman -S tldr

# Debian/Ubuntu
apt install tldr

# Fedora
dnf install tldr

# macOS (Homebrew)
brew install tldr
```

</details>

<details>
<summary><strong>📱 Mobile & Desktop Apps</strong></summary>

Check our [comprehensive client list](https://github.com/tldr-pages/tldr/wiki/Clients) for:
- 📱 iOS and Android apps
- 🖥️ Desktop applications
- 🌐 Browser extensions
- 🔌 Editor plugins (VS Code, Vim, Emacs)

</details>

<details>
<summary><strong>📄 Offline PDF Version</strong></summary>

Don't want to install anything? Download our [PDF version](https://github.com/tldr-pages/tldr/releases/latest/download/tldr-book.pdf) instead!

📚 **PDFs available in multiple languages** - check the [latest release](https://github.com/tldr-pages/tldr/releases/latest) assets.

</details>

---

## 🎯 Usage Examples

### Basic Commands

```bash
# Get help for any command
tldr <command>

# Examples
tldr git
tldr docker
tldr curl
tldr find
```

### Advanced Features

```bash
# Search for commands
tldr --search "compress"

# List all available pages
tldr --list

# Update the local cache
tldr --update

# Get help for specific platforms
tldr -p linux du
tldr -p windows dir
```

### Real-World Examples

```bash
# Before: trying to remember tar syntax
man tar  # 😵‍💫 overwhelming

# After: quick, practical examples
tldr tar  # 😊 exactly what you need
```

---

## 🤝 Contributing

**All contributions are welcome!** 🎉 We strive to maintain a welcoming and collaborative community.

### 🌟 Ways to Contribute

- 📝 **Add new command pages** for tools that aren't covered yet
- ✏️ **Improve existing pages** with better examples or descriptions  
- 🔍 **Help with [help wanted issues](https://github.com/tldr-pages/tldr/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22)**
- 🌍 **Translate pages** into different languages
- 🐛 **Report bugs** or suggest improvements

### 🚀 Getting Started

1. **Read our [Contributing Guidelines](CONTRIBUTING.md)**
2. **Check our [Governance](GOVERNANCE.md) document**
3. **Browse [open issues](https://github.com/tldr-pages/tldr/issues)**
4. **Join our [Matrix chat](https://matrix.to/#/#tldr-pages:matrix.org)** for questions

### ✍️ Writing Pages

All tldr pages are written in **Markdown** and follow a simple format:

- Clear, practical examples
- Common use cases first
- Brief descriptions
- No lengthy explanations

You can contribute using:
- 💻 **Command line** with Git
- 🌐 **GitHub web interface** (perfect for beginners!)

---

## 🌍 Translations

We support multiple languages! 🗺️

### 📊 Translation Progress

Visit [tldri18n](https://lukwebsforge.github.io/tldri18n/) to see:
- Overall progress of all translations
- Which translations need help
- Missing or outdated pages

### 🤝 Join Translation Efforts

Ready to help translate? 
1. Check the progress tracker above
2. Read our [translation guidelines](CONTRIBUTING.md#translations)
3. Start translating pages in your language!

---

## 🔗 Similar Projects

Explore other great command-line help tools:

| Project | Description | Best For |
|---------|-------------|----------|
| [**CLI Pages**](https://github.com/command-line-interface-pages) | Standardized help for CLI, directories, and configs | Comprehensive documentation |
| [**Cheat**](https://github.com/cheat/cheat) | Interactive command-line cheatsheets | Personal customization |
| [**cheat.sh**](https://cheat.sh/) | Unified interface aggregating multiple sources | Quick online lookup |
| [**devhints**](https://devhints.io/) | Programming-focused cheatsheets | Development workflows |
| [**eg**](https://github.com/srsudar/eg) | Detailed examples with explanations | In-depth learning |
| [**navi**](https://github.com/denisidoro/navi) | Interactive cheatsheet browser | Interactive exploration |

---

## ❓ FAQ

<details>
<summary><strong>What does "tldr" mean?</strong></summary>

**TL;DR** stands for "**Too Long; Didn't Read**" - Internet slang for content that's been skipped as too lengthy. Perfect for our mission of simplifying documentation! 

📖 [Learn more about TL;DR](https://www.howtogeek.com/435266/what-does-tldr-mean-and-how-do-you-use-it/)

</details>

<details>
<summary><strong>How is this different from man pages?</strong></summary>

- **📚 Man pages**: Comprehensive, technical, reference documentation
- **⚡ tldr pages**: Practical examples, common use cases, quick reference

Think of tldr as your friendly cheat sheet, while man pages are the complete manual.

</details>

<details>
<summary><strong>Can I use tldr offline?</strong></summary>

**Yes!** Most clients cache pages locally for offline use. The pages are also available as downloadable PDFs.

</details>

<details>
<summary><strong>How often are pages updated?</strong></summary>

Pages are continuously updated by our community. The clients typically update their local cache automatically or when you run `tldr --update`.

</details>

---

<div align="center">

### 🎉 Thank you to all our contributors!

[![Contributors](https://contrib.rocks/image?repo=tldr-pages/tldr)](https://github.com/tldr-pages/tldr/graphs/contributors)

---

**💬 Questions? Ideas? Join our community!**

[![Matrix Chat](https://img.shields.io/badge/Chat-Matrix-brightgreen?style=for-the-badge&logo=matrix)](https://matrix.to/#/#tldr-pages:matrix.org)
[![Mastodon](https://img.shields.io/badge/Follow-Mastodon-6364FF?style=for-the-badge&logo=mastodon&logoColor=fff)](https://fosstodon.org/@tldr_pages)

**Made with ❤️ by the community, for the community**

</div>

---

<!-- Badge definitions -->
[github-actions-url]: https://github.com/tldr-pages/tldr/actions
[github-actions-image]: https://img.shields.io/github/actions/workflow/status/tldr-pages/tldr/ci.yml?branch=main&label=Build
[matrix-url]: https://matrix.to/#/#tldr-pages:matrix.org
[matrix-image]: https://img.shields.io/matrix/tldr-pages:matrix.org?label=Chat+on+Matrix
[prs-merged-url]: https://github.com/tldr-pages/tldr/pulls?q=is:pr+is:merged
[prs-merged-image]: https://img.shields.io/github/issues-pr-closed-raw/tldr-pages/tldr.svg?label=Merged+PRs&color=green
[contributors-url]: https://github.com/tldr-pages/tldr/graphs/contributors
[contributors-image]: https://img.shields.io/github/contributors-anon/tldr-pages/tldr.svg?label=Contributors
[license-url]: https://github.com/tldr-pages/tldr/blob/main/LICENSE.md
[license-image]: https://img.shields.io/badge/license-CC_BY_4.0-blue.svg?label=License
[mastodon-url]: https://fosstodon.org/@tldr_pages
[mastodon-image]: https://img.shields.io/badge/Mastodon-6364FF?logo=mastodon&logoColor=fff
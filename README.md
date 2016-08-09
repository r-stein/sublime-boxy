<p align="center"><img src="https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/name.gif" alt="BOXY"></p>

<p align="center">
  <a href="https://github.com/oivva/boxy/releases"><img src="https://img.shields.io/github/release/oivva/boxy.svg?maxAge=3600&style=flat-square" alt="Release"></a>
  <a href="https://packagecontrol.io/packages/Boxy%20Theme"><img src="https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square" alt="Downloads"></a>
  <a href="https://travis-ci.org/oivva/boxy"><img src="https://img.shields.io/travis/oivva/boxy.svg?maxAge=3600&style=flat-square" alt="Build Status"></a>
  <a href="https://gitter.im/oivva/boxy"><img src="https://img.shields.io/gitter/room/nwjs/nw.js.svg?maxAge=2592000&style=flat-square" alt="Gitter"></a>
  <a href="https://github.com/oivva/boxy/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000&style=flat-square" alt="License"></a>&nbsp;
  <a href="https://twitter.com/intent/tweet?hashtags=Boxy%2CTheme%2CColorScheme%2CSublimeText&amp;original_referer=http%3A%2F%2Foivva.com%2Fboxy%2F&amp;ref_src=twsrc%5Etfw&amp;text=The%20most%20hackable%20theme%20%E2%9D%A4%20Sublime%20Text%203&amp;tw_p=tweetbutton&amp;url=https%3A%2F%2Fpackagecontrol.io%2Fpackages%2FBoxy%2520Theme&amp;via=oivvatweets" title="Share via Twitter"><img src="https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/twitter.png" alt="Twitter"></a>&nbsp;
  <a href="https://www.patreon.com/oivva" title="Donate with Patreon"><img src="https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/patreon.png" alt="Click here to lend your support to: Boxy and make a donation at patreon.com"></a>&nbsp;
  <a href="https://flattr.com/profile/oivva" title="Donate with Flattr"><img src="https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/flattr.png" alt="Click here to lend your support to: Boxy and make a donation at flattr.com !"></a>&nbsp;
  <a href="https://www.coinbase.com/oivva" title="Donate with Bitcoin"><img src="https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/bitcoin.png" alt="Click here to lend your support to: Boxy and make a donation at coinbase.com !"></a>
</p>

***

A set of easy customizable interface and syntax themes for **Sublime Text 3 3103+**. Comes in, both, light and dark variations. There are dozens of [**options**][settings] that enable you to personalize your experience with `Boxy Theme`, don't forget to check [them][settings] out.

Want to contribute some code? Excellent! Read up on our [guidelines](https://github.com/oivva/boxy/blob/dev/.github/CONTRIBUTING.md).

If you have some problems, first search for a similar issue, and then report with [new one][issues]. Please read the [**Known Issues**][known-issues] section before reporting a new one.

Want to learn more? [**See the wiki &#8594;**][wiki].

***

<div>
<a href="https://github.com/oivva/boxy#getting-started">Getting Started</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/boxy#installation">Installation</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/boxy#activation">Activation</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/boxy#presets">Presets</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/boxy/wiki/Settings">Settings</a>&nbsp;
▪&nbsp;<a href="https://forum.sublimetext.com/t/boxy-the-most-hackable-theme-for-sublime-text-3/20564">Forum</a>&nbsp;
▪&nbsp;<a href="https://packagecontrol.io/packages/Boxy%20Theme">Package Control</a>
▪&nbsp;<a href="https://github.com/oivva/boxy#share-the-love">Share The Love</a>
</div>

***

### Getting Started

[![Getting Started with Boxy Theme][img-getting-started]][getting-started]

### Installation

#### Package Control

The easiest way to install is using [Package Control][pc], where [Boxy][theme] is listed as **`Boxy Theme`**.

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Package Control: Install Package`
3. Find `Boxy Theme` and hit `Enter`
4. Restart Sublime Text
    - **macOS**  : menu item `Sublime Text -> Quit Sublime Text`
    - **Windows**: menu item `File -> Exit`
    - **Linux**  : menu item `File -> Exit`
5. Repeat step 1, then choose `Package Control: Satisfy Dependencies`
6. Restart Sublime Text

#### Download

1. [Download the .zip][release]
2. Unzip and rename the folder to `Boxy Theme`
3. Copy the folder into `Packages` directory, which you can find using the menu item `Preferences → Browse Packages...`
4. Restart Sublime Text
5. Manually install all dependencies listed in the `dependencies.json`
6. Restart Sublime Text

### Activation

Activate the UI theme and color scheme by modifying your user preferences file, which you can find using the menu item `Preferences → Settings`. Also you can use commands provided by the theme:

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Boxy Theme: Activation` or `Boxy Theme: Preferences`
3. Hit `Enter`

> **DON'T FORGET TO RESTART SUBLIME TEXT AFTER ACTIVATING THE THEME.**

#### Boxy Yesterday

```js
"theme": "Boxy Yesterday.sublime-theme",
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Yesterday.tmTheme",
```

[![Boxy Yesterday][img-yesterday]][img-yesterday]

### Boxy Tomorrow

```js
"theme": "Boxy Tomorrow.sublime-theme",
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Tomorrow.tmTheme",
```

[![Boxy Tomorrow][img-tomorrow]][img-tomorrow]

### Boxy Ocean

```js
"theme": "Boxy Ocean.sublime-theme",
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Ocean.tmTheme",
```

[![Boxy Ocean][img-ocean]][img-ocean]

### Boxy Monokai

```js
"theme": "Boxy Monokai.sublime-theme",
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Monokai.tmTheme",
```

[![Boxy Monokai][img-monokai]][img-monokai]

### Presets

You can activate presets by using commands provided by the theme:

1. Open `Command Palette` using menu item `Tools → Command Palette...`
2. Choose `Boxy Theme: Activation` to change the UI theme and color scheme
3. Choose `Boxy Theme: Presets` to change the preset
4. Hit `Enter`

#### Atom Preset & Boxy Yesterday

[![Atom Preset & Boxy Yesterday][img-yesterday-atom]][img-yesterday-atom]

The screenshot above shows next options in action:

```js
// Boxy Yesterday Activation
"theme": "Boxy Yesterday.sublime-theme",
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Yesterday.tmTheme",
```

```js
// Atom Preset Settings
"theme_accent_sky": true,
"theme_button_rounded": true,
"theme_find_panel_close_hidden": true,
"theme_grid_border_size_lg": true,
"theme_icon_button_highlighted": true,
"theme_icons_atomized": true,
"theme_popup_border_visible": true,
"theme_scrollbar_rounded": true,
"theme_sidebar_disclosure": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_tab_rounded": true,
"theme_tab_selected_prelined": true,
"theme_tab_separator": true,
```

The operating system is **macOS**. The font used for the code is [**Fira Code**][fira-code]. The UI font is [**San Francisco Text**][san-francisco] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Boxy Theme Addon - Widget Font Size][addon-widget-font-size]
* [Bracket Highlighter][bracket-highlighter]

#### Predawn Preset & Boxy Tomorrow

[![Predawn Preset & Boxy Tomorrow][img-tomorrow-predawn]][img-tomorrow-predawn]

The screenshot above shows next options in action:

```js
// Boxy Tomorrow Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Tomorrow.tmTheme",
"theme": "Boxy Tomorrow.sublime-theme",
```

```js
// Predawn Preset Settings
"theme_accent_tangerine": true,
"theme_bar": true,
"theme_dirty_materialized": true,
"theme_scrollbar_colored": true,
"theme_scrollbar_line": true,
"theme_sidebar_folder_mono": true,
"theme_tab_arrows_hidden": true,
"theme_tab_line_size_lg": true,
"theme_tab_selected_transparent": true,
"theme_tab_selected_underlined": true,
"theme_tab_size_lg": true,
```

The operating system is **Windows**. The font used for the code is [**Operator Mono**][operator-mono]. The UI font is [**Segoe UI Semibold**][segoe-ui] (via [addon][addon-font-face])

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Boxy Theme Addon - Mono File Icons - Dark UI][addon-mono-file-icons-dark-ui]
* [Bracket Highlighter][bracket-highlighter]

#### Material Preset & Boxy Ocean

[![Material Preset & Boxy Ocean][img-ocean-material]][img-ocean-material]

The screenshot above shows next options in action:

```js
// Boxy Ocean Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Ocean.tmTheme",
"theme": "Boxy Ocean.sublime-theme",
```

```js
// Material Preset Settings
"theme_accent_lime": true,
"theme_bar": true,
"theme_bar_colored": true,
"theme_bar_logo_atomized": true,
"theme_button_rounded": true,
"theme_icons_materialized": true,
"theme_scrollbar_rounded": true,
"theme_sidebar_highlight_selected_text_only": true,
"theme_sidebar_highlight_text_only": true,
"theme_sidebar_indent_top_level_disabled": true,
"theme_tab_highlight_text_only": true,
"theme_tab_line_size_lg": true,
"theme_tab_selected_transparent": true,
"theme_tab_selected_underlined": true,
```

The operating system is **Ubuntu**. The font used for the code is [**Roboto Mono**][roboto-mono]. The UI font is [**Ubuntu Medium**][ubuntu] (via [addon][addon-font-face]).

Installed packages:

* [Boxy Theme Addon - Font Face][addon-font-face]
* [Color Highlighter][color-highlighter]
* [Color ​Helper][color-helper]

#### Code Preset & Boxy Monokai

[![Code Preset & Boxy Monokai][img-monokai-code]][img-monokai-code]

The screenshot above shows next options in action:

```js
// Boxy Monokai Activation
"color_scheme": "Packages/Boxy Theme/schemes/Boxy Monokai.tmTheme",
"theme": "Boxy Monokai.sublime-theme",
```

```js
// Code Preset Settings
"theme_accent_purple": true,
"theme_bar": true,
"theme_sidebar_disclosure": true,
"theme_sidebar_indent_sm": true,
"theme_statusbar_colored": true,
"theme_tab_highlight_text_only": true,
```

The operating system is **Windows**. The font used for the code is [**Space Mono**][space-mono].

Installed packages:

* [Bracket Highlighter][bracket-highlighter]
* [Sublime Linter][sublime-linter]

***

### Share The Love

I've put a lot of time and effort into making `Boxy Theme` awesome. If you love it, you can buy me a coffee. Every cup helps! I promise it will be a good investment 😉

**Donate with:**

[![Patreon][img-patreon-with-title]][patreon] &nbsp; [![Flattr][img-flattr-with-title]][flattr] &nbsp; [![Bitcoin][img-bitcoin-with-title]][bitcoin]

<!-- Links -->

[release]: https://github.com/oivva/boxy/releases
[downloads]: https://packagecontrol.io/packages/Boxy%20Theme
[build-status]: https://travis-ci.org/oivva/boxy
[gitter]: https://gitter.im/oivva/boxy
[license]: https://github.com/oivva/boxy
[patreon]: https://www.patreon.com/oivva "Donate with Patreon"
[flattr]: https://flattr.com/profile/oivva "Donate with Flattr"
[bitcoin]: https://www.coinbase.com/oivva "Donate with Bitcoin"
[upgrading]: https://github.com/oivva/boxy/wiki/Upgrading
[issues]: https://github.com/oivva/boxy/issues
[wiki]: https://github.com/oivva/boxy/wiki
[website]: http://www.oivva.com/boxy/
[known-issues]: https://github.com/oivva/boxy/wiki#known-issues
[pr]: https://github.com/wbond/package_control_channel/pull/5500
[manual-install]: https://github.com/oivva/boxy/wiki/Get-It#manual
[settings]: https://github.com/oivva/boxy/wiki/Settings
[pc]: https://packagecontrol.io/
[theme]: https://packagecontrol.io/packages/Boxy%20Theme
[getting-started]: https://youtu.be/GSWdjWX_LnE "Watch 'Getting Started with Boxy Theme' on YouTube"


<!-- Images -->

[img-name]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/name.png
[img-release]: https://img.shields.io/github/release/oivva/boxy.svg?maxAge=3600&style=flat-square
[img-downloads]: https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square
[img-build-status]: https://img.shields.io/travis/oivva/boxy.svg?maxAge=3600&style=flat-square
[img-gitter]: https://img.shields.io/gitter/room/nwjs/nw.js.svg?maxAge=2592000&style=flat-square
[img-license]: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000&style=flat-square
[img-patreon]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/patreon.png
[img-patreon-with-title]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/patreon-with-title.png
[img-flattr]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/flattr.png
[img-flattr-with-title]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/flattr-with-title.png
[img-bitcoin]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/bitcoin.png
[img-bitcoin-with-title]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/bitcoin-with-title.png
[img-yesterday]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/default/yesterday.png
[img-tomorrow]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/default/tomorrow.png
[img-ocean]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/default/ocean.png
[img-monokai]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/default/monokai.png
[img-yesterday-atom]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/presets/yesterday.png
[img-tomorrow-predawn]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/presets/tomorrow.png
[img-ocean-material]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/presets/ocean.png
[img-monokai-code]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/presets/monokai.png
[img-getting-started]: https://raw.githubusercontent.com/oivva/boxy-extras/master/assets/readme/3.2.0/getting-started.png

<!-- Fonts -->

[fira-code]: https://github.com/tonsky/FiraCode/blob/master/README.md
[san-francisco]: https://developer.apple.com/fonts/
[ubuntu]: http://font.ubuntu.com/
[roboto-mono]: https://fonts.google.com/specimen/Roboto+Mono?query=Roboto
[space-mono]: https://fonts.google.com/specimen/Space+Mono?query=Space+Mono
[operator-mono]: http://www.typography.com/fonts/operator/styles/operatorscreensmartpro
[segoe-ui]: https://www.microsoft.com/typography/Fonts/family.aspx?FID=331

<!-- Packages -->

[addon-font-face]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Font%20Face
[addon-widget-font-size]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Widget%20Font%20LG
[addon-mono-file-icons-dark-ui]: https://github.com/search?q=user%3Aoivva+boxy-addon-mono
[git-gutter]: https://packagecontrol.io/packages/GitGutter
[sublime-linter]: https://packagecontrol.io/packages/SublimeLinter
[bracket-highlighter]: https://packagecontrol.io/packages/BracketHighlighter
[color-highlighter]: https://packagecontrol.io/packages/Color%20Highlighter
[color-helper]: https://packagecontrol.io/packages/ColorHelper

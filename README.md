<p align="center"><img src="https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/name.gif" alt="BOXY"></p>

<p align="center">
  <a href="https://github.com/oivva/st-boxy/releases"><img src="https://img.shields.io/github/release/oivva/st-boxy.svg?maxAge=3600&style=flat-square" alt="Release"></a>
  <a href="https://packagecontrol.io/packages/Boxy%20Theme"><img src="https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square" alt="Downloads"></a>
  <a href="https://travis-ci.org/oivva/st-boxy"><img src="https://img.shields.io/travis/oivva/st-boxy.svg?maxAge=3600&style=flat-square" alt="Build Status"></a>
  <a href="https://twitter.com/intent/tweet?hashtags=Boxy%2CTheme%2CColorScheme%2CSublimeText&amp;original_referer=http%3A%2F%2Foivva.com%2Fboxy%2F&amp;ref_src=twsrc%5Etfw&amp;text=The%20most%20hackable%20theme%20%E2%9D%A4%20Sublime%20Text%203&amp;tw_p=tweetbutton&amp;url=https%3A%2F%2Fpackagecontrol.io%2Fpackages%2FBoxy%2520Theme&amp;via=oivvatweets" title="Share via Twitter" target="_blank"><img src="https://img.shields.io/badge/share-twitter-1DA1F2.svg?maxAge=2592000&style=flat-square" alt="Twitter"></a>
  <a href="https://www.patreon.com/oivva" title="Donate with Patreon"><img src="https://img.shields.io/badge/donate-patreon-orange.svg?maxAge=2592000&style=flat-square" alt="Make a donation at patreon.com"></a>
</p>

***

A set of easy customizable interface and syntax themes for **Sublime Text 3 3103+**. Comes in, both, light and dark variations. There are dozens of [**options**][settings] that enable you to personalize your experience with `Boxy Theme`, don't forget to check [them][settings] out.

Want to contribute some code? Excellent! Read up on our [guidelines](https://github.com/oivva/st-boxy/blob/dev/.github/CONTRIBUTING.md).

If you have some problems, first search for a similar issue, and then report with [new one][issues]. Please read the [**Known Issues**][known-issues] section before reporting a new one.

Want to learn more? [**See the wiki &#8594;**][wiki].

***

<div>
<a href="https://github.com/oivva/st-boxy#getting-started">Getting Started</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/st-boxy#installation">Installation</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/st-boxy#activation">Activation</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/st-boxy#presets">Presets</a>&nbsp;
▪&nbsp;<a href="https://github.com/oivva/st-boxy/wiki/Settings">Settings</a>&nbsp;
▪&nbsp;<a href="https://forum.sublimetext.com/t/boxy-the-most-hackable-theme-for-sublime-text-3/20564">Forum</a>&nbsp;
▪&nbsp;<a href="https://packagecontrol.io/packages/Boxy%20Theme">Package Control</a>
▪&nbsp;<a href="https://github.com/oivva/st-boxy#share-the-love">Share The Love</a>
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
    - **macOS**  : menu item `Sublime Text → Quit Sublime Text`
    - **Windows**: menu item `File → Exit`
    - **Linux**  : menu item `File → Exit`
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

**Donate with:** [Patreon][patreon].

<!-- Links -->

[build-status]: https://travis-ci.org/oivva/st-boxy
[downloads]: https://packagecontrol.io/packages/Boxy%20Theme
[getting-started]: https://youtu.be/d2FZCUDcNxo 'Watch "Getting Started with Boxy Theme" on YouTube'
[issues]: https://github.com/oivva/st-boxy/issues
[known-issues]: https://github.com/oivva/st-boxy/wiki#known-issues
[manual-install]: https://github.com/oivva/st-boxy/wiki/Get-It#manual
[patreon]: https://www.patreon.com/oivva "Donate with Patreon"
[pc]: https://packagecontrol.io/
[release]: https://github.com/oivva/st-boxy/releases
[settings]: https://github.com/oivva/st-boxy/wiki/Settings
[theme]: https://packagecontrol.io/packages/Boxy%20Theme
[upgrading]: https://github.com/oivva/st-boxy/wiki/Upgrading
[website]: http://www.oivva.com/st-boxy/
[wiki]: https://github.com/oivva/st-boxy/wiki


<!-- Images -->

[img-build-status]: https://img.shields.io/travis/oivva/st-boxy.svg?maxAge=3600&style=flat-square
[img-downloads]: https://img.shields.io/packagecontrol/dt/Boxy%20Theme.svg?maxAge=3600&style=flat-square
[img-getting-started]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.4.0/getting-started.png
[img-monokai]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/default/monokai.png
[img-monokai-code]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/presets/monokai.png
[img-name]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/name.png
[img-ocean]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/default/ocean.png
[img-ocean-material]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/presets/ocean.png
[img-patreon]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/patreon.png
[img-release]: https://img.shields.io/github/release/oivva/st-boxy.svg?maxAge=3600&style=flat-square
[img-tomorrow]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/default/tomorrow.png
[img-tomorrow-predawn]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/presets/tomorrow.png
[img-yesterday]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/default/yesterday.png
[img-yesterday-atom]: https://raw.githubusercontent.com/oivva/st-boxy-assets/master/assets/readme/3.2.0/presets/yesterday.png

<!-- Fonts -->

[fira-code]: https://github.com/tonsky/FiraCode/blob/master/README.md
[operator-mono]: http://www.typography.com/fonts/operator/styles/operatorscreensmartpro
[roboto-mono]: https://fonts.google.com/specimen/Roboto+Mono?query=Roboto
[san-francisco]: https://developer.apple.com/fonts/
[segoe-ui]: https://www.microsoft.com/typography/Fonts/family.aspx?FID=331
[space-mono]: https://fonts.google.com/specimen/Space+Mono?query=Space+Mono
[ubuntu]: http://font.ubuntu.com/

<!-- Packages -->

[addon-font-face]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Font%20Face
[addon-mono-file-icons-dark-ui]: https://github.com/search?q=user%3Aoivva+boxy-addon-mono
[addon-widget-font-size]: https://packagecontrol.io/packages/Boxy%20Theme%20Addon%20-%20Widget%20Font%20LG
[bracket-highlighter]: https://packagecontrol.io/packages/BracketHighlighter
[color-helper]: https://packagecontrol.io/packages/ColorHelper
[color-highlighter]: https://packagecontrol.io/packages/Color%20Highlighter
[git-gutter]: https://packagecontrol.io/packages/GitGutter
[sublime-linter]: https://packagecontrol.io/packages/SublimeLinter

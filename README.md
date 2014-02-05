# Validatorian.sugar

Local CSS validation for Espresso 2, using the W3C CSS validator.

## Installation

**Requires Espresso 2.2** and the **ShellActions.sugar**

1. Follow the instructions to install the [ShellActions.sugar](https://github.com/onecrayon/ShellActions-sugar) (if you have not already previously done so)
2. [Download Validatorian.sugar](http://onecrayon.com/downloads/Validatorian.sugar.zip)
3. Decompress the zip file (your browser might do this for you)
4. Double click the Sugar to install it

Optionally, you can clone it from GitHub for easier updating:

    cd ~/Library/Application\ Support/Espresso/Sugars
    git clone git://github.com/onecrayon/Validatorian.sugar.git

Relaunch Espresso, and a new Validation submenu will be available in your Actions menu. You can then update the Sugar when necessary by running the following command:

    cd ~/Library/Application\ Support/Espresso/Sugars/Validatorian.sugar
    git pull

## Available actions

Validatorian.sugar currently includes the following actions:

* **Validate CSS**: Parses the current CSS file (or CSS files linked from the current HTML file) using a local copy of the [W3C CSS Validator](http://jigsaw.w3.org/css-validator/) (no internet connection necessary).

## Development

Validatorian.sugar is written entirely in XML and Python using ShellAction.sugar's built-in HTML outputting! For linking to errors, it uses a special `x-espresso://` URL scheme that is new in Espresso 2.2.

To discover how I'm doing things or tweak its behavior to fit your own needs, right click the Sugar in the Finder and choose Show Package Contents or fork this project and go to town.

You can also [email me](http://onecrayon.com/about/contact/) if you have any feedback, requests, or run across any problems. Alternately, come chat with me and other [Sugar devs on Glassboard](https://app.glassboard.com/web/invitation/code/yvyic).

## Changelog

**1.0**:

* Initial release, with CSS validation using the W3C CSS Validator

## Licensing

W3C CSS Validator released under the [W3C Software license](http://www.w3.org/Consortium/Legal/copyright-software); source code is available at <http://dev.w3.org/cvsweb/2002/css-validator/>. Its various dependencies may be released under other open source licenses, and you can find their source code and licensing information on their respective websites.

All other code copyright (c) 2014 Ian Beck, and published under the MIT license

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

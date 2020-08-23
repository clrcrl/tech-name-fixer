# tech-name-fixer

A script to generate MacOS text replacements to correct common misspellings of tech company and product names.

For example: `Github` will be corrected to `GitHub` wherever MacOS Text Replacements are respected.

MacOS Text Replacements are respected in:
- Apple apps (iMessage, Notes, Pages etc.)
- Slack

MacOS Text Replacements are _not_ respected in:
- Notion
- Google Docs

## Usage instructions
A basic understanding of python and the command line is assumed in these instructions.

To install these snippets on your own computer:
1. Clone this repo, and `cd` into it.
2. Run `python generate-text-replacements.py` — this generates a file named `tech-names.plist`
3. Open up `System Preferences` > `Keyboard` > `Text`
4. Drag the `tech-names.plist` file from its location to the Text pane.

## Contributing
Contributions (especially to the list of company and product names) are welcome!

Please keep the entries in `tech-names.csv` in alphabetical order.

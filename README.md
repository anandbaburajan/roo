# roo

Simple CLI to-do app

## Installation

```
$ git clone https://github.com/AnandBaburajan/roo.git
$ cd roo
$ pip install .
```

## Usage

`roo` provides 3 commands:
- `c`: Check a list
- `a`: Add a task to a list
- `d`: Delete a task from a list

## Example

```
$ roo a today "Clean the house"

$ roo a today "Take Roo for a walk"

$ roo c today
[1]: Clean the house
[2]: Take Roo for a walk

$ roo d today 2

$ roo c today
[1]: Clean the house
```

# roo

Simple CLI to-do list app

## Installation

```
$ git clone https://github.com/AnandBaburajan/roo.git
$ cd roo
$ pip install .
```

## Usage

`roo` provides 3 commands:
- `v`: View a list
- `a`: Add a task to a list
- `e`: Edit a task in a list
- `d`: Delete a task from a list

## Example

```
$ roo a today "Clean the house"

$ roo a today "Take Roo for a walk"

$ roo v today
[1]: Clean the house
[2]: Take Roo for a walk

$ roo d today 1

$ roo v today
[1]: Take Roo for a walk

$ roo e today 1 "Take Roo for a run"

$ roo v today
[1]: Take Roo for a run
```

## License

`roo` is distributed under the [MIT License](https://github.com/AnandBaburajan/roo/blob/main/LICENSE).

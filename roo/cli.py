import os
import argparse
from pathlib import Path


ROO_DATA_PATH = Path.home() / "roo_data/"


def main():
    args = parse_args()
    args.func(args)


def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command")
    commands.required = True

    check_parser = commands.add_parser("v", help="View a list")
    check_parser.set_defaults(func=check)
    check_parser.add_argument("listname")

    add_parser = commands.add_parser("a", help="Add a task to a list")
    add_parser.set_defaults(func=add)
    add_parser.add_argument("listname")
    add_parser.add_argument("task", type=str)
    
    edit_parser = commands.add_parser("e", help="Edit a task in a list")
    edit_parser.set_defaults(func=edit)
    edit_parser.add_argument("listname")
    edit_parser.add_argument("number", type=int)
    edit_parser.add_argument("newtask", type=str)

    delete_parser = commands.add_parser("d", help="Delete a task from a list")
    delete_parser.set_defaults(func=delete)
    delete_parser.add_argument("listname")
    delete_parser.add_argument("number", type=int)

    return parser.parse_args()


def check(args):
    list_path = str(ROO_DATA_PATH / args.listname) + ".txt"

    try:
        with open(os.path.expanduser(list_path), "r") as f:
            lines = f.readlines()

        if not lines:
            print("List is empty")

        for i, line in enumerate(lines):
            print("[{0}]: {1}".format(i + 1, line.strip()))
    except FileNotFoundError:
        print("List doesn't exist")


def add(args):
    list_path = str(ROO_DATA_PATH / args.listname) + ".txt"

    with open(os.path.expanduser(list_path), "a") as f:
        f.write(args.task + "\n")


def edit(args):
    list_path = str(ROO_DATA_PATH / args.listname) + ".txt"

    try:
        with open(os.path.expanduser(list_path), "r") as f:
            lines = f.readlines()

        if len(lines) < args.number:
            print("Task doesn't exist")
            return

        with open(os.path.expanduser(list_path), "w") as f:
            for i, line in enumerate(lines):
                if i == args.number - 1:
                    f.write(args.newtask + "\n")
                else:
                    f.write(line)

    except FileNotFoundError:
        print("List doesn't exist")


def delete(args):
    list_path = str(ROO_DATA_PATH / args.listname) + ".txt"

    try:
        with open(os.path.expanduser(list_path), "r") as f:
            lines = f.readlines()

        if len(lines) < args.number:
            print("Task doesn't exist")
            return

        with open(os.path.expanduser(list_path), "w") as f:
            for i, line in enumerate(lines):
                if i != args.number - 1:
                    f.write(line)
    except FileNotFoundError:
        print("List doesn't exist")

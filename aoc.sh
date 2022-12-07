#!/bin/bash

function show_usage() {
    printf "Usage: $0 {action} {day}\n"
    printf "\n"
    printf "Actions:\n"
    printf "  new   - Create files for new day\n"
    printf "  test  - Run unit tests for day\n"
    printf "  run   - Generate output\n"
    printf "  help  - Show this help screen\n"
    printf "\n"
    printf "Day is in format 00\n"
    return 0
}

if [ -z $2 ]; then
    show_usage
else
    case $1 in
	"tmux")
	    echo "TODO: open tumx with split panes nvim | aoc test day..."
	    ;;
	"new")
	    cp src/_day_nn.py "src/day_$2.py"
	    sed "s/{day}/$2/g" tests/_test_nn.py > "tests/test_$2.py" 
	    touch "data/input_$2.txt"
	    ;;
	"test")
	    python -m unittest "tests.test_$2"
	    ;;
	"run")
	    python "src/day_$2.py"
	    ;;
	"help")
	    show_usage
	    ;;
    esac
fi

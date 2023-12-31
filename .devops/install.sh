#!/bin/bash

# use python 3.12, check if it exists
# check if python3.12 is installed
if ! [ -x "$(command -v python3.12)" ]
then
    echo "Python 3.12 could not be found, please install it."
    exit
fi


## check if Python venv exists
if [ ! -d ".venv" ]; then
    echo "Creating Python venv..."
    python3.12 -m venv .venv
fi

# check if venv is created
if [ ! -d ".venv" ]; then
    echo "Python venv could not be found, please create it."
    echo $PWD
    exit
fi

## activate Python venv
echo "Activating Python venv..."
. .venv/bin/activate

# check if venv is activated
if [ ! -n "$VIRTUAL_ENV" ]; then
    echo "Python venv could not be activated, please activate it."
    exit
fi

## install Python dependencies
echo "Installing Python dependencies..."
pip install poetry -q
poetry install

## activate pre-commit hooks
echo "Activating pre-commit hooks..."
pre-commit install

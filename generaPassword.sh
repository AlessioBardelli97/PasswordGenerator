#!/bin/bash

echo -n "$0: "

param=8

if [[ -n $1 ]]; then
    param=$1
fi

python3 generaPassword.py "$param"

#!/bin/bash

set -euo pipefail

if [ $# -lt 1 ]; then
    echo "Usage: $0 <day>" >&2
    exit 1
fi

day=$1

reporoot=$(git rev-parse --show-toplevel)
outdir="${reporoot}/days/${day}"
cookie=$(cat "$reporoot/.aocsessionid")

mkdir -p "$outdir"
curl -o "$outdir/input" --cookie "$cookie" "https://adventofcode.com/2021/day/${day}/input"

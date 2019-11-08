#!/usr/bin/env bash

# This script checks whether the files added/edited in the PR exist in other platform folders also or not.
set -ex

git --no-pager diff --name-only HEAD~

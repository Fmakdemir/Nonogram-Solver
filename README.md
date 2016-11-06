# Nonogram-Solver
![Python 3.4|3.5](https://img.shields.io/badge/python-3.4%7C3.5-blue.svg)
[![Build Status](https://travis-ci.org/Fmakdemir/nonogram-solver.svg?branch=master)](https://travis-ci.org/Fmakdemir/nonogram-solver)

A nonogram puzzle solver and a nonogram to json generator written in python. It can be used as both a library or cli program.

## Setup:
`pip install -r requirements.txt`

## Usage:
Run solver:
```
python3 nonogramsolver.py -f [json-path]
```
Run generator:
```
python3 nonogramgenerator.py -f [nonogram-path]
```
alternatively
```
python3 nonogramgenerator.py -s 'XXX
X.X
XXX'
```

json file is a multi dimensional array as in examples

nonogram file is in the form of . and x/X's where x shows painted blocks such as:
```
x.X
XXX
XxX
```

!!This is under develepment. Not functional yet!!

# pygments.formatters.satysfi

A [SATySFi](https://github.com/gfngfn/SATySFi) formatter for [pygments](http://pygments.org/)

# Installation

``` console
$ sudo python setup.py install
```

# Usage

Install `pygmentize` and this module before using.


To format:

``` console
$ pygmentize -Ofull=true -f satysfi -o out.saty
```

To output the style definition:

``` console
$ pygmentize -f satysfi -S <style> > pygments.satyh
```

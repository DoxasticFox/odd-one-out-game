# README #

### About ###
This is a quick and somewhat dirty script which uses Wordnet to select the "odd one out" from a list (of arbitrary size). For example, in the list "arm, leg, computer", the only object which isn't a limb is the odd one out.

### Dependencies ###
* Python 2
* NLTK (I don't remember which version)

### Usage ###
Load the file in the Python interpreter using

    execfile("odd one out.py")

then call `odd` function from the console like so

    >>> odd('arm', 'leg', 'computer')
    'computer'
    >>> odd('liver', 'spleen', 'battery', 'tongue')
    'battery'
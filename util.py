# Natural Language Toolkit: Utility functions
#
# Copyright (C) 2001-2010 NLTK Project
# Author: Steven Bird <sb@csse.unimelb.edu.au>
# URL: <http://www.nltk.org/>
# For license information, see LICENSE.TXT

from itertools import chain

def ingrams(sequence, n, pad_left=False, pad_right=False, pad_symbol=None):
    """
    A utility that produces an iterator over ngrams generated from a sequence of items.
    
    For example:
    
    >>> list(ingrams([1,2,3,4,5], 3))
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    
    Use ngrams for a list version of this function.  Set pad_left
    or pad_right to true in order to get additional ngrams:
    
    >>> list(ingrams([1,2,3,4,5], 2, pad_right=True))
    [(1, 2), (2, 3), (3, 4), (4, 5), (5, None)]

    @param sequence: the source data to be converted into ngrams
    @type sequence: C{sequence} or C{iterator}
    @param n: the degree of the ngrams
    @type n: C{int}
    @param pad_left: whether the ngrams should be left-padded
    @type pad_left: C{boolean}
    @param pad_right: whether the ngrams should be right-padded
    @type pad_right: C{boolean}
    @param pad_symbol: the symbol to use for padding (default is None)
    @type pad_symbol: C{any}
    @return: The ngrams
    @rtype: C{iterator} of C{tuple}s
    """

    sequence = iter(sequence)
    if pad_left:
        sequence = chain((pad_symbol,) * (n-1), sequence)
    if pad_right:
        sequence = chain(sequence, (pad_symbol,) * (n-1))

    history = []
    while n > 1:
        history.append(sequence.next())
        n -= 1
    for item in sequence:
        history.append(item)
        yield tuple(history)
        del history[0]
        
def ibigrams(sequence, **kwargs):
    """
    A utility that produces an iterator over bigrams generated from a sequence of items.
    
    For example:
    
    >>> list(ibigrams([1,2,3,4,5]))
    [(1, 2), (2, 3), (3, 4), (4, 5)]
    
    Use bigrams for a list version of this function.

    @param sequence: the source data to be converted into bigrams
    @type sequence: C{sequence} or C{iterator}
    @return: The bigrams
    @rtype: C{iterator} of C{tuple}s
    """

    for item in ingrams(sequence, 2, **kwargs):
        yield item
        
def itrigrams(sequence, **kwargs):
    """
    A utility that produces an iterator over trigrams generated from a sequence of items.
    
    For example:
    
    >>> list(itrigrams([1,2,3,4,5])
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
    
    Use trigrams for a list version of this function.

    @param sequence: the source data to be converted into trigrams
    @type sequence: C{sequence} or C{iterator}
    @return: The trigrams
    @rtype: C{iterator} of C{tuple}s
    """

    for item in ingrams(sequence, 3, **kwargs):
        yield item

"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

def isPowerOfTwo(n):
    if n == 0:
        return False
    if n == 1:
        return True
    elif n % 2 == 0:
        return self.isPowerOfTwo(n / 2)
    else:
        return False

n = 17
print(isPowerOfTwo(n))

"""
l'idea è molto semplice si tratta di una funzione ricorsiva che divide n per due fino ad arrivare ad 1.
se riesci ad arrivare ad 1 allora si tratta di una potenza di 2 altrimenti no. Ad antecedere tutto c'è il caso in cui
n = 0 in questo caso se utilizassi il reminder n%2 otterei 0 ma ciò non significa che sia potenza di due, il reminder
uguale a zero è una condizione vera per tutte le potenze di 2 e per 0 che però non è potenza di 2
"""

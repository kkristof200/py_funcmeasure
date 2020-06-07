from funcmeasure import measure

def f1():
    5**2

def f2():
    5**2**10

measure([f1, f2], times=1000)
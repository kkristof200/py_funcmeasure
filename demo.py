from funcmeasure import measure

def f1():
    5**2

def f2():
    5**10**5

measure([f1, f2], times=1000)
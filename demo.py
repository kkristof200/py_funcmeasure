from funcmeasure import measure, partial, Measurement

def f1():
    5**2

def f2():
    5**2**10

measurements = measure([f1, f2], times=1000, print_benchmark=True)
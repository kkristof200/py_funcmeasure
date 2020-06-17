from funcmeasure import measure, partial, Measurement

def f1():
    5**2

def f2():
    5**2**10

def f3():
    5**2**2**2

measurements = measure([f1, (f2, 'second'), f3], times=1000)

measurements = measure(
    {
        f1: None,
        f2: 'second',
        f3: None
    },
    times=1000
)
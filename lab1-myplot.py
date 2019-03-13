from numpy import *
from matplotlib.pyplot import *

def myplot(z):
    # plot(x, y)
    # show()
    x = linspace(-10., 10., int(z))
    #x2 = linspace(-10., 10., int(z))
    #y = sin(x) * exp(-(x / 5.0) ** 2)
    y1 = sin(int(z) * x) + cos(x * x)
    #y2 = cos(x2) * exp(-(x2 / 2.0) ** 2)

    #figure(1, figsize=(6,4))
    #plot(x, y, 'b-', label='theory')
    #plot(x2, y2, 'r', label="data")

    #xlabel('x')
    #legend(loc='upper right')
    #axhline(color='gray', zorder=-1)
    #axvline(color='gray', zorder=-1)
    #ogranicza widocznosc wykresu
    #ylim(-1.3, 1.3)
    #savefig('WavyPulse.pdf')
    #show()
    plot(x, y1)

    show()



myplot(3)



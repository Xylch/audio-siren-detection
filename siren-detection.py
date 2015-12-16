import essentia
import essentia.standard
from essentia.standard import *
import numpy
import math
from sys import argv


siren_avg_high = -7.6
siren_max_low = 8.05

loader = essentia.standard.MonoLoader(filename=argv[1])
func = FFT()
curr = func(loader())
avg = math.log(abs(numpy.mean(curr)))
maxim = math.log(abs(max(curr)))

if avg <= siren_avg_high and maxim >= siren_max_low:
    print "This is a siren!"
else:
    print "This is not a siren."


# --------------------- CODE USED FOR TESTING ---------------------

#import matplotlib.pyplot as plt

#loader1 = essentia.standard.MonoLoader(filename='siren-short.mp3')
#loader2 = essentia.standard.MonoLoader(filename='siren-long.mp3')
#loader3 = essentia.standard.MonoLoader(filename='audio-siren.mp3')
#loader4 = essentia.standard.MonoLoader(filename='siren2-short.mp3')
#loader5 = essentia.standard.MonoLoader(filename='siren2-long.mp3')
#loader6 = essentia.standard.MonoLoader(filename='antidote.mp3')
#loader7 = essentia.standard.MonoLoader(filename='beep13.mp3')
#loader8 = essentia.standard.MonoLoader(filename='vacuum.mp3')

#loaders = [loader1(), loader2(), loader3(), loader4(),
    #loader5(), loader6(), loader7(), loader8()]

#func = FFT()
#curr = func(loader8())
#plt.plot(curr)
#plt.show()
#print math.log(abs(numpy.mean(curr)))
#print math.log(abs(max(curr)))

#for loader in loaders:
    #curr = func(loader)
    #avg = math.log(abs(numpy.mean(curr)))
    #maxim = math.log(abs(max(curr)))

    #if avg <= siren_avg_high and maxim >= siren_max_low:
        #print "this is a siren!"
    #else:
        #print "NOPE!"

#file.write(func(loader2()))

#file.write(func(loader7()))
#file.write("\n")
#file.write(func(loader8()))

#file.close()

#def arrayToFile(fName, ldr):
    #func = FFT()
    #arr = func(ldr)

    #fle = open(fName, 'w')

    #for item in arr:
        #print >> fle, item

    #fle.close()

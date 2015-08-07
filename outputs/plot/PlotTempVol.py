#!usr/bin/python

from sys import argv
import matplotlib.pyplot as plt
import glob
import numpy 
from scipy.optimize import curve_fit
import pylab



def extract_Temp_Dens( Filename ):
	File = open(Filename)
	Temp = []
	Density = []
	Volume = []
	Enthalpy = []
    #Energy = []
	for line in File:
		line = line.split()
		try:
			if (float(line[0]>0.0)):
				Temp.append(float(line[0]))
				Density.append(float(line[2]))
				Volume.append(float(line[1]))
                #Energy.append(float(line[3]))
				Enthalpy.append(float(line[4]))
		except:
			continue
	Temp = numpy.asarray(Temp)
	Density = numpy.asarray(Density)
	Volume = numpy.asarray(Volume)
    #Energy = numpy.asarray(Energy)
	Enthalpy = numpy.asarray(Enthalpy)
	
	return Temp, Density, Volume, Enthalpy

def Convert_Data(Density):
    Temp = [550., 500., 450., 400., 350., 300., 250., 200.]
    DENS = []
    k = 0
    P = 2500
    for i in range(8):
        DENS.append(numpy.mean(Density[k:(P+k)]))
        k+= 5000
    Temp = numpy.asarray(Temp)
    DENS = numpy.asarray(DENS)
                    
    return Temp, DENS

def Convert_Data_2(Density):
    Temp = [150., 100.]
    DENS = []
    k = 2500
    P = 2500
    for i in range(2):
        DENS.append(numpy.mean(Density[k:(P+k)]))
        k+= 5000
    Temp = numpy.asarray(Temp)
    DENS = numpy.asarray(DENS)

    return Temp, DENS


def Convert_Data_3(Density):
    Temp = [550., 500., 450., 400., 350., 300., 250., 200., 150.0, 100.0]
    DENS = []
    k = 0
    P = 2500
    for i in range(10):
        DENS.append(numpy.mean(Density[k:(P+k)]))
        k+= 5000
    Temp = numpy.asarray(Temp)
    DENS = numpy.asarray(DENS)
    return Temp, DENS


def linear(x, a, b):
    return a*x + b



Temp2, Density2, Volume2, Enthalpy2 = extract_Temp_Dens('Temp_Dens_Glass_P3HT_2.txt')
Temp, Density, Volume, Enthalpy = extract_Temp_Dens('Temp_Dens_Glass_P3HT.txt')
Temp3, Density3, Volume3, Enthalpy3 = extract_Temp_Dens('Temp_Dens_Glass_P3NT.txt')
Temp4, Density4, Volume4, Enthalpy4 = extract_Temp_Dens('Temp_Dens_Glass_P3DT.txt')
Temp5, Density5, Volume5, Enthalpy5 = extract_Temp_Dens('Temp_Dens_Glass_P3DT_2.txt')
#TempG, DensityG, VolumeG = extract_Temp_Dens('Temp_Density_Glass.txt')


Temp = Temp - 273.15
T, D = Convert_Data(Density)
T2,D2 = Convert_Data_2(Density2)
TN, DN = Convert_Data_3(Density3)
TD, DD = Convert_Data(Density4)
TD2, DD2 = Convert_Data_2(Density5)




T3, D3 = Convert_Data_3(Density3)

D = numpy.concatenate((D,D2))
T = numpy.concatenate((T,T2))
DD = numpy.concatenate((DD,DD2))
TD = numpy.concatenate((TD,TD2))

DD[8] = 1.0795
DD[9] = 1.0912

Density = numpy.concatenate((Density, Density2))


Tg = T[6:10]
Dg = D[6:10]
Tm = T[0:5]
Dm = D[0:5]

TgN = TN[6:10]
DgN = DN[6:10]
TmN = TN[0:5]
DmN = DN[0:5]

TgD = TD[6:10]
DgD = DD[6:10]
TmD = TD[0:5]
DmD = DD[0:5]



m,b = pylab.polyfit(Tg,Dg,1)
m1, b1 = pylab.polyfit(Tm,Dm,1)

mN, bN = pylab.polyfit(TgN, DgN, 1)
mN1, bN1 = pylab.polyfit(TmN, DmN, 1)

mD, bD = pylab.polyfit(TgD,DgD,1)
mD1, bD1 = pylab.polyfit(TmD, DmD,1)

Density4 = numpy.concatenate((Density4,Density5))


print "P3HT", m, b, m1, b1
print "P3NT", mN, bN, mN1, bN1
print "P3DT", mD, bD, mD1, bD1

print T, D
#plt.xlim([100,550])
"""
plt.subplot(121)
plt.xlim([0,47500])
plt.ylim([.94,1.15])
plt.xlabel('Time Step', fontsize = 30)
plt.ylabel('Density (g/cm^3)', fontsize = 30 )
#plt.title('Glass Transition', fontsize = 40 )
plt.plot( Density,'k', label = 'P3HT')
plt.plot( Density4, 'b', label = 'P3DT')
"""
plt.figure()
plt.ylabel('Density (g/cm^3)', fontsize = 30 )
plt.ylim([.94,1.15])
plt.xlabel('Temperature (Kelvin)', fontsize = 30)
#plt.ylabel('Density (g/cm^3)', fontsize = 30)
#plt.plot(T, D, 'o', label='...')
plt.plot(T, D,'o', label = 'P3HT')
plt.plot(TD, DD,'o', label = 'P3DT')
plt.plot(TN,DN, 'o', label = 'P3NT')
x = numpy.linspace(100,550,100)
plt.plot(x, m*x + b)
plt.plot(x, m1*x + b1)
plt.plot(x, mN*x + bN)
plt.plot(x, mN1*x + bN1)
plt.plot(x, mD*x + bD)
plt.plot(x, mD1*x + bD1)
#plt.plot( T,D,'o')
#plt.plot( Density3, label = 'P3NT')
#plt.plot( T3,D3,'o')
#plt.plot(TempG, DensityG, 'o', label = 'Melting Curve')


plt.legend(loc="upper left")
plt.show()




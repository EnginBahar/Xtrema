# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 18:48:00 2015

@author: TheLichWing
"""
from numpy import *

class Methods:
    @staticmethod
    def Special_Func(Data, ToVS, Type, Bness, f):        
        """'Geçerli bir hata hesabına ihtiyaç var'"""
        sort = argsort(Data[0])
            
        Data[0] = Data[0][sort]
        Data[1] = Data[1][sort]
        
        time_ini = int(Data[0][0])

        Data[0] = Data[0] - time_ini
        
        'a*x^2+b*x+c'
        """
        fun = f.strip()
        m = sorted(set(f.lower()) & set(f.upper()), key = f.lower().index)
        for item in m:
            f = ','.join(f.split(item))
            
        par = ','.join(list(''.join( unique(f.split(','))).replace('x','').replace('X',''))).strip()
        """
        
        fun = f.strip().replace('^', '**')
        par = []
        
        for i in fun:
            if i.isupper() == True:
                par.append(str(i))
        par = ','.join(unique(par))

        print(fun, par)
        exec(compile(f"def curve(x, {par}):\n    return {fun}", '', 'exec'), globals())

        from scipy.optimize import curve_fit

        p, params_covariance = curve_fit(curve, Data[0], Data[1])

        print(p)

        xrange_ = linspace(min(Data[0]), max(Data[0]), 1000)
        
        m = []        
        for i in range(len(p)):
            m.append(str(p[i]))
        
        # p = ','.join(m)

        # exec(compile('y_value = curve(xrange_,'+p+')','' ,'exec'))
        # exec(compile('e_value = curve(Data[0],'+p+')','' ,'exec'))

        y_value = curve(xrange_, *p)
        e_value = curve(Data[0], *p)

        g = std(e_value)
        Mintime_Err = Maxtime_Err = sum(((Data[1] - e_value)/g)**2)/len(Data[0])
        
        if Type == 0 or Type == 1:
            if ToVS == 0:
                minm = argmax(y_value) if Bness == 'Magnitude' else argmin(y_value)
                Mintime = xrange_[minm] + time_ini
                return (Mintime, Mintime_Err, xrange_ + time_ini, y_value)                
            else:
                maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
                Maxtime = xrange_[maxm] + time_ini
                return (Maxtime, Maxtime_Err, xrange_ + time_ini, y_value)                
            
        elif Type == 2:
            maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
            Maxtime = xrange_[maxm] + time_ini
            return (Maxtime, min(y_value) if Bness == 'Magnitude' else max(y_value),
                    xrange_ + time_ini, y_value)
    
        
    @staticmethod
    def Cubic_Spline(Data, ToVS, Type, Bness):
        """Geçerli bir hata hesabına ihtiyaç var. Ayrıca bu yöntem
        zaman hesabı için ne kadar iyi!. Metodlardan çıkarılabilir."""
        sort=argsort(Data[0])
        Data[0]=Data[0][sort]
        Data[1]=Data[1][sort]
        
        time_ini = int(Data[0][0])
        Data[0] = Data[0] - time_ini
        
        import scipy.interpolate as inter
        xrange_=linspace(min(Data[0]),max(Data[0]),5000)
        tck = inter.splrep(Data[0], Data[1])

        y_value = inter.splev(xrange_, tck)
        
        if Type == 0 or Type == 1:
            if ToVS == 0:
                minm = argmax(y_value) if Bness == 'Magnitude' else argmin(y_value)
                Mintime = xrange_[minm] + time_ini
                return (Mintime, 0, xrange_ + time_ini, y_value)                
            else:
                maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
                Maxtime = xrange_[maxm] + time_ini
                return (Maxtime, 0, xrange_ + time_ini, y_value)                
            
        elif Type == 2:
            maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
            Maxtime = xrange_[maxm]  + time_ini
            return (Maxtime, min(y_value) if Bness == 'Magnitude' else max(y_value),
                    xrange_ + time_ini, y_value)
          
    @staticmethod
    def Kwee(Data, ToVS, Bness):
        """Tekrar yazılmalı"""
        sort = argsort(Data[0])
        Time = Data[0][sort]
        Mag = Data[1][sort]
        
        if (ToVS == 0 and Bness == 'Magnitude') or (ToVS == 1 and Bness == 'Flux'):
            Mag = Mag * -1

        if (len(Time) % 2 == 0):
            Time = Time[:-1]
            Mag = Mag[:-1]
        
        Time_ini = int(Time[0])
        Time = Time - Time_ini

        nop = len(Time)                       
                      
        if nop < 21:
            nop = 21                      
                                    
        ti = (Time[-1] - Time[0])/(nop - 1)
        IPtime = zeros(nop, dtype=float)                                              
        for i in range(nop):
             IPtime[i] = Time[0] + i*ti                       
                                
        IPmag = interp(IPtime, Time, Mag)
        minm = argmin(IPmag)   

        #import matplotlib.pyplot as plt
        #plt.plot(IPtime, IPmag, 'bo')
        
        #print len(IPmag), len(Time), nop
        for i in range(nop):                               
            pm = min(minm, nop - minm - 1) - 2
            SoS_R = zeros(3,dtype=float)
            #print 'min', minm
            #print 'pm',pm
            for j in range(3):
                for k in range(1,pm,1):
                    SoS_R[j] = SoS_R[j] + (IPmag[(minm+(j-1)+k)] - \
                        IPmag[(minm+(j-1)-k)])**2
                    #print j , (minm+(j-1)+k) , (minm+(j-1)-k)                    

            #print SoS_R
            if SoS_R[1] <= SoS_R[2] and SoS_R[1] <= SoS_R[0]:
                SoS_F = SoS_R
                break
            elif SoS_R[1] > SoS_R[2]:
                minm +=1
               
            elif SoS_R[1] > SoS_R[0]:
                minm -=1
        try:
            #if  minm - 1 > 0 and minm + 1 < nop:
            y1 = SoS_F[1]
            y2 = SoS_F[0]
            y3 = SoS_F[2]

            x1 = IPtime[minm]
            x2 = IPtime[minm - 1]
            x3 = IPtime[minm + 1]

            Cona= float((((y1-y3)/(x1-x3)) - ((y3-y2)/(x3-x2))) / (x1-x2))
            Conb= float(((y1-y3)/(x1-x3)) - (Cona*(x1+x3)))                                       
            Conc= float(y1 - Cona*(x1**2) - Conb*x1)
            
            ExtTime= (-1*(Conb))/(2*Cona) + Time_ini  
            z = nop/4.0
            ExtTime_err=sqrt((4*Cona*Conc-Conb**2)/(4*(Cona**2)*(z-1)))
            
            if ExtTime_err < 0:
                ExtTime_err = 0

        except:            
            ExtTime = 'nan'
            ExtTime_err = 'nan'                              
        
        return (ExtTime, ExtTime_err)
    
    """
    @staticmethod
    def Kwee(Data, ToVS, Bness):
        '''Tekrar yazılmalı'''
        sort = argsort(Data[0])
        Time = Data[0][sort]
        Mag = Data[1][sort]
                
        if (ToVS == 0 and Bness == 'Magnitude') or (ToVS == 1 and Bness == 'Flux'):
            Mag = Mag * -1

        if (len(Time) % 2 == 0):
            Time=Time[:-1]
            Mag=Mag[:-1]
        
        Time_ini = int(Time[0])
        Time = Time - Time_ini

        nop=len(Time)                       
                      
        if (nop < 21):
            nop = 21                      
                                    
        ti=(Time[-1]-Time[0])/float((nop-1))
        IPtime=zeros(nop,dtype=float)                                              
        for i in range(nop):
             IPtime[i]=Time[0]+i*ti                       
                                
        IPmag=interp(IPtime,Time,Mag)
        
        ASoR = [[],[],[]]
        for i in range(1,nop-1,1):
            Sum = 0
            k = 1
            #print i
            while i - k >= 0 and i + k < nop:
                Sum += (IPmag[i - k] - IPmag[i + k])**2
                    += (IPmag[i - k] - IPmag[i])**2
                    += (IPmag[i] - IPmag[i + k])**2
                
                #print i - k, i + k
                
                k += 1
            #print "***************"
            ASoR[0].append(i)
            ASoR[1].append(float(Sum)/(k-1))
            ASoR[2].append(float(Sum))
        
        print ASoR[1]
        print ASoR[2]
            
        Ind_min_ASoR = argmin(ASoR[1])
        
        y1 = ASoR[2][Ind_min_ASoR]
        y2 = ASoR[2][Ind_min_ASoR - 1]
        y3 = ASoR[2][Ind_min_ASoR + 1]
        
        x1 = IPtime[ASoR[0][Ind_min_ASoR]]
        x2 = IPtime[ASoR[0][Ind_min_ASoR] - 1]
        x3 = IPtime[ASoR[0][Ind_min_ASoR] + 1]
        
        Cona= (((y1-y3)/(x1-x3)) - ((y3-y2)/(x3-x2))) / (x1-x2)                                               
        Conb= ((y1-y3)/(x1-x3)) - (Cona*(x1+x3))                                            
        Conc= y1 - Cona*(x1**2) - Conb*x1                     
        
        '''
        def func(x, a, b, c):
          return a*x**2 + b*x + c
        
        p, v = curve_fit(func,[x1, x2, x3], [y1, y2, y3])
                                              
        Cona = p[0]                                      
        Conb = p[1]                                    
        Conc = p[2]
        '''                            
        ExtTime= -Conb/(2*Cona) + Time_ini
        
#        print Cona, Conb, Conc
#        print (4*Cona*Conc-Conb**2)
#        print (4*(Cona**2)*((nop/4.0)-1))
        
        ExtTime_err=sqrt((4*Cona*Conc-Conb**2)/(4*(Cona**2)*((nop/4.0)-1)))                     
        
#        import matplotlib.pyplot as plt        
#        plt.plot(IPtime, IPmag, 'bo')
        #print ExtTime, ExtTime_err
        return (ExtTime, ExtTime_err)
    
    """            
    @staticmethod
    def Bisection(Data, ToVS, Bness):
        """ 3 farklı kiriş yönteminden hangisi daha etkili.
        Bakılmalı ve ona göre yeniden yazılmalı"""
        
        sort = argsort(Data[0])
        Time = Data[0][sort]
        Mag = Data[1][sort]        
        
        if (ToVS == 0 and Bness == 'Magnitude') or (ToVS == 1 and Bness == 'Flux'):
            Mag = Mag * -1
            
        Time_ini = int(Data[0][0])
        Time = Time - Time_ini
        
        nop = len(Time)
        
        if nop < 7:
            
            IPtime = linspace(min(Time),max(Time),21)
            IPMag = interp(IPtime,Time,Mag)
            
            Time = IPtime
            Mag = IPMag
        
        minm = argmin(Mag)
        
        dataR_x = Time[minm+1:]
        dataR_y = Mag[minm+1:]

        dataL_x = Time[:minm]
        dataL_y = Mag[:minm]
        
        int_y_L = Mag[minm:]
        int_x_L = Time[minm:]

        int_y_L = int_y_L[argsort(Mag[minm:])]
        int_x_L = int_x_L[argsort(Mag[minm:])]
        
        int_y_R = Mag[:minm+1]
        int_x_R = Time[:minm+1]

        int_y_R = int_y_R[argsort(Mag[:minm+1])]
        int_x_R = int_x_R[argsort(Mag[:minm+1])]
        
        if Mag[0] > Mag[-1]:
            i = argwhere(Mag > Mag[-1])
            
            dataLtoR_x = interp(dataL_y[len(i):],int_y_L,int_x_L)
            dataRtoL_x = interp(dataR_y,int_y_R,int_x_R)
            
            Lp_x = (dataL_x[len(i):] + dataLtoR_x)/2.0
            Lp_y = dataL_y[len(i):]
            Rp_x = (dataR_x + dataRtoL_x)/2.0
            Rp_y = dataR_y
        else:
            i = argwhere(Mag > Mag[0])
            
            dataLtoR_x = interp(dataL_y,int_y_L,int_x_L)
            dataRtoL_x = interp(dataR_y[:-len(i)],int_y_R,int_x_R)
            
            Lp_x = (dataL_x + dataLtoR_x)/2.0
            Lp_y = dataL_y
            Rp_x = (dataR_x[:-len(i)]+ dataRtoL_x)/2.0
            Rp_y = dataR_y[:-len(i)]
            
        x = hstack((Lp_x,Rp_x))
        y = hstack((Lp_y,Rp_y))
        
        s = argsort(y)        
        x = x[s]        
        y = y[s]
        
        x = x[4:]
        y = y[4:]
        
        #try:
        Mintime = average(x) 
        Mintime_Err = sqrt((sum(x**2) - sum(x) * Mintime) / 
                                                    (len(x) - 1))
        
#        except:
#            Mintime = 'nan'
#            Mintime_Err = 'nan'
        #print Mintime + Time_ini, Mintime_Err
        
#        import matplotlib.pyplot as plt
#        plt.plot(x,y,'ro',Time,Mag,'bo')
        
        return (Mintime + Time_ini, Mintime_Err)
        
    @staticmethod
    def fourier(Data, ToVS, Type, Bness):        
        """Geçerli bir hata hesabına ihtiyaç var"""
        
        sort = argsort(Data[0])
            
        Data[0] = Data[0][sort]
        Data[1] = Data[1][sort]
        
        time_ini = int(Data[0][0])

        Data[0] = Data[0] - time_ini

        def curve(x, a0, a1, b1, a2, b2):
          return a0 + a1*cos(pi*x) + b1*sin(pi*x) + a2*cos(2*pi*x) + \
          b2*sin(2*pi*x)
        
        from scipy.optimize import curve_fit
        p, params_covariance = curve_fit(curve,Data[0], Data[1])

        xrange_ = linspace(min(Data[0]), max(Data[0]), 1000)  
        y_value = curve(xrange_, p[0], p[1], p[2], p[3], p[4])
        e_value = curve(Data[0], p[0], p[1], p[2], p[3], p[4])
        
        g = std(e_value)
        Mintime_Err = Maxtime_Err = sum(((Data[1] - e_value)/g)**2)/len(Data[0])
        
        if Type == 0 or Type == 1:
            if ToVS == 0:
                minm = argmax(y_value) if Bness == 'Magnitude' else argmin(y_value)
                Mintime = xrange_[minm] + time_ini
                return (Mintime, Mintime_Err, xrange_ + time_ini, y_value)                
            else:
                maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
                Maxtime = xrange_[maxm] + time_ini
                return (Maxtime, Maxtime_Err, xrange_ + time_ini, y_value)                
            
        elif Type == 2:
            maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
            Maxtime = xrange_[maxm] + time_ini
            return (Maxtime, min(y_value) if Bness == 'Magnitude' else max(y_value),
                    xrange_ + time_ini, y_value)
            
    @staticmethod
    def polyn(data, n, ToVS, Type, Bness):    
        """Geçerli bir hata hesabına ihtiyaç var"""
    
        sira=argsort(data[0])
        data[0]=data[0][sira]
        data[1]=data[1][sira]
        
        time_ini = int(data[0][0])

        data[0] = data[0] - time_ini

        z0, z1, z2, z3, z4 = polyfit(data[0], data[1], n, full=True)
        conf = poly1d(z0)
        #print z0,z1,z2,z3,z4
        #print conf
        xrange_ = linspace(min(data[0]),max(data[0]),1000)    
        y_value = conf(xrange_)

        #print sqrt(sum((conf(data[0]) - data[1])**2)/float(len(data[0])-2))

        g = std(conf(data[0]))
        Mintime_Err = Maxtime_Err = sum(((data[1] - conf(data[0]))/g)**2)/len(data[0])
        if Type == 0 or Type == 1:
            if ToVS == 0:
                minm = argmax(y_value) if Bness == 'Magnitude' else argmin(y_value)
                Mintime = xrange_[minm] + time_ini
                #z = len(data[0])/2.
                #Mintime_Err = conf(xrange_[minm])/(float(z0[0])*(z-1))
                if Mintime_Err < 0:
                    Mintime_Err = 0

                return (Mintime, Mintime_Err, xrange_ + time_ini, y_value)                
            else:
                maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
                Maxtime = xrange_[maxm] + time_ini
                #z = len(data[0])/2.
                #Maxtime_Err = conf(xrange_[maxm])/(float(z0[0])*z-1)
                if Maxtime_Err < 0:
                    Maxtime_Err = 0
                return (Maxtime, Maxtime_Err, xrange_ + time_ini, y_value)                
            
        elif Type == 2:
            maxm = argmin(y_value) if Bness == 'Magnitude' else argmax(y_value)
            Maxtime = xrange_[maxm] + time_ini
            return (Maxtime, min(y_value) if Bness == 'Magnitude' else max(y_value),
                    xrange_ + time_ini, y_value)
    
        
    
class Seperator:
    def __init__(self,ToVS,Type,Bness,T0,P):  
        self.ToVS = ToVS
        self.Type = Type
        self.T0=float(T0)
        self.P=float(P)
        self.Bness = Bness

    def Seperate(self,Data):
        self.Data_x=Data[0][argsort(Data[0])]
        self.Data_y=Data[1][argsort(Data[0])]
        
        self.Epoch=(self.Data_x-self.T0)/self.P
        range_ = (int(ceil(self.Epoch[-1])-floor(self.Epoch[0])))
        if self.ToVS == 0:
            Ext1_Data_x = []
            Ext1_Data_y = []
            Ext2_Data_x = []
            Ext2_Data_y = []
            for i in range(range_):
                if self.Type == 0:
                    ERange1 = [0.25, 0.25]
                    ERange2 = [0.25, 0.75]
                elif self.Type == 2:
                    ERange1 = [0.00, 0.50]
                    ERange2 = [0.50, 1.00]
                    
                Ext1_Where = argwhere((self.Epoch > floor(self.Epoch[0]) + i - ERange1[0])&
                (self.Epoch < floor(self.Epoch[0]) + i + ERange1[1]))
                Ext2_Where = argwhere((self.Epoch > floor(self.Epoch[0]) + i + ERange2[0])&
                (self.Epoch < floor(self.Epoch[0]) + i + ERange2[1]))
                
                if len(Ext1_Where) != 0:
                    Ext1_Where = reshape(Ext1_Where, (len(Ext1_Where),))
                    Ext1_Data_x.append(self.Data_x[Ext1_Where])
                    Ext1_Data_y.append(self.Data_y[Ext1_Where])
                else:
                    Ext1_Data_x.append([])
                    Ext1_Data_y.append([])
                
                if len(Ext2_Where) != 0:
                    Ext2_Where = reshape(Ext2_Where, (len(Ext2_Where),))
                    Ext2_Data_x.append(self.Data_x[Ext2_Where])
                    Ext2_Data_y.append(self.Data_y[Ext2_Where])
                else:
                    Ext2_Data_x.append([])
                    Ext2_Data_y.append([])    

            return ([Ext1_Data_x,Ext1_Data_y],[Ext2_Data_x,Ext2_Data_y])
        
        else:
            
            Ext_Data_x = []
            Ext_Data_y = []
            
            for i in range(range_):
                Max_Where = argwhere((self.Epoch > floor(self.Epoch[0]) + i - 0.5)&
                (self.Epoch < floor(self.Epoch[0]) + i + 0.5))
                
                if len(Max_Where) != 0:
                    Max_Where = reshape(Max_Where, (len(Max_Where),))
                    Ext_Data_x.append(self.Data_x[Max_Where])
                    Ext_Data_y.append(self.Data_y[Max_Where])
                else:
                    Ext_Data_x.append([])
                    Ext_Data_y.append([])

            return [Ext_Data_x,Ext_Data_y]
            
    def Data_Stack(self,Data,Stack,Ofac=None,Hifac=None,MACC=None):       
        P = self.P
        if Ofac == None:
            Ofac = 4
        if Hifac == None:
            Hifac = 1
        if MACC == None:
            MACC = 4
        Ext_Data_x = []
        Ext_Data_y = []
        for j in range(len(Data[0])):
                #print Data[0][j]
            #if len(hstack(Data[0][j:j+Stack])) != 0:
                """Her stack için yeni T0 ve P hesaplanıp veri
                öyle kaydırılmalı. Şu an için problemli"""
#                if j % Stack == 0:
#                    PS = lscargle.fasper(hstack(Data[0][j:j+Stack]),hstack(Data[1][j:j+Stack]),
#                                         Ofac,Hifac,MACC)
#                    P = float(2.0/PS[0][PS[3]])
                #try:
                if len(Data[0][j]) != 0:
                    x = []
                    y = []
                    for i in range(int((Stack/2)*-1), int((Stack/2)+1), 1):
                        #print i
                        if i+j >= 0:
                            try:
                                if len(Data[0][i+j]) != 0:
                                    x.append(Data[0][i+j]-i*P)
                                    y.append(Data[1][i+j])
                            except:
                                pass
                            
                    Ext_Data_x.append(hstack(x))
                    Ext_Data_y.append(hstack(y))
#                except:
#                    pass        
    
        return [Ext_Data_x,Ext_Data_y]
    
    def Level(self,Data,lvl):
        Ext_Data_x = []
        Ext_Data_y = []
        for i in range(len(Data[1])):
            if len(Data[0][i]) != 0:
                if self.Type == 0:
                    if self.Bness == 'Magnitude':
                        Ext_Where = argwhere(Data[1][i] > lvl)
                    else:
                        Ext_Where = argwhere(Data[1][i] < lvl)
                else:
                    if self.Bness == 'Magnitude':
                        Ext_Where = argwhere(Data[1][i] < lvl)
                    else:
                        Ext_Where = argwhere(Data[1][i] > lvl)

                Ext_Where = reshape(Ext_Where, (len(Ext_Where),))
                if len(Ext_Where) != 0:
                    Ext_Data_x.append(Data[0][i][Ext_Where])
                    Ext_Data_y.append(Data[1][i][Ext_Where])
                else:
                    Ext_Data_x.append([])
                    Ext_Data_y.append([])
            else:
                Ext_Data_x.append([])
                Ext_Data_y.append([])
                
        return [Ext_Data_x,Ext_Data_y]
    
    def Profil(self,Data,WoPR,WoPL,Points):
        Ext_Data_x = []
        Ext_Data_y = []
        for i in range(len(Data[0])):
            if len(Data[1][i]) != 0:
                if self.Type == 0:
                    if self.Bness == 'Magnitude':
                        Ext = argmax(Data[1][i])
                    else:
                        Ext = argmin(Data[1][i])
                else:
                    if self.Bness == 'Magnitude':
                        Ext = argmin(Data[1][i])
                    else:
                        Ext = argmax(Data[1][i])
                
                #print Ext,Data[0][i][0] + self.P/10. ,Data[0][i][Ext]  , Data[0][i][-1] - self.P/10.
                
#                T = Data[1][i][Ext]
#                E = int((T - self.T0)/self.P)
#                print abs(self.T0+E*self.P - T)
#                if abs(self.T0+E*self.P - T)  < 0.5:
                
                #import matplotlib.pyplot as plt
#                Ext_Where = argwhere((self.Data_x < Data[0][i][Ext] + self.P/WoPR)&
#                                (self.Data_x > Data[0][i][Ext] - self.P/WoPL))
#                Ext_Where = reshape(Ext_Where, (len(Ext_Where),))
#                plt.figure()
#                plt.plot(self.Data_x[Ext_Where],self.Data_y[Ext_Where],'bo')
#                print Points-1, Ext,len(Data[0][i])
                if Points-1 < Ext < len(Data[0][i]) - Points:
                        
                    Ext_Where = argwhere((self.Data_x < Data[0][i][Ext] + self.P/WoPR)&
                                (self.Data_x > Data[0][i][Ext] - self.P/WoPL))
                    Ext_Where = reshape(Ext_Where, (len(Ext_Where),))
                    #print len(Ext_Where)
                    #print 'ext where',len(Ext_Where)
                    Data_x = self.Data_x[Ext_Where]
                    Data_y = self.Data_y[Ext_Where]
                    #z0 = polyfit(Data_x, Data_y, 1)    
                    #conf = poly1d(z0)
                    
                    #g = std(conf(self.Data_x[Ext_Where]))
                    #err = sum(((Data_y - conf(Data_x))/g)**2)/len(Data_x)
                    
                    if len(Ext_Where) > 2:# and err > 1:
                            Ext_Data_x.append(Data_x)
                            Ext_Data_y.append(Data_y)
                    else:
                        Ext_Data_x.append([])
                        Ext_Data_y.append([])                        
                else:
                    Ext_Data_x.append([])
                    Ext_Data_y.append([])
            else:
                Ext_Data_x.append([])
                Ext_Data_y.append([])
                
        return [Ext_Data_x,Ext_Data_y]
        
def OC(mins,types,T0,P):
    T0 = float(T0)
    P = float(P)
    
    epoch=(mins-T0)/P
  
    Eduz = arange(0,dtype=float)
    OC = arange(0,dtype=float)
    for i in range(len(epoch)):
        if (types[i] == 1):
                Eduz = hstack((Eduz,round(epoch[i])))            
                C = float(T0)+round(epoch[i])*P
                OC = hstack((OC,mins[i]-C))                                    
                
        else:
                Eduz = hstack((Eduz,floor(epoch[i])+0.5))            
                C = float(T0)+(floor(epoch[i])+0.5)*P
                OC = hstack((OC,mins[i]-C))
        
    return (Eduz,OC)

def PlotRangeData(curve, range_):
    """Guiqwt içinde çözülmeli"""
    
    x0, x1 = range_.get_range()
    data = curve.get_data()
    X = data[0]
    i0 = X.searchsorted(x0)
    i1 = X.searchsorted(x1)
    if i0 > i1:
        i0, i1 = i1, i0
    vectors = []
    for vector in data:
        if vector is None:
            vectors.append(None)
        elif i0 == i1:
            #import numpy as np
            vectors.append(array([NaN]))
        else:
            vectors.append(vector[i0:i1])
    
    return vectors

def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    import sys
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True
 
    return array(maxtab), array(mintab)
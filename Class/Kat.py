import pandas as pd

from .Tablolar import *
from .Kuvvet import kuvvet

PI = 3.14
C = 0.8 # Burkulma katsayısı



#deklem 1.2
def X_d(C_n,C_y,omega,X_k):
    #X_k  : Karakteristik dayanım
    #omega: Malzeme kısmi güvenlik katsayısı
    #C_n  : Kullanım sınıfına bağlı nem durumu düzeltme katsayısı
    #C_y  : Yük etki sınıfına bağlı yük etki süresi düzeltme katsayısı
    return (C_n*C_y*X_k) / omega

def E_d(E_ort,omega):
    #E_ort : Elastisite modülü ortalama değeri
    #omega : Malzeme kısmi güvenlik katsayısı
    return E_ort/omega

def G_d(G_ort,omega):
    #G_ort : Kayma modülü ortalama değeri
    #omega : Malzeme kısmi güvenlik katsayısı
    return G_ort/omega

# Farklı özelikte 2 ahşap için Cn / denklem 1.4
def C_n_ort(C_n_1,C_n_2):
    return (C_n_1*C_n_2)**0.5

# Farklı özelikte 2 ahşap için Cy / denklem 1.5
def C_y_ort(C_y_1,C_y_2):
    return (C_y_1*C_y_2)**0.5

#denklem 1.6 veya tablo 1.7
def k_def(w_sünme,w_ani):
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    #w_sünme : Sünme kaynaklı sehim
    #w_ani : Ani sehim
    return w_sünme/w_ani

#denklem 1.7
def E_ort_son(E_ort,k_def_ort):
    #E_ort : ortalama elastisite modülü
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    return E_ort/(1+k_def_ort)

#denklem 1.7
def G_ort_son(G_ort,k_def_ort):
    #G_ort ortalama kayma modülü
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    return G_ort/(1+k_def_ort)

#denklem 1.7
def K_ort_son(K_ser,k_def_ort):
    #K_ser arayüz kayma rijitliği
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    return K_ser/(1+k_def_ort)

#denklem 1.8
def E_ort_son(E_ort,k_def_ort,psi):
    #E_ort : ortalama elastisite modülü
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    #psi : Kısmi yük katsayısı
    return E_ort/(1+k_def_ort*psi)

#denklem 1.8
def G_ort_son(G_ort,k_def_ort,psi):
    #G_ort ortalama kayma modülü
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    #psi : Kısmi yük katsayısı
    return G_ort/(1+k_def_ort*psi)

#denklem 1.8
def K_ort_son(K_ser,k_def_ort,psi):
    #K_ser arayüz kayma rijitliği
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    #psi : Kısmi yük katsayısı
    return K_ser/(1+k_def_ort*psi)

#denklem 1.9
def k_def_ort(k_def_1,k_def_2):
    #k_def : Zamana bağlı şekil değiştrime davranışı için düzeltme katsayısı
    return ((k_def_1*k_def_2)**0.5)*2




#_--------__---__-__--_--___

def C_y_tablo(malzeme: str, nem_durumu: str):
    filtre = (tablo_C_y["Malzeme"] == malzeme) & (tablo_C_y["Nem Durumu Katsayıları"] == nem_durumu)
    C_y_tablo = tablo_C_y[filtre]
    return C_y_tablo

def C_y(kuvvet:kuvvet,C_y_tablo:pd.DataFrame):
    g_kat, q_kat, e_kat = C_y_tablo[["Kalıcı Etki", "Orta Süreli Etki", "Anlık Etki"]].values[0]
    C_y = (kuvvet.G * g_kat + kuvvet.Q * q_kat + kuvvet.E *e_kat) / 3
    return C_y

def C_n(nem_durumu : str):
    C_n = tablo_Cn.loc[
    tablo_Cn["Nem Durumu"] == nem_durumu,
    "Nem Durumu Düzeltme Katsayısı,Cn"
    ].values[0]
    return C_n

# Burada lambda_x ve lambda_y için ayrı kullanmaya gerek yok
def lambda_xy(l:float,i:float):
    return l/i

def omega(temel_yuk_bilesimi:str):
    return tablo_omega.loc[temel_yuk_bilesimi].values[0]

def f_E_xy(E005,lambda_xy):
    return ((PI**2)*E005)/(lambda_xy**2)

def f_c_0_d(f_c_0_k,C_n,C_y,C_b,omega):
    return (f_c_0_k*C_n*C_y*C_b)/omega

def C_p(f_E,f_c_0_k,c=C):
    x = f_E/f_c_0_k
    x1 = (1+x) / 2*c
    x2 = ((1 + x**2) / (2*c))**2
    x3 = x / c
    return x1 - (x2 - x3)**0.5

def sigma_c_0_d():
    pass


"""Burayı yap tablodan verileri çek ve a.py de kullan"""
# Boyut katsayısı denklemi
# örnek Masif ahşap için boyut katsayısı (C_b) bölüm 2.2
# C_b(h,150,0.2,1.3) -> min([(150/h)**0.2 , 1.3])
def C_b_(h,sabit,üst,kiyas):
    return min([(sabit/h)**üst,kiyas])






def A_g(b,h):
    return b*h
def l(b,h):
    return (b*(h**3))/12
def i(l,Ag):
    return (l/Ag)**0.5




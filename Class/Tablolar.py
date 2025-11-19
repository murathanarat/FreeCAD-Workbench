import pandas as pd
import os

__dosya_yolu = os.path.abspath(__file__)
__klasor_yolu = os.path.dirname(__dosya_yolu)

__klasor_yolu = r"C:\Users\murat\Desktop\Ahsap Hesap Program\Program"


__tablo1_2 = __klasor_yolu + r"\Tablolar\tablo1.2.txt"
tablo_onogks = pd.read_csv(__tablo1_2,header=0,sep=";") 
tablo1_3 = __klasor_yolu + r"\Tablolar\tablo1.3.txt"
tablo_omega = pd.read_csv(tablo1_3,header=0,sep=";",index_col=0) 
tablo1_4 = __klasor_yolu + r"\Tablolar\tablo1.4.txt"
tablo_Cn = pd.read_csv(tablo1_4,header=0,sep=";") 
tablo1_5 = __klasor_yolu + r"\Tablolar\tablo1.5.txt"
tablo_yes = pd.read_csv(tablo1_5,header=0,sep=";") 
tablo1_6 = __klasor_yolu + r"\Tablolar\tablo1.6.txt"
tablo_C_y = pd.read_csv(tablo1_6,header=0,sep=";") 
tablo1_7 = __klasor_yolu + r"\Tablolar\tablo1.7.txt"
tablo_Kdef = pd.read_csv(tablo1_7,header=0,sep=";") 
tablo1_7 = __klasor_yolu + r"\Tablolar\tablo1.7.txt"
tablo_Kdef = pd.read_csv(tablo1_7,header=0,sep=";") 

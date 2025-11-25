import os
import pandas as pd

# Bu dosyanın bulunduğu klasör
__klasor_yolu = os.path.dirname(os.path.abspath(__file__))

# Eğer Tablolar klasörü Proje altında ise:
proje_klasoru = os.path.dirname(__klasor_yolu)  # Class'ın üstü
tablolar_klasoru = os.path.join(proje_klasoru, "Tablolar")
# Dosya yolları
tablo1_2 = os.path.join(tablolar_klasoru, "tablo1.2.txt")
tablo_onogks = pd.read_csv(tablo1_2, header=0, sep=";")

tablo1_3 = os.path.join(tablolar_klasoru, "tablo1.3.txt")
tablo_omega = pd.read_csv(tablo1_3, header=0, sep=";", index_col=0)

tablo1_4 = os.path.join(tablolar_klasoru, "tablo1.4.txt")
tablo_Cn = pd.read_csv(tablo1_4, header=0, sep=";")

tablo1_5 = os.path.join(tablolar_klasoru, "tablo1.5.txt")
tablo_yes = pd.read_csv(tablo1_5, header=0, sep=";")

tablo1_6 = os.path.join(tablolar_klasoru, "tablo1.6.txt")
tablo_C_y = pd.read_csv(tablo1_6, header=0, sep=";")

tablo1_7 = os.path.join(tablolar_klasoru, "tablo1.7.txt")
tablo_Kdef = pd.read_csv(tablo1_7, header=0, sep=";")

malzemeler_path = os.path.join(tablolar_klasoru, "malzemeler.txt")
malzemeler_tablo = pd.read_csv(malzemeler_path, header=0, sep=";")

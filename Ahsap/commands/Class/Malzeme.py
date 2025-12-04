import pandas as pd
from io import StringIO

class Malzeme:
    # ---- Sınıf içi gizli DataFrame ----
    __data_text = """
Malzeme;fmk;ft0k;ft90k;fc0k;fc90k;fvk;E0ort;E005;E90ort;Gort;pk;port
D18;18;11;0.6;18;4.8;3.5;9.5;8;0.63;0.59;475;570
D24;24;14;0.6;21;4.9;3.7;10;8.4;0.67;0.63;485;580
D27;27;16;0.6;22;5.1;3.8;10.5;8.8;0.7;0.66;510;610
D30;30;18;0.6;24;5.3;3.9;11;9.2;0.73;0.69;530;640
D35;35;21;0.6;25;5.4;4.1;12;10.1;0.8;0.75;540;650
D40;40;24;0.6;27;5.5;4.2;13;10.9;0.87;0.81;550;660
D45;45;27;0.6;29;5.8;4.4;13.5;11.3;0.9;0.84;580;700
D50;50;30;0.6;30;6.2;4.5;14;11.8;0.93;0.88;620;740
D55;55;33;0.6;32;6.6;4.7;15.5;13;1.03;0.97;660;790
D60;60;36;0.6;33;10.5;4.8;17;14.3;1.13;1.06;700;840
D65;65;39;0.6;35;11.3;5;18.5;15.5;1.23;1.16;750;900
D70;70;42;0.6;36;12;5;20;16.8;1.33;1.25;800;960
D75;75;45;0.6;37;12.8;5;22;18.5;1.47;1.38;850;1020
D80;80;48;0.6;38;13.5;5;24;20.2;1.6;1.5;900;1080
C14;14;7.2;0.4;16;2;3;7;4.7;0.23;0.44;290;350
C16;16;8.5;0.4;17;2.2;3.2;8;5.4;0.27;0.5;310;370
C18;18;10;0.4;18;2.2;3.4;9;6;0.3;0.56;320;380
C20;20;11.5;0.4;19;2.3;3.6;9.5;6.4;0.32;0.59;330;400
C22;22;13;0.4;20;2.4;3.8;10;6.7;0.33;0.63;340;410
C24;24;14.5;0.4;21;2.5;4;11;7.4;0.37;0.69;350;420
C27;27;16.5;0.4;22;2.5;4;11.5;7.7;0.38;0.72;360;430
C30;30;19;0.4;24;2.7;4;12;8;0.4;0.75;380;460
C35;35;22.5;0.4;25;2.7;4;13;8.7;0.43;0.81;390;470
C40;40;26;0.4;27;2.8;4;14;9.4;0.47;0.88;400;480
C45;45;30;0.4;29;2.9;4;15;10.1;0.5;0.94;410;490
C50;50;33.5;0.4;30;3;4;16;10.7;0.53;1;430;520
T8;13.5;8;0.4;16;2;2.8;7;4.7;0.23;0.44;290;350
T9;14.5;9;0.4;17;2.1;3;7.5;5;0.25;0.47;300;360
T10;16;10;0.4;17;2.2;3.2;8;5.4;0.27;0.5;310;370
T11;17;11;0.4;18;2.2;3.4;9;6;0.3;0.56;320;380
T12;18;12;0.4;19;2.3;3.6;9.5;6.4;0.32;0.59;330;400
T13;19.5;13;0.4;20;2.4;3.8;10;6.7;0.33;0.63;340;410
T14;20.5;14;0.4;21;2.5;4;11;7.4;0.37;0.69;350;420
T14.5;21;14.5;0.4;21;2.5;4;11;7.4;0.37;0.69;350;420
T15;22;15;0.4;21;2.5;4;11.5;7.7;0.38;0.72;360;430
T16;23;16;0.4;22;2.6;4;11.5;7.7;0.38;0.72;370;440
T18;25.5;18;0.4;23;2.7;4;12;8;0.4;0.75;380;460
T21;29;21;0.4;25;2.7;4;13;8.7;0.43;0.81;390;470
T22;30.5;22;0.4;26;2.7;4;13;8.7;0.43;0.81;390;470
T24;33;24;0.4;27;2.8;4;13.5;9;0.45;0.84;400;480
T26;35;26;0.4;28;2.9;4;14;9.4;0.47;0.88;410;490
T27;36.5;27;0.4;29;2.9;4;15;10.1;0.5;0.94;410;490
T28;37.5;28;0.4;29;2.9;4;15;10.1;0.5;0.94;420;500
T30;40;30;0.4;30;3;4;15.5;10.4;0.52;0.97;430;520
"""

    __df = pd.read_csv(StringIO(__data_text), sep=';', index_col=0)

    # Sadece sınıf üzerinden erişim için private
    __malzemeler = __df.index.values
    __parametreler = __df.columns.values

    # Sınıf metodları
    @classmethod
    def get_malzemeler(cls):
        return cls.__df.copy()

    @classmethod
    def get_malzeme_ad(cls):
        return cls.__malzemeler.copy()

    @classmethod
    def get_parametreler(cls):
        return cls.__parametreler.copy()
    
    # ---- Nesne metodu ----
    def __init__(self, malzeme_adi: str):
        if malzeme_adi not in self.__df.index:
            raise ValueError(f"{malzeme_adi} isimli malzeme bulunamadı.")
        self.__malzeme = self.__df.loc[malzeme_adi]  # Series olarak satır

    def get(self, parametre: str):
        if parametre in self.__malzeme.index:
            return self.__malzeme[parametre]
        raise ValueError(f"{parametre} parametresi bulunamadı.")
    
    def get_malzeme(self):
        return self.__malzeme

    def __str__(self):
        lines = [f"Malzeme : {self.__malzeme.name}"]
        width = max(len(col) for col in self.__malzeme.index) + 1
        for col, val in self.__malzeme.items():
            lines.append(f"{col.ljust(width)} : {val}")
        return "\n".join(lines)


"""# Nesne üretme
malzeme_d18 = Malzeme("D18")

# Tüm malzeme adlarını yazdırma
print(Malzeme.get_malzeme_ad())

# Tüm malzemeleri ve özeliklerini yazdırma
print(Malzeme.get_malzemeler())

# Tüm parametreleri yazdırma
print(Malzeme.get_parametreler())

# Malzeme özeliklerini yazdırma (pd dataframe dir direk buradan da özeliklerere erişile bilir)
print(malzeme_d18.get_malzeme())

# Malzeme özeliklerini yazdırma (tablo olarak yazdırır)
print(malzeme_d18)

# Malzeme D18 in fvk özeliğini getirir
print(malzeme_d18.get("fvk"))

# Basit işlem 
a = malzeme_d18.get("fvk") * malzeme_d18.get("E0ort")
print(a)
"""

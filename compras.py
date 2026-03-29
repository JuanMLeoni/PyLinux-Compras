import pandas as pd
df = pd.read_csv('COM\PyLinux-Compras\Compras.csv')

while True:
    print("1. Ver ventas por sucursal y producto")
    print("2. Ver minimo y máximo de ventas y cantidad de productos vendidos por sucursal")
    print("3. Ver cantidad de sucursales y total de ventas en todas las sucursales")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

#-----------------------------------------------------------------------------------------------------#

    if opcion == "1":
        i = 0
        Su = df['PRSUC'][0]
        Pr = df['PRCOD'][0]
        TOTUNI = 0
        TOTPES = 0
        print(f"* Sucursal: \033[35m{Su}\033[0m *")
        print("*" * 19)
        while i < len(df):
            if df['PRSUC'][i] == Su:
                if df['PRCOD'][i] == Pr:
                    TOTUNI += df['PRCANT'][i]
                    TOTPES = round(TOTPES + (df['PRCANT'][i] * df['PRPRE'][i]), 2)
                else:
                    print(f"Producto: \033[33m{df['PRCOD'][i-1]}\033[0m: Cantidad Total: \033[36m{TOTUNI}\033[0m, Ventas totales: \033[32m{TOTPES}\033[0m")
                    TOTUNI = 0
                    TOTPES = 0
                    Pr = df['PRCOD'][i]
            else:
                print(f"Producto: \033[33m{df['PRCOD'][i-1]}\033[0m: Cantidad Total: \033[36m{TOTUNI}\033[0m, Ventas totales: \033[32m{TOTPES}\033[0m")
                Su = df['PRSUC'][i]
                print(f"* Sucursal: \033[35m{Su}\033[0m *")
                print("*" * 19)
                Pr = df['PRCOD'][i]
                TOTUNI = 0
                TOTPES = 0
            i += 1
        print(f"Producto: \033[33m{df['PRCOD'][i-1]}\033[0m: Cantidad Total: \033[36m{TOTUNI}\033[0m, Ventas totales: \033[32m{TOTPES}\033[0m")
        print("/" * 20)

#-----------------------------------------------------------------------------------------------------#

    elif opcion == "2":
        i = 0
        Su = df['PRSUC'][0]
        Pr = df['PRCOD'][0]
        TOTSUC = 0
        MYPROD = 0
        MYIMPOR = 0
        MNPRO = 0
        MNIMPOR = 0
        print("-" * 19)
        print(f"* Sucursal: \033[35m{Su}\033[0m *")
        print("*" * 19)
        while i < len(df):
            if df['PRSUC'][i] == Su:
                if df['PRCOD'][i] == Pr:
                    TOTSUC += df['PRCANT'][i]
                    IMPOR = round(df['PRCANT'][i] * df['PRPRE'][i], 2)
                    if IMPOR > MYIMPOR:
                        MYIMPOR = IMPOR
                        MYPROD = df['PRCOD'][i]
                    if IMPOR < MNIMPOR or MNIMPOR == 0:
                        MNIMPOR = IMPOR
                        MNPRO = df['PRCOD'][i]
                else:
                    Pr = df['PRCOD'][i]
            else:
                print(f"Total de productos vendidos: \033[36m{TOTSUC}\033[0m \nProducto más vendido: \033[33m{MYPROD}\033[0m con un importe de \033[32m{MYIMPOR}\033[0m \nProducto menos vendido: \033[33m{MNPRO}\033[0m con un importe de \033[31m{MNIMPOR}\033[0m")
                print("-" * 19)
                Su = df['PRSUC'][i]
                print(f"* Sucursal: \033[35m{Su}\033[0m *")
                print("*" * 19)
                Pr = df['PRCOD'][i]
                TOTSUC = 0
                MYPROD = 0
                MYIMPOR = 0
                MNPRO = 0
                MNIMPOR = 0
            i += 1
        print(f"Total de productos vendidos: \033[36m{TOTSUC}\033[0m \nProducto más vendido: \033[33m{MYPROD}\033[0m con un importe de \033[32m{MYIMPOR}\033[0m \nProducto menos vendido: \033[33m{MNPRO}\033[0m con un importe de \033[31m{MNIMPOR}\033[0m")
        print("/" * 19)
        
#-----------------------------------------------------------------------------------------------------#

    elif opcion == "3":
        i = 0
        Su = df['PRSUC'][0]
        Pr = df['PRCOD'][0]
        CANSUC = 1
        TOTALIMP = 0
        while i < len(df):
            if df['PRSUC'][i] == Su:
                TOTALIMP = round(TOTALIMP + (df['PRCANT'][i] * df['PRPRE'][i]), 2)
            else:
                CANSUC += 1
                Su = df['PRSUC'][i]
            i += 1
        print("-" * 19)
        print(f"Cantidad de sucursales: \033[35m{CANSUC}\033[0m \nTotal de ventas: \033[32m{TOTALIMP}\033[0m")
        print("/" * 19)

#-----------------------------------------------------------------------------------------------------#

    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

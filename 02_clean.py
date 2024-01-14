import csv
import pandas as pd


def limpiar_archivo_texto(archivo_entrada, archivo_salida, archivo_errores):
    with open(archivo_entrada, "r", encoding="utf-8") as entrada, open(
        archivo_salida, "w", encoding="utf-8"
    ) as salida, open(archivo_errores, "w", encoding="utf-8") as errores:
        num_linea = 0

        for linea in entrada:
            num_linea += 1

            if len(linea.strip()) >= 55:
                salida.write(linea)
            else:
                # Guardar la línea errónea en el archivo de errores
                errores.write(f"Error en la línea {num_linea}: {linea}")


def unificar_comas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, "r", encoding="utf-8") as entrada, open(
        archivo_salida, "w", encoding="utf-8"
    ) as salida:
        for linea in entrada:
            # Contar la cantidad de comas en la línea
            cantidad_comas = linea.count(",")

            if cantidad_comas != 12:
                # Calcular la cantidad de comas que faltan o sobran
                diferencia_comas = 12 - cantidad_comas

                if diferencia_comas > 0:
                    # Agregar comas al final de la línea
                    nueva_linea = f'{linea.strip()}{"," * diferencia_comas}\n'
                elif diferencia_comas < 0:
                    # Quitar comas del final de la línea
                    nueva_linea = ",".join(linea.strip().rsplit(",", 12)[:12]) + "\n"
            else:
                nueva_linea = linea

            salida.write(nueva_linea)


## unified
def limpiar_csv_final(archivo_entrada, archivo_salida):
    # Cargar el archivo CSV en un DataFrame de pandas
    df = pd.read_csv(archivo_entrada, header=None)

    # Eliminar columnas vacías
    df = df.dropna(axis=1, how="all")

    # Verificar si hay nombres de columna ya existentes
    if all(str(col).isdigit() for col in df.columns):
        # Si todas las columnas son números, agregar encabezado genérico
        encabezado = [f"col{i+1}" for i in range(len(df.columns))]
        df.columns = encabezado

    # Eliminar registros duplicados
    df = df.drop_duplicates()

    # Guardar el DataFrame limpio en un nuevo archivo CSV
    df.to_csv(archivo_salida, index=False)


if __name__ == "__main__":
    archivo_entrada = "full_data_pages.csv"
    archivo_salida = "full_data_pages_fixed.csv"

    archivo_salida_unificado = "full_data_pages_fixed_lines.csv"

    archivo_errores = "full_data_pages_errors.csv"

    archivo_salida_csv = "final_data.csv"
    archivo_salida_csv2 = "final_data2.csv"

    limpiar_archivo_texto(archivo_entrada, archivo_salida, archivo_errores)
    print("Proceso 1 completado de length clean.")

    unificar_comas(archivo_salida, archivo_salida_unificado)
    print("Proceso 2 de unificación de comas")

    ## test2
    limpiar_csv_final(archivo_salida_unificado, archivo_salida_csv2)
    print("Proceso 3 de limpieza con pandas")

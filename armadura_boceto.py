import math


# Diccionario de tornillos basado en la tabla
tornillos = {
    "A307": {
        "Tension": {"MPa": 310, "kg/cm²": 3160},
        "Cortante": {
            "Con_cuerda_incluida": {"MPa": 186, "kg/cm²": 1900},
            "Con_cuerda_excluida": {"MPa": 186, "kg/cm²": 1900}
        }
    },
    "A325": {
        "Tension": {"MPa": 620, "kg/cm²": 6320},
        "Cortante": {
            "Con_cuerda_incluida": {"MPa": 372, "kg/cm²": 3800},
            "Con_cuerda_excluida": {"MPa": 469, "kg/cm²": 4780}
        }
    },
    "A490": {
        "Tension": {"MPa": 780, "kg/cm²": 7950},
        "Cortante": {
            "Con_cuerda_incluida": {"MPa": 469, "kg/cm²": 4780},
            "Con_cuerda_excluida": {"MPa": 579, "kg/cm²": 5900}
        }
    },
    "Factores": {
        "Partes_roscadas": {
            "Tension": 0.75,
            "Cortante_incluida": 0.45,
            "Cortante_excluida": 0.56
        }
    }
}
diametros_tornillos = [13, 16, 19, 22, 25,
                       28, 32, 36, 38, 45]  # Diámetros en mm


# Ejemplo de acceso a los datos
for tipo, datos in tornillos.items():
    print(f"Tornillo: {tipo}")
    for propiedad, valores in datos.items():
        print(f"  {propiedad}: {valores}")


# Diccionario para soldaduras
soldaduras = {
    "E60": {
        "Fy": {"MPa": 330},
        "Fu": {"MPa": 410}
    },
    "E70": {
        "Fy": {"MPa": 365},
        "Fu": {"MPa": 480}
    }
}

# Diccionario de materiales corregido
materials = {
    "NMX-B-060": {
        "ASTM": None,
        "Grados": {
            "Clase A": {"Grado": "N/A", "F_y": 230, "F_u": 310},
            "Clase B": {"Grado": "N/A", "F_y": 255, "F_u": 360},
            "Clase C": {"Grado": "N/A", "F_y": 275, "F_u": 380},
            "Clase D": {"Grado": "N/A", "F_y": 345, "F_u": 450},
            "Clase E": {"Grado": "N/A", "F_y": 550, "F_u": 570},
            "Clase F": {"Grado": "N/A", "F_y": 345, "F_u": 480}
        }
    },
    "NMX-B-066": {
        "ASTM": None,
        "Grados": {
            "Clase A": {"Grado": "N/A", "F_y": 230, "F_u": 310},
            "Clase B": {"Grado": "N/A", "F_y": 255, "F_u": 360},
            "Clase C": {"Grado": "N/A", "F_y": 275, "F_u": 380},
            "Clase D": {"Grado": "N/A", "F_y": 345, "F_u": 450},
            "Clase E": {"Grado": "N/A", "F_y": 550, "F_u": 570},
            "Clase F": {"Grado": "N/A", "F_y": 345, "F_u": 480}
        }
    },
    "NMX-B-254": {
        "ASTM": "A36/A36M",
        "Grados": {
            "Planchas y barras": {"Grado": "36", "F_y": 250, "F_u": 400},
            "Perfiles": {"Grado": "36", "F_y": 250, "F_u": 400}
        }
    },
    "NMX-B-284": {
        "ASTM": "A572/A572M",
        "Grados": {
            "A": {
                "290": {"Grado": "290", "F_y": 290, "F_u": 415},
                "345": {"Grado": "345", "F_y": 345, "F_u": 450},
                "380": {"Grado": "380", "F_y": 380, "F_u": 485},
                "415": {"Grado": "415", "F_y": 415, "F_u": 520},
                "450": {"Grado": "450", "F_y": 450, "F_u": 550}
            },
            "B": {
                "345": {"Grado": "345", "F_y": 345, "F_u": 450},
                "C": {"Grado": "345", "F_y": 345, "F_u": 450}
            }
        }
    },
    # Puedes añadir más normas y grados según sea necesario
}

# Factores de reducción
Fr1 = 0.9   # Factor de reducción para la barra
Fr2 = 0.75  # Factor de reducción para el tornillo


# Diccionario unificado con todos los perfiles
perfiles = {
    # Perfiles TR 102
    "TR 102 x 7.5": {
        "Peso": 7.5,
        "Area": 9.5,
        "d/tw": 23.2,
        "Eje_X-X": {"I": 89, "S": 11.8, "r": 3.05, "y": 2.4},
        "Eje_Y-Y": {"I": 44, "S": 8.7, "r": 2.13},
        "Constante de torsion": 0.95,
        "Dimensiones": {"d": 100, "tw": 4.3, "bf": 100, "tf": 5.2, "k": 15.9}
    },
    "TR 102 x 9.7": {
        "Peso": 9.7,
        "Area": 12.4,
        "d/tw": 17.4,
        "Eje_X-X": {"I": 116, "S": 13.1, "r": 2.6, "y": 2.57},
        "Eje_Y-Y": {"I": 57, "S": 11.2, "r": 2.14},
        "Constante de torsion": 1.84,
        "Dimensiones": {"d": 100, "tw": 5.6, "bf": 100, "tf": 6.5, "k": 17.5}
    },
    "TR 102 x 11.2": {
        "Peso": 11.2,
        "Area": 14.3,
        "d/tw": 17.6,
        "Eje_X-X": {"I": 137, "S": 17.6, "r": 3.07, "y": 2.52},
        "Eje_Y-Y": {"I": 71, "S": 13.9, "r": 2.22},
        "Constante de torsion": 3.03,
        "Dimensiones": {"d": 103, "tw": 5.8, "bf": 103, "tf": 8.4, "k": 19}
    },
    "TR 102 x 13.3": {
        "Peso": 13.3,
        "Area": 17,
        "d/tw": 17.7,
        "Eje_X-X": {"I": 142, "S": 17.2, "r": 2.89, "y": 2.12},
        "Eje_Y-Y": {"I": 166, "S": 24.9, "r": 3.12},
        "Constante de torsion": 3.61,
        "Dimensiones": {"d": 103, "tw": 6.4, "bf": 103, "tf": 8.8, "k": 20.6}
    },
    "TR 102 x 15.6": {
        "Peso": 15.6,
        "Area": 19.9,
        "d/tw": 16.5,
        "Eje_X-X": {"I": 162, "S": 19.3, "r": 2.85, "y": 2.11},
        "Eje_Y-Y": {"I": 204, "S": 30.3, "r": 3.19},
        "Constante de torsion": 6.12,
        "Dimensiones": {"d": 105, "tw": 6.8, "bf": 105, "tf": 8.9, "k": 20.6}
    },
    "TR 102 x 17.9": {
        "Peso": 17.9,
        "Area": 22.8,
        "d/tw": 16.1,
        "Eje_X-X": {"I": 147, "S": 17.7, "r": 2.53, "y": 1.76},
        "Eje_Y-Y": {"I": 380, "S": 46, "r": 4.07},
        "Constante de torsion": 7.4,
        "Dimensiones": {"d": 101, "tw": 7.6, "bf": 166, "tf": 11.8, "k": 22}
    },
    "TR 102 x 20.9": {
        "Peso": 20.9,
        "Area": 26.6,
        "d/tw": 14.2,
        "Eje_X-X": {"I": 176, "S": 21, "r": 2.57, "y": 1.86},
        "Eje_Y-Y": {"I": 450, "S": 54.2, "r": 4.11},
        "Constante de torsion": 11.3,
        "Dimensiones": {"d": 102, "tw": 7.2, "bf": 166, "tf": 11.8, "k": 23.8}
    },
    "TR 102 x 23.1": {
        "Peso": 23.1,
        "Area": 29.4,
        "d/tw": 14,
        "Eje_X-X": {"I": 178, "S": 20.1, "r": 2.46, "y": 1.7},
        "Eje_Y-Y": {"I": 770, "S": 86, "r": 5.12},
        "Constante de torsion": 11.3,
        "Dimensiones": {"d": 104, "tw": 7.2, "bf": 166, "tf": 13.1, "k": 25.4}
    },
    "TR 102 x 26": {
        "Peso": 26,
        "Area": 33.3,
        "d/tw": 12.5,
        "Eje_X-X": {"I": 200, "S": 23.4, "r": 2.46, "y": 1.75},
        "Eje_Y-Y": {"I": 887, "S": 86, "r": 5.17},
        "Constante de torsion": 16.1,
        "Dimensiones": {"d": 102, "tw": 7.6, "bf": 204, "tf": 13.2, "k": 26.4}
    },
    "TR 102 x 29.7": {
        "Peso": 29.7,
        "Area": 37.9,
        "d/tw": 11.7,
        "Eje_X-X": {"I": 258, "S": 32.3, "r": 2.5, "y": 1.97},
        "Eje_Y-Y": {"I": 1270, "S": 123.2, "r": 5.28},
        "Constante de torsion": 23.7,
        "Dimensiones": {"d": 104, "tw": 8, "bf": 204, "tf": 15.1, "k": 27.8}
    },
    "TR 102 x 35.7": {
        "Peso": 35.7,
        "Area": 45.5,
        "d/tw": 10.6,
        "Eje_X-X": {"I": 350, "S": 42.7, "r": 2.62, "y": 2.22},
        "Eje_Y-Y": {"I": 1621, "S": 149.6, "r": 5.32},
        "Constante de torsion": 69.7,
        "Dimensiones": {"d": 105, "tw": 8.5, "bf": 204, "tf": 16.2, "k": 29.8}
    },
    "TR 102 x 49.8": {
        "Peso": 49.8,
        "Area": 63.5,
        "d/tw": 7.9,
        "Eje_X-X": {"I": 454, "S": 50, "r": 2.67, "y": 2.38},
        "Eje_Y-Y": {"I": 1844, "S": 175.3, "r": 5.39},
        "Constante de torsion": 105,
        "Dimensiones": {"d": 114, "tw": 14.5, "bf": 210, "tf": 23.7, "k": 36.5}
    },
    # Perfiles TR 152
    "TR 152 x 10.5": {
        "Peso": 10.5,
        "Area": 13.4,
        "d/tw": 29.8,
        "Eje_X-X": {"I": 319, "S": 30.1, "r": 4.87, "y": 4.41},
        "Eje_Y-Y": {"I": 49, "S": 9.7, "r": 1.9},
        "Constante de torsion": 1.64,
        "Dimensiones": {"d": 151, "tw": 5.1, "bf": 101, "tf": 5.7, "k": 17.5}
    },
    "TR 152 x 12": {
        "Peso": 12,
        "Area": 15.2,
        "d/tw": 27.3,
        "Eje_X-X": {"I": 362, "S": 33.6, "r": 4.87, "y": 4.38},
        "Eje_Y-Y": {"I": 59, "S": 11.6, "r": 1.96},
        "Constante de torsion": 2.32,
        "Dimensiones": {"d": 152, "tw": 5.6, "bf": 101, "tf": 6.7, "k": 19}
    },
    "TR 152 x 14.1": {
        "Peso": 14.1,
        "Area": 18,
        "d/tw": 25.9,
        "Eje_X-X": {"I": 420, "S": 37.4, "r": 4.82, "y": 4.16},
        "Eje_Y-Y": {"I": 78, "S": 15.4, "r": 2.08},
        "Constante de torsion": 3.98,
        "Dimensiones": {"d": 154, "tw": 6, "bf": 102, "tf": 8.9, "k": 20.6}
    },
    "TR 152 x 16.4": {
        "Peso": 16.4,
        "Area": 20.9,
        "d/tw": 23.7,
        "Eje_X-X": {"I": 477, "S": 42.4, "r": 4.82, "y": 4.12},
        "Eje_Y-Y": {"I": 97, "S": 19, "r": 2.15},
        "Constante de torsion": 6.34,
        "Dimensiones": {"d": 156, "tw": 5.6, "bf": 102, "tf": 10.8, "k": 22.2}
    },
    "TR 152 x 19.3": {
        "Peso": 19.3,
        "Area": 24.6,
        "d/tw": 26.5,
        "Eje_X-X": {"I": 487, "S": 39.3, "r": 4.43, "y": 3.15},
        "Eje_Y-Y": {"I": 360, "S": 43.8, "r": 3.81},
        "Constante de torsion": 6.5,
        "Dimensiones": {"d": 155, "tw": 5.8, "bf": 105, "tf": 8.4, "k": 31.8}
    },
    "TR 152 x 22.3": {
        "Peso": 22.3,
        "Area": 28.4,
        "d/tw": 23.7,
        "Eje_X-X": {"I": 562, "S": 45.1, "r": 4.44, "y": 3.21},
        "Eje_Y-Y": {"I": 425, "S": 51.1, "r": 3.86},
        "Constante de torsion": 9.76,
        "Dimensiones": {"d": 153, "tw": 8.5, "bf": 204, "tf": 14.6, "k": 31.8}
    },
    "TR 152 x 26.2": {
        "Peso": 26.2,
        "Area": 33.4,
        "d/tw": 20.9,
        "Eje_X-X": {"I": 666, "S": 52.9, "r": 4.45, "y": 3.3},
        "Eje_Y-Y": {"I": 508, "S": 61.1, "r": 3.9},
        "Constante de torsion": 16,
        "Dimensiones": {"d": 159, "tw": 7.6, "bf": 167, "tf": 13.2, "k": 25.4}
    },
    "TR 152 x 29.8": {
        "Peso": 29.8,
        "Area": 38,
        "d/tw": 20.2,
        "Eje_X-X": {"I": 599, "S": 48.4, "r": 3.98, "y": 2.75},
        "Eje_Y-Y": {"I": 916, "S": 90.3, "r": 4.92},
        "Constante de torsion": 19.8,
        "Dimensiones": {"d": 152, "tw": 7.5, "bf": 203, "tf": 13.1, "k": 31.8}
    },
    "TR 152 x 33.5": {
        "Peso": 33.5,
        "Area": 42.6,
        "d/tw": 18,
        "Eje_X-X": {"I": 691, "S": 55.5, "r": 4.02, "y": 2.87},
        "Eje_Y-Y": {"I": 1041, "S": 101.8, "r": 4.93},
        "Constante de torsion": 27.9,
        "Dimensiones": {"d": 155, "tw": 8.3, "bf": 205, "tf": 16.3, "k": 35}
    },
    "TR 152 x 37.2": {
        "Peso": 37.2,
        "Area": 47.4,
        "d/tw": 16.5,
        "Eje_X-X": {"I": 778, "S": 62.1, "r": 4.05, "y": 2.96},
        "Eje_Y-Y": {"I": 1174, "S": 114.2, "r": 4.97},
        "Constante de torsion": 37.4,
        "Dimensiones": {"d": 155, "tw": 9.4, "bf": 205, "tf": 16.3, "k": 35}
    },
    "TR 152 x 39.4": {
        "Peso": 39.4,
        "Area": 50.2,
        "d/tw": 17.5,
        "Eje_X-X": {"I": 737, "S": 58, "r": 3.83, "y": 2.6},
        "Eje_Y-Y": {"I": 1994, "S": 157, "r": 6.29},
        "Constante de torsion": 33.4,
        "Dimensiones": {"d": 153, "tw": 8.8, "bf": 254, "tf": 14.6, "k": 31.8}
    },
    "TR 152 x 43.1": {
        "Peso": 43.1,
        "Area": 55,
        "d/tw": 17,
        "Eje_X-X": {"I": 795, "S": 61.7, "r": 3.79, "y": 2.62},
        "Eje_Y-Y": {"I": 2227, "S": 175.3, "r": 6.36},
        "Constante de torsion": 44.1,
        "Dimensiones": {"d": 155, "tw": 9.1, "bf": 254, "tf": 16.3, "k": 35}
    }
}


# Convertimos el diccionario de perfiles a una lista para facilitar su manejo
lista_perfiles = []
for nombre, datos in perfiles.items():
    perfil = {
        "nombre": nombre,
        "Peso": datos["Peso"],
        "Area": datos["Area"],  # Área en cm²
        "d_t": datos["d/tw"],
        "Ix": datos["Eje_X-X"]["I"],   # cm^4
        "Sx": datos["Eje_X-X"]["S"],   # cm^3
        "rx": datos["Eje_X-X"]["r"],   # cm
        "Iy": datos["Eje_Y-Y"]["I"],   # cm^4
        "Sy": datos["Eje_Y-Y"]["S"],   # cm^3
        "ry": datos["Eje_Y-Y"]["r"],   # cm
        "J": datos["Constante de torsion"],  # cm^4
        "d": datos["Dimensiones"]["d"],      # mm
        "tw": datos["Dimensiones"]["tw"],    # mm
        "bf": datos["Dimensiones"]["bf"],    # mm
        "tf": datos["Dimensiones"]["tf"],    # mm
        "k": datos["Dimensiones"]["k"],      # mm,
    }
    lista_perfiles.append(perfil)

# Factores de reducción
Fr1 = 0.9   # Factor de reducción para la barra
Fr2 = 0.75  # Factor de reducción para el tornillo

# Función para realizar cálculos a tensión


def realizar_calculos_tension(carga, perfil):
    resultados = []

    # Iteramos sobre los materiales disponibles
    for norma, data in materials.items():
        grados = data.get("Grados", {})
        for grado, propiedades_material in grados.items():
            # Verificar si propiedades_material contiene 'F_y' y 'F_u'
            if "F_y" in propiedades_material and "F_u" in propiedades_material:
                fy = propiedades_material["F_y"]  # MPa
                fu = propiedades_material["F_u"]  # MPa
                grado_material = grado
            else:
                # Si 'propiedades_material' es un diccionario anidado, iteramos sobre él
                for subgrado, sub_propiedades in propiedades_material.items():
                    if "F_y" in sub_propiedades and "F_u" in sub_propiedades:
                        fy = sub_propiedades["F_y"]  # MPa
                        fu = sub_propiedades["F_u"]  # MPa
                        grado_material = f"{grado} {subgrado}"
                    else:
                        continue

            # Parámetros del acero
            factor_reduccion_barra = Fr1

            # Calcular U usando directamente los valores de 'perfil'
            d = perfil["d"]  # mm
            bf = perfil["bf"]  # mm
            if bf >= (2/3) * d:
                U = 0.90
            else:
                U = 0.85

            # Datos de la barra
            area_bruta = perfil["Area"] * 100  # mm²
            espesor = perfil["tf"]  # mm

            carga_N = carga * 1000  # Convertir carga a N

            # Cálculo del área requerida de la barra a tensión (Ag requerido)
            area_barra_requerida = carga_N / \
                (factor_reduccion_barra * fy)  # mm²

            # Verificación del área bruta de la barra propuesta
            cumple_area_bruta = area_bruta >= area_barra_requerida

            if not cumple_area_bruta:
                continue  # Si el área bruta no es suficiente, pasamos al siguiente material

            # Cálculo del área neta (sin considerar agujeros aún)
            # mm² (asumiendo que los agujeros se diseñarán después)
            area_neta = area_bruta

            # Cálculo de TR1
            Pn = factor_reduccion_barra * fu * area_neta  # N
            relacion_tr1 = carga_N / Pn

            # Cálculo de TR2 (asumiendo área neta efectiva igual al 90% de área bruta)
            area_efectiva = U * area_neta  # mm²
            tr2 = factor_reduccion_barra * fu * area_efectiva  # N
            relacion_tr2 = carga_N / tr2

            # Cálculo de TR3 y TR4 (asumiendo valores aproximados)
            tr3 = 0.75 * ((0.6 * fu * area_neta) + (fy * area_neta))  # N
            tr4 = 0.75 * ((0.6 * fu * area_bruta) + (fy * area_bruta))  # N

            relacion_tr3 = carga_N / tr3
            relacion_tr4 = carga_N / tr4

            # Verificación de todas las relaciones (deben ser <= 1)
            cumple_TRs = all([
                relacion_tr1 <= 1,
                relacion_tr2 <= 1,
                relacion_tr3 <= 1,
                relacion_tr4 <= 1
            ])

            if cumple_TRs:
                resultados.append({
                    "perfil": perfil,
                    "norma_material": norma,
                    "grado_material": grado_material,
                    "fy": fy,
                    "fu": fu,
                    "TRs": {
                        "TR1": relacion_tr1,
                        "TR2": relacion_tr2,
                        "TR3": relacion_tr3,
                        "TR4": relacion_tr4
                    }
                })

    return resultados

# Función para realizar cálculos a compresión


def realizar_calculos_compresion(carga, perfil, longitud_no_soportada=3000):
    resultados = []

    # Iteramos sobre los materiales disponibles
    for norma, data in materials.items():
        grados = data.get("Grados", {})
        for grado, propiedades_material in grados.items():
            # Verificar si propiedades_material contiene 'F_y' y 'F_u'
            if "F_y" in propiedades_material and "F_u" in propiedades_material:
                fy = propiedades_material["F_y"]  # MPa
                fu = propiedades_material["F_u"]  # MPa
                grado_material = grado
            else:
                # Si 'propiedades_material' es un diccionario anidado, iteramos sobre él
                for subgrado, sub_propiedades in propiedades_material.items():
                    if "F_y" in sub_propiedades and "F_u" in sub_propiedades:
                        fy = sub_propiedades["F_y"]  # MPa
                        fu = sub_propiedades["F_u"]  # MPa
                        grado_material = f"{grado} {subgrado}"
                    else:
                        continue

            # Parámetros del acero
            factor_reduccion_barra = Fr1

            # Datos de la barra
            area_bruta = perfil["Area"] * 100  # mm²
            espesor = perfil["tf"]  # mm

            carga_N = carga * 1000  # Convertir carga a N

            # Cálculo del área requerida de la barra a compresión (Ag requerido)
            area_barra_requerida = carga_N / \
                (factor_reduccion_barra * fy)  # mm²

            # Verificación del área bruta de la barra propuesta
            cumple_area_bruta = area_bruta >= area_barra_requerida

            if not cumple_area_bruta:
                continue  # Si el área bruta no es suficiente, pasamos al siguiente material

            # Cálculo de la resistencia a compresión (CR)
            E = 200000  # MPa
            K = 1.0   # todas las conexiones son articuladas
            L = longitud_no_soportada  # mm
            ry_mm = perfil["ry"] * 10  # Convertimos de cm a mm
            Ag = area_bruta  # mm²
            n = 1.4  # Coeficiente adimensional
            FR = factor_reduccion_barra  # Factor de reducción

            # Cálculo de la esbeltez (KL/r)
            esbeltez = (K * L) / ry_mm

            # Esfuerzo crítico de Euler (Fe)
            Fe = (math.pi ** 2 * E) / (esbeltez ** 2)

            # Parámetro de esbeltez (λc)
            lambda_c = math.sqrt(fy / Fe)

            # Factor de reducción por esbeltez (χ)
            chi = 1 / ((1 + lambda_c ** n) ** (1 / n))

            # Resistencia a compresión (CR)
            CR = FR * chi * fy * Ag  # En N

            # Relación de la carga aplicada con la resistencia a compresión
            relacion_cr = carga_N / CR

            # Verificación de que la resistencia es suficiente
            if relacion_cr <= 1.0:
                resultados.append({
                    "perfil": perfil,
                    "norma_material": norma,
                    "grado_material": grado_material,
                    "fy": fy,
                    "fu": fu,
                    "Compresion": {
                        "Esbeltez (KL/r)": esbeltez,
                        "Esfuerzo crítico de Euler (Fe)": Fe,
                        "Parámetro de esbeltez (λc)": lambda_c,
                        "Factor de reducción por esbeltez (χ)": chi,
                        "Resistencia a compresión (CR)": CR,
                        "Relación carga/CR": relacion_cr
                    }
                })

    return resultados

# Función para seleccionar el elemento más óptimo


def seleccionar_elemento(carga, tipo_carga, lista_perfiles, longitud_no_soportada=3000):
    elementos_adecuados = []

    for perfil in lista_perfiles:
        if tipo_carga == "Tensión":
            resultados = realizar_calculos_tension(carga, perfil)
        elif tipo_carga == "Compresión":
            resultados = realizar_calculos_compresion(
                carga, perfil, longitud_no_soportada)
        else:
            continue  # Tipo de carga no válido

        for res in resultados:
            # Intentar diseñar las conexiones
            elemento_con_conexiones = diseñar_conexiones(
                res, carga, tipo_carga, longitud_no_soportada)
            if "nota" not in elemento_con_conexiones and "nota_soldadura" not in elemento_con_conexiones:
                elementos_adecuados.append(elemento_con_conexiones)

    # Verificar si hay elementos adecuados
    if elementos_adecuados:
        if tipo_carga == "Tensión":
            # Ordenar según el TR1 más cercano a 1 sin excederlo
            elementos_adecuados = [
                v for v in elementos_adecuados if "TRs" in v and "TR1" in v["TRs"]]
            if elementos_adecuados:
                elementos_adecuados.sort(
                    key=lambda v: abs(1 - v["TRs"]["TR1"]))
            else:
                return None  # No hay elementos con TRs válidos
        elif tipo_carga == "Compresión":
            # Ordenar según la relación carga/CR más cercana a 1 sin excederlo
            elementos_adecuados.sort(key=lambda v: abs(
                1 - v["Compresion"]["Relación carga/CR"]))
        elemento_mas_adecuado = elementos_adecuados[0]
        return elemento_mas_adecuado
    else:
        return None  # No hay elementos adecuados


# Función para diseñar las conexiones


def diseñar_conexiones(elemento, carga, tipo_carga, longitud_no_soportada=3000):
    elemento = diseñar_conexion_tornillos(
        elemento, carga, tipo_carga, longitud_no_soportada)
    elemento = diseñar_conexion_soldadura(elemento, carga, tipo_carga)
    return elemento


def diseñar_conexion_tornillos(elemento, carga, tipo_carga, longitud_no_soportada=3000):
    perfil = elemento["perfil"]
    fy = elemento["fy"]
    fu = elemento["fu"]

    # Datos del perfil
    area_bruta = perfil["Area"] * 100  # mm² (convertimos de cm² a mm²)
    espesor = perfil["tf"]  # mm
    U = 0.90  # Factor U según la sección (puedes ajustarlo si es necesario)

    carga_N = carga * 1000  # Convertir carga a N

    # Parámetros del perfil
    d = perfil["d"]  # mm (altura del perfil)
    bf = perfil["bf"]  # mm (ancho de la placa o ala)

    # Verificar si la resistencia a compresión (CR) está disponible en elemento
    if tipo_carga == "Compresión":
        if "Compresion" in elemento and "Resistencia a compresión (CR)" in elemento["Compresion"]:
            CR = elemento["Compresion"]["Resistencia a compresión (CR)"]  # N
        else:
            elemento["nota"] = "Falta la resistencia a compresión en el elemento."
            return elemento  # No podemos continuar sin CR

    # Lista para almacenar todas las opciones viables
    opciones_viables = []

    # Iteramos sobre los tipos de tornillos disponibles
    for tipo_tornillo, propiedades in tornillos.items():
        if tipo_tornillo == "Factores":
            continue  # Saltamos el diccionario de factores

        # Resistencia al corte del tornillo
        Fv = propiedades["Cortante"]["Con_cuerda_excluida"]["MPa"]  # MPa
        Fr_tornillo = Fr2  # Factor de reducción para tornillos

        # Iteramos sobre los diámetros disponibles
        for d_tor in diametros_tornillos:
            # Cálculo del área del tornillo (Ator)
            area_tornillo = math.pi * (d_tor ** 2) / 4  # mm²

            # Resistencia nominal al corte por tornillo
            Rn_tornillo = Fv * area_tornillo  # N

            # Resistencia de diseño al corte por tornillo
            Rn_tornillo_diseño = Fr_tornillo * Rn_tornillo  # N

            # Cálculo del número de tornillos necesarios
            n_tornillos_necesarios = carga_N / Rn_tornillo_diseño
            numero_tornillos = math.ceil(n_tornillos_necesarios)

            # Aseguramos que el número de tornillos es al menos 1
            if numero_tornillos < 1:
                numero_tornillos = 1

            # Asumimos un número máximo de tornillos por fila (máximo 4)
            max_tornillos_por_fila = min(numero_tornillos, 4)

            # Permitir desde 1 tornillo por fila
            for tornillos_por_fila in range(1, max_tornillos_por_fila + 1):
                filas_de_tornillos = math.ceil(
                    numero_tornillos / tornillos_por_fila)
                numero_tornillos_total = tornillos_por_fila * filas_de_tornillos

                # Calcular el diámetro del agujero
                dH = d_tor + 3  # mm (diámetro del agujero)

                # Separaciones y distancias al borde mínimas y máximas
                s_min = 2.67 * d_tor  # mm
                e_min = 1.5 * d_tor  # mm
                s_max = min(14 * espesor, 200)  # mm
                e_max = min(12 * espesor, 150)  # mm

                # Generar posibles valores de s y e
                s_values = [s_min + i *
                            5 for i in range(int((s_max - s_min) // 5) + 1)]
                e_values = [e_min + i *
                            5 for i in range(int((e_max - e_min) // 5) + 1)]

                # Iterar sobre combinaciones de s y e
                for s in s_values:
                    for e in e_values:
                        # Calcular dimensiones del grupo de tornillos
                        # Largo en dirección de las filas
                        Largo_agv = e + (filas_de_tornillos - 1) * s + e
                        # Ancho en dirección de los tornillos por fila
                        Ancho_agt = e + (tornillos_por_fila - 1) * s + e

                        # Verificar que el arreglo de tornillos cabe en el perfil
                        if Largo_agv > d or Ancho_agt > bf:
                            continue  # No cabe, probar con otra combinación

                        if tipo_carga == "Tensión":
                            # Cálculos del plano de cortante
                            Agv = Largo_agv * espesor  # mm²
                            Anv = (Largo_agv - filas_de_tornillos *
                                   dH) * espesor  # mm²

                            # Cálculos del plano de tensión
                            Agt = Ancho_agt * espesor  # mm²
                            Ant = (Ancho_agt - tornillos_por_fila *
                                   dH) * espesor  # mm²

                            # Verificación de áreas críticas
                            if Anv <= 0 or Ant <= 0:
                                continue  # No es viable esta combinación

                            # Cálculo del área neta de la barra (An)
                            area_neta = area_bruta - numero_tornillos_total * dH * espesor  # mm²

                            # Verificación de área neta
                            if area_neta <= 0:
                                continue  # No es viable esta combinación

                            # Cálculo del área efectiva de la barra (Ae)
                            area_efectiva = U * area_neta  # mm²

                            # Verificación de área efectiva
                            if area_efectiva <= 0:
                                continue  # No es viable esta combinación

                            # Cálculo de TR2
                            tr2 = Fr1 * fu * area_efectiva  # N
                            relacion_tr2 = carga_N / tr2

                            if relacion_tr2 > 1.0:
                                continue  # No cumple, pasamos a la siguiente combinación

                            # Cálculo de Pn y relacion_tr1
                            Pn = Fr1 * fu * area_neta  # N
                            relacion_tr1 = carga_N / Pn

                            # Cálculo de TR3 y TR4
                            tr3 = 0.75 * ((0.6 * fu * Anv) + (fy * Ant))  # N
                            tr4 = 0.75 * ((0.6 * fu * Agv) + (fy * Agt))  # N

                            relacion_tr3 = carga_N / tr3
                            relacion_tr4 = carga_N / tr4

                            # Revisiones de tornillos
                            # TorR1: Cortante en tornillos
                            TorR1_resistencia = Rn_tornillo_diseño * numero_tornillos_total  # N
                            relacion_TorR1 = carga_N / TorR1_resistencia

                            # TorR2: Aplastamiento
                            Ab = numero_tornillos_total * dH * espesor  # mm²
                            TorR2_resistencia = 0.75 * (2.4 * fu) * Ab  # N
                            relacion_TorR2 = carga_N / TorR2_resistencia

                            # TorR3: Desgarramiento
                            A_tor = 2 * (e - 0.5 * dH) * espesor  # mm²
                            if A_tor <= 0:
                                continue  # No es viable
                            TorR3_resistencia = 0.75 * (1.2 * fu) * A_tor  # N
                            relacion_TorR3 = carga_N / TorR3_resistencia

                            # Verificación de todas las relaciones (deben ser <= 1.0)
                            cumple_TRs = all([
                                relacion_tr1 <= 1.0,
                                relacion_tr2 <= 1.0,
                                relacion_tr3 <= 1.0,
                                relacion_tr4 <= 1.0,
                                relacion_TorR1 <= 1.0,
                                relacion_TorR2 <= 1.0,
                                relacion_TorR3 <= 1.0
                            ])

                            if cumple_TRs:
                                # Guardamos la opción viable
                                opcion_viable = {
                                    "tipo_tornillo": tipo_tornillo,
                                    "diametro_tornillo": d_tor,
                                    "numero_tornillos": numero_tornillos_total,
                                    "filas_de_tornillos": filas_de_tornillos,
                                    "tornillos_por_fila": tornillos_por_fila,
                                    "distancia_al_borde": e,
                                    "distancia_entre_tornillos": s,
                                    "TRs": {
                                        "TR1": relacion_tr1,
                                        "TR2": relacion_tr2,
                                        "TR3": relacion_tr3,
                                        "TR4": relacion_tr4,
                                        "TorR1": relacion_TorR1,
                                        "TorR2": relacion_TorR2,
                                        "TorR3": relacion_TorR3
                                    }
                                }
                                opciones_viables.append(opcion_viable)

                        elif tipo_carga == "Compresión":
                            # Revisiones de tornillos
                            # TorR1: Cortante en tornillos
                            TorR1_resistencia = Rn_tornillo_diseño * numero_tornillos_total  # N
                            relacion_TorR1 = carga_N / TorR1_resistencia

                            # TorR2: Aplastamiento
                            Ab = numero_tornillos_total * dH * espesor  # mm²
                            TorR2_resistencia = 0.75 * (2.4 * fu) * Ab  # N
                            relacion_TorR2 = carga_N / TorR2_resistencia

                            # TorR3: Desgarramiento (si aplica)
                            A_tor = 2 * (e - 0.5 * dH) * espesor  # mm²
                            if A_tor <= 0:
                                continue  # No es viable
                            TorR3_resistencia = 0.75 * (1.2 * fu) * A_tor  # N
                            relacion_TorR3 = carga_N / TorR3_resistencia

                            # Verificación de todas las relaciones (deben ser <= 1.0)
                            cumple_TRs = all([
                                relacion_TorR1 <= 1.0,
                                relacion_TorR2 <= 1.0,
                                relacion_TorR3 <= 1.0
                            ])

                            if cumple_TRs:
                                # Guardamos la opción viable
                                opcion_viable = {
                                    "tipo_tornillo": tipo_tornillo,
                                    "diametro_tornillo": d_tor,
                                    "numero_tornillos": numero_tornillos_total,
                                    "filas_de_tornillos": filas_de_tornillos,
                                    "tornillos_por_fila": tornillos_por_fila,
                                    "distancia_al_borde": e,
                                    "distancia_entre_tornillos": s,
                                    "TRs": {
                                        "TorR1": relacion_TorR1,
                                        "TorR2": relacion_TorR2,
                                        "TorR3": relacion_TorR3
                                    }
                                }
                                opciones_viables.append(opcion_viable)

    if opciones_viables:
        # Seleccionar la opción con TR1 más cercana a 0.99 sin exceder 1.0
        if tipo_carga == "Tensión":
            opciones_viables.sort(key=lambda v: abs(0.99 - v["TRs"]["TR1"]))
        elif tipo_carga == "Compresión":
            opciones_viables.sort(key=lambda v: max(v["TRs"].values()))
        mejor_opcion = opciones_viables[0]
        elemento.update(mejor_opcion)
    else:
        elemento["nota"] = "No se encontró una combinación de tornillos que cumpla"

    return elemento


# Función para diseñar la conexión de soldadura
def diseñar_conexion_soldadura(elemento, carga, tipo_carga):
    perfil = elemento["perfil"]
    fy = elemento["fy"]
    fu = elemento["fu"]

    # Datos del perfil
    espesor = perfil["tf"]  # mm

    carga_N = carga * 1000  # Convertir carga a N

    # Variables relacionadas con la soldadura
    tplaca = espesor  # Espesor de la placa (mm)

    # Tamaño máximo de filete
    if tplaca <= 6:
        tamano_maximo = tplaca  # El tamaño máximo es igual al espesor de la placa
    else:
        tamano_maximo = tplaca - 2  # El tamaño máximo es el espesor menos 2 mm

    a_min = 3  # Tamaño mínimo práctico del filete (mm)
    a_max = tamano_maximo  # Tamaño máximo de la pierna del filete (mm)

    # Ajustamos a_min si a_max es menor
    if a_max < a_min:
        a_min = a_max  # El tamaño mínimo no puede ser mayor que el máximo

    mejor_soldadura = None

    for electrodo, propiedades_soldadura in soldaduras.items():
        fu_sold = propiedades_soldadura["Fu"]["MPa"]  # MPa

        # Generamos los posibles tamaños de 'a' en múltiplos de 1 mm dentro del rango permitido
        a_values = [a for a in range(int(a_min), int(a_max) + 1)]
        for a in a_values:
            # Longitudes de filete
            longitud_minima = 4 * a  # Longitud mínima de la soldadura
            longitud_maxima = 100 * a  # Longitud máxima de la soldadura

            # Resistencia nominal de la soldadura por unidad de longitud
            Rn_weld = 0.75 * 0.6 * fu_sold * a  # N/mm

            # Calcular longitud requerida
            L_required = carga_N / Rn_weld  # mm

            # Asegurar que L_required está entre longitud mínima y máxima
            L_actual = max(L_required, longitud_minima)
            L_actual = min(L_actual, longitud_maxima)

            # Factor de reducción beta
            beta = min(1.2 - 0.002 * (L_actual / a), 1.0)

            # Recalcular Rn_weld con beta
            Rn_weld_beta = beta * Rn_weld  # N/mm

            # Resistencia total de la soldadura
            resistencia_total_soldadura = Rn_weld_beta * L_actual  # N

            # Relación de eficiencia de la soldadura
            sold_tr = carga_N / resistencia_total_soldadura

            # Verificar que sold_tr no exceda 1.0
            if sold_tr <= 1.0:
                # Buscamos sold_tr más cercano a 0.99 sin exceder 1.0
                if (mejor_soldadura is None) or (abs(0.99 - sold_tr) < abs(0.99 - mejor_soldadura["sold_tr"])):
                    mejor_soldadura = {
                        "electrodo": electrodo,
                        "fu_sold": fu_sold,
                        "a": a,
                        "L_ideal": L_required,
                        # Redondeamos al múltiplo de 10 mm superior
                        "L_redondeado": math.ceil(L_actual / 10) * 10,
                        "sold_tr": sold_tr,
                        "beta": beta
                    }

            # Si sold_tr es exactamente 0.99, podemos terminar la búsqueda
            if mejor_soldadura and mejor_soldadura["sold_tr"] == 0.99:
                break

        # Si ya encontramos una soldadura con sold_tr igual a 0.99, salimos del loop de electrodos
        if mejor_soldadura and mejor_soldadura["sold_tr"] == 0.99:
            break

    if mejor_soldadura:
        elemento["mejor_soldadura"] = mejor_soldadura
    else:
        elemento["nota_soldadura"] = "No se encontró una combinación de soldadura que cumpla"

    return elemento

# Función para imprimir los resultados


def imprimir_resultados(carga, tipo_carga, elemento):
    print(f"""
    -----------------------------------------------
                   RESULTADOS DE CÁLCULO
    -----------------------------------------------
    Tipo de carga:                         {tipo_carga}
    Carga aplicada:                        {carga:.2f} kN
    """)
    if elemento:
        perfil = elemento["perfil"]
        print("Perfil más adecuado que pasa todas las verificaciones:")
        print(f"- {perfil['nombre']} con área {perfil['Area']} cm²")
        print(f"Peso del perfil: {perfil['Peso']} kg/m")
        print(f"Material utilizado:")
        print(f"- Norma: {elemento['norma_material']}")
        print(f"- Grado: {elemento['grado_material']}")
        print(f"- F_y: {elemento['fy']} MPa")
        print(f"- F_u: {elemento['fu']} MPa")

        if tipo_carga == "Tensión":
            TRs = elemento["TRs"]
            print("\nRelaciones de las TRs:")
            print(
                f"TR1 (Carga aplicada / Resistencia nominal): {TRs['TR1']:.3f}")
            print(f"TR2 (Carga aplicada / TR2): {TRs['TR2']:.3f}")
            print(f"TR3 (Carga aplicada / TR3): {TRs['TR3']:.3f}")
            print(f"TR4 (Carga aplicada / TR4): {TRs['TR4']:.3f}")
        elif tipo_carga == "Compresión" and "Compresion" in elemento:
            comp = elemento["Compresion"]
            print("\nResultados de compresión:")
            print(f"Esbeltez (KL/r): {comp['Esbeltez (KL/r)']:.2f}")
            print(
                f"Esfuerzo crítico de Euler (Fe): {comp['Esfuerzo crítico de Euler (Fe)']:.2f} MPa")
            print(
                f"Parámetro de esbeltez (λc): {comp['Parámetro de esbeltez (λc)']:.4f}")
            print(
                f"Factor de reducción por esbeltez (χ): {comp['Factor de reducción por esbeltez (χ)']:.4f}")
            print(
                f"Resistencia a compresión (CR): {comp['Resistencia a compresión (CR)'] / 1000:.2f} kN")
            print(f"Relación carga/CR: {comp['Relación carga/CR']:.3f}")

        conexion_realizada = False

        if "tipo_tornillo" in elemento:
            conexion_realizada = True
            print("\nMejor combinación de tornillos:")
            print(f"- Tipo de tornillo: {elemento['tipo_tornillo']}")
            print(
                f"- Diámetro del tornillo: {elemento['diametro_tornillo']} mm")
            print(
                f"- Número total de tornillos: {elemento['numero_tornillos']}")
            print(
                f"- Disposición: {elemento['filas_de_tornillos']} filas de {elemento['tornillos_por_fila']} tornillos")
            print(
                f"- Distancia al borde (e): {elemento['distancia_al_borde']:.1f} mm")
            print(
                f"- Separación entre tornillos (s): {elemento['distancia_entre_tornillos']:.1f} mm")

            if "TRs" in elemento:
                TRs = elemento["TRs"]
                if tipo_carga == "Tensión":
                    print("\nRelaciones de las TRs:")
                    print(
                        f"TR1 (Carga aplicada / Resistencia nominal): {TRs['TR1']:.3f}")
                    print(f"TR2 (Carga aplicada / TR2): {TRs['TR2']:.3f}")
                    print(f"TR3 (Carga aplicada / TR3): {TRs['TR3']:.3f}")
                    print(f"TR4 (Carga aplicada / TR4): {TRs['TR4']:.3f}")

                print("\nRelaciones de las TorRs:")
                print(
                    f"TorR1 (Carga aplicada / Resistencia al cortante de tornillos): {TRs['TorR1']:.3f}")
                print(
                    f"TorR2 (Carga aplicada / Resistencia al aplastamiento): {TRs['TorR2']:.3f}")
                if "TorR3" in TRs:
                    print(
                        f"TorR3 (Carga aplicada / Resistencia al desgarramiento): {TRs['TorR3']:.3f}")
            else:
                print("\nNo se encontraron las relaciones de las TRs y TorRs.")

        if "nota" in elemento:
            print(f"\nNota: {elemento['nota']}")

        if "mejor_soldadura" in elemento:
            conexion_realizada = True
            ms = elemento["mejor_soldadura"]
            print("\nMejor opción de soldadura:")
            print(f"- Electrodo: {ms['electrodo']}")
            print(f"- Tamaño de la garganta (a): {ms['a']:.1f} mm")
            print(f"- Longitud ideal de soldadura: {ms['L_ideal']:.2f} mm")
            print(
                f"- Longitud de soldadura redondeada: {ms['L_redondeado']} mm")
            print(f"- sold_tr (relación soldadura): {ms['sold_tr']:.3f}")
        if "nota_soldadura" in elemento:
            print(f"\nNota sobre soldadura: {elemento['nota_soldadura']}")

        if not conexion_realizada:
            print(
                "\nNo se encontró una conexión válida (tornillos o soldadura) para este perfil.")
    else:
        print("No se encontró un perfil adecuado que pase todas las verificaciones para esta carga.")

    print("-----------------------------------------------\n")


# Función para procesar las cargas
def procesar_cargas(cargas, tipo_carga="Tensión", longitud_no_soportada=3000):
    print(
        f"\n********** PROCESAMIENTO DE CARGAS A {tipo_carga.upper()} **********\n")
    for i, carga in enumerate(cargas, 1):
        print(f"**** Carga {i}: {carga} kN ****")
        elemento_adecuado = seleccionar_elemento(
            carga, tipo_carga, lista_perfiles, longitud_no_soportada)
        if elemento_adecuado:
            elemento_adecuado = diseñar_conexiones(
                elemento_adecuado, carga, tipo_carga, longitud_no_soportada)
        imprimir_resultados(carga, tipo_carga, elemento_adecuado)


# Listas de cargas proporcionadas
cargas_compresion = [632]
cargas_tension = [632]

# Longitud no soportada para miembros a compresión (en mm)
longitud_no_soportada = 3000  # Ajusta este valor según tus condiciones

# Procesar cargas a compresión
procesar_cargas(cargas_compresion, tipo_carga="Compresión",
                longitud_no_soportada=longitud_no_soportada)

# Procesar cargas a tensión
procesar_cargas(cargas_tension, tipo_carga="Tensión")

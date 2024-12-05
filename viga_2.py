def calcular_peso_propio(peralte, peso):
    # Calcula el peso propio de la viga en kN/m
    return peso * 9.81 / 1000


def calcular_carga_disenio(peso_propio, carga_muerta, carga_viva):
    # Calcula la carga de diseño combinando las cargas con sus factores correspondientes
    return 1.5 * (carga_muerta + peso_propio) + 1.7 * carga_viva


def calcular_resistencia_flexion(FR, Fy, Sx):
    # Calcula el momento resistente elástico y lo convierte a kN·m
    MR_flexion_elastico = FR * Fy * Sx
    return MR_flexion_elastico / 1e6  # Convertir de N·mm a kN·m


def calcular_relacion_flexion(Md, MR_flexion_elastico):
    # Calcula la relación entre el momento de diseño y el momento resistente
    return Md / MR_flexion_elastico


def calcular_resistencia_cortante(FR, Fy, T, tw, Cv):
    # Calcula la resistencia a cortante y la convierte a kN
    Aa = T * tw  # Área del alma en mm²
    VR = FR * 0.6 * Fy * Aa * Cv  # Resistencia a cortante en N
    return VR / 1e3  # Convertir de N a kN


def calcular_reacciones(carga_muerta, carga_viva, longitud):
    # Calcula las reacciones en los apoyos para cargas distribuidas
    Rap = (carga_muerta * longitud) / 2
    Rav = (carga_viva * longitud) / 2
    return Rap, Rav, Rap + Rav


def calcular_reacciones_puntual(Fa):
    # Calcula las reacciones en los apoyos para una carga puntual centrada
    return Fa / 2, Fa / 2


def calcular_flecha_maxima_distribuida(carga_muerta, carga_viva, q_o, longitud, E, I):
    # Convertir I de cm⁴ a mm⁴
    I = I * 1e4  # cm⁴ a mm⁴
    # Carga total en kN/m es numéricamente igual a N/mm
    q_total_N_mm = carga_muerta + carga_viva + q_o  # N/mm
    # Convertir longitud de m a mm
    L_mm = longitud * 1e3  # mm
    # Calcular flecha máxima
    return (5 * q_total_N_mm * L_mm**4) / (384 * E * I)  # Resultado en mm


def calcular_flecha_maxima_central_puntual(Fa, L, E, I):
    # Convertir I de cm⁴ a mm⁴
    I = I * 1e4  # cm⁴ a mm⁴
    # Convertir Fa de kN a N
    Fa_N = Fa * 1e3  # N
    # Convertir longitud de m a mm
    L_mm = L * 1e3  # mm
    # Calcular flecha máxima
    return (Fa_N * L_mm**3) / (48 * E * I)  # Resultado en mm


def mostrar_resultados(peralte, peso, S, IR, q_o, qd, longitud, Md, MR_flexion_elastico, relacion_flexion,
                       tw, T, VR, Vd, relacion_cortante, Rap, Rav, R, flecha_maxima_distribuida,
                       flecha_maxima_puntual, flecha_total, flecha_maxima_permitida_l400, flecha_maxima_permitida_6mm,
                       cumple_flecha, carga_muerta, carga_viva, FR, Fy, Cv, E, Ix, Fa, a):
    # Mostrar los resultados en un formato organizado
    print("="*60)
    print(f"{'CÁLCULOS PARA LA VIGA:':^60}")
    print(f"{IR:^60}")
    print("="*60)

    # Variables de Entrada
    print(f"{'VARIABLES DE ENTRADA':^60}")
    print(f"{'Peralte:':<40} {peralte} mm")
    print(f"{'Peso:':<40} {peso} kg/m")
    print(f"{'Módulo de sección (S):':<40} {S} cm³")
    print(f"{'Espesor del alma (tw):':<40} {tw} mm")
    print(f"{'Altura del alma (T):':<40} {T} mm")
    print(f"{'Carga muerta:':<40} {carga_muerta} kN/m")
    print(f"{'Carga viva:':<40} {carga_viva} kN/m")
    print(f"{'Longitud de la viga (L):':<40} {longitud} m")
    print(f"{'Factor de resistencia (FR):':<40} {FR}")
    print(f"{'Esfuerzo de fluencia (Fy):':<40} {Fy} MPa")
    print(f"{'Coeficiente de cortante (Cv):':<40} {Cv}")
    print(f"{'Módulo de elasticidad (E):':<40} {E} MPa")
    print(f"{'Momento de inercia (Ix):':<40} {Ix} cm⁴")
    print(f"{'Carga puntual (Fa):':<40} {Fa} kN")
    print(f"{'Distancia hasta la carga puntual (a):':<40} {a} m")
    print("="*60)

    # Resultados de Flexión
    print(f"{'RESULTADOS DE FLEXIÓN':^60}")
    print(f"{'Momento de diseño total (Md):':<40} {Md:.2f} kN·m")
    print(f"{'Momento resistente elástico (MR):':<40} {MR_flexion_elastico:.2f} kN·m")
    print(f"{'Relación Md/MR (flexión):':<40} {relacion_flexion:.3f}")
    if relacion_flexion <= 1:
        print(f"{'FLEXIÓN:':<40} CUMPLE")
    else:
        print(f"{'FLEXIÓN:':<40} NO CUMPLE")
    print("-"*60)

    # Resultados de Cortante
    print(f"{'RESULTADOS DE CORTANTE':^60}")
    print(f"{'Cortante de diseño total (Vd):':<40} {Vd:.2f} kN")
    print(f"{'Resistencia a cortante (VR):':<40} {VR:.2f} kN")
    print(f"{'Relación Vd/VR (cortante):':<40} {relacion_cortante:.3f}")
    if Vd <= VR:
        print(f"{'CORTANTE:':<40} CUMPLE")
    else:
        print(f"{'CORTANTE:':<40} NO CUMPLE")
    print("-"*60)

    # Resultados de Reacciones
    print(f"{'RESULTADOS DE REACCIONES':^60}")
    print(f"{'Reacción por carga muerta (Rap):':<40} {Rap:.2f} kN")
    print(f"{'Reacción por carga viva (Rav):':<40} {Rav:.2f} kN")
    print(f"{'Reacción total (R):':<40} {R:.2f} kN")
    if Fa > 0:
        print(f"{'Reacción por carga puntual (Ra):':<40} {Fa/2:.2f} kN")
    print("-"*60)

    # Peso de la Viga
    print(f"{'PESO DE LA VIGA':^60}")
    peso_viga = q_o * longitud
    print(f"{'Peso propio de la viga:':<40} {peso_viga:.2f} kN")
    print("-"*60)

    # Resultados de Flecha
    print(f"{'RESULTADOS DE FLECHA':^60}")
    print(f"{'Flecha máxima por carga distribuida:':<40} {flecha_maxima_distribuida:.2f} mm")
    print(f"{'Flecha máxima por carga puntual:':<40} {flecha_maxima_puntual:.2f} mm")
    print(f"{'Flecha total:':<40} {flecha_total:.2f} mm")
    print(f"{'Flecha máxima permitida (L/180):':<40} {flecha_maxima_permitida_l400:.2f} mm")
    print(
        f"{'Flecha máxima permitida (L/240:':<40} {flecha_maxima_permitida_6mm:.2f} mm")
    if cumple_flecha:
        print(f"{'FLECHA:':<40} CUMPLE")
    else:
        print(f"{'FLECHA:':<40} NO CUMPLE")
    print("="*60)
    print("\n")


def calcular_viga(peralte, peso, S, tw, T, carga_muerta, carga_viva, longitud, FR, Fy, Cv, E, Ix, IR, Fa, a):
    # Calcular el peso propio
    q_o = calcular_peso_propio(peralte, peso)

    # Calcular la carga de diseño (carga distribuida)
    qd = calcular_carga_disenio(q_o, carga_muerta, carga_viva)

    # Calcular momentos debido a la carga distribuida
    Md_uniforme = (qd * longitud**2) / 8  # Momento debido a carga distribuida

    # Calcular momentos debido a la carga puntual en el centro
    # Momento máximo para carga puntual
    Md_puntual = (Fa * (longitud - a) * a) / longitud if Fa > 0 else 0

    # Momento de diseño total
    Md = Md_uniforme + Md_puntual

    # Calcular resistencia a flexión
    Sx = S * 1e3  # Convertir módulo de sección a mm³
    MR_flexion_elastico = calcular_resistencia_flexion(FR, Fy, Sx)

    # Verificar flexión
    relacion_flexion = calcular_relacion_flexion(Md, MR_flexion_elastico)

    # Calcular cortantes debido a la carga distribuida
    Vd_uniforme = (qd * longitud) / 2  # Cortante debido a carga distribuida

    # Calcular cortantes debido a la carga puntual
    Vd_puntual = Fa / 2 if Fa > 0 else 0  # Cortante máximo debido a carga puntual

    # Cortante de diseño total
    Vd = Vd_uniforme + Vd_puntual

    # Calcular resistencia a cortante
    VR = calcular_resistencia_cortante(FR, Fy, T, tw, Cv)

    # Calcular relación de cortante
    relacion_cortante = Vd / VR

    # Calcular reacciones para cargas distribuidas
    Rap, Rav, R = calcular_reacciones(carga_muerta + q_o, carga_viva, longitud)

    # Calcular flecha máxima para carga distribuida
    flecha_maxima_distribuida = calcular_flecha_maxima_distribuida(
        carga_muerta, carga_viva, q_o, longitud, E, Ix)

    # Calcular flecha máxima para carga puntual en el centro
    flecha_maxima_puntual = calcular_flecha_maxima_central_puntual(
        Fa, longitud, E, Ix) if Fa > 0 else 0

    # Flecha total
    flecha_total = flecha_maxima_distribuida + flecha_maxima_puntual

    # Criterios de flecha máxima permitida
    # Convertir longitud a mm y dividir entre 400
    flecha_maxima_permitida_l180 = (longitud * 1e3) / 180
    flecha_maxima_permitida_l240 = (
        longitud * 1e3) / 240  # Flecha máxima de 6 mm
    cumple_flecha = flecha_total <= min(
        flecha_maxima_permitida_l180, flecha_maxima_permitida_l240)

    # Mostrar los resultados
    mostrar_resultados(
        peralte, peso, S, IR, q_o, qd, longitud, Md, MR_flexion_elastico, relacion_flexion,
        tw, T, VR, Vd, relacion_cortante, Rap, Rav, R, flecha_maxima_distribuida,
        flecha_maxima_puntual, flecha_total, flecha_maxima_permitida_l180, flecha_maxima_permitida_l240,
        cumple_flecha, carga_muerta, carga_viva, FR, Fy, Cv, E, Ix, Fa, a
    )


# Datos de la viga secundaria
datos_viga_secundaria = {
    'peralte': 254,
    'peso': 58.2,
    'S': 690,
    'tw': 8,
    'T': 195,
    'carga_muerta': 28.35,
    'carga_viva': 3.5,
    'longitud': 5,
    'FR': 0.90,
    'Fy': 250,
    'Cv': 1.0,
    'E': 210000,  # MPa
    'Ix': 8699,   # cm⁴
    'IR': "IR 58.2 x 254",
    'Fa': 0,
    'a': 0
}

# Calcular el peso propio de la viga secundaria
q_o_secundaria = calcular_peso_propio(
    datos_viga_secundaria['peralte'], datos_viga_secundaria['peso'])

# Calcular reacciones de la viga secundaria
Rap_secundaria, Rav_secundaria, R_secundaria = calcular_reacciones(
    datos_viga_secundaria['carga_muerta'] + q_o_secundaria,
    datos_viga_secundaria['carga_viva'],
    datos_viga_secundaria['longitud']
)
Fa_viga_principal = R_secundaria  # Carga puntual aplicada a la viga principal

# Datos de la viga principal
datos_viga_principal = {
    'peralte': 254,
    'peso': 44.8,
    'S': 531,
    'tw': 7.6,
    'T': 218,
    'carga_muerta': 0,   # No hay carga muerta adicional
    'carga_viva': 0,     # No hay carga viva adicional
    'longitud': 5,      # Longitud de la viga principal
    'FR': 0.90,
    'Fy': 250,
    'Cv': 1.0,
    'E': 210000,         # MPa
    'Ix': 7076,         # cm⁴ 
    'IR': "IR 254 x 44.8",
    'Fa': Fa_viga_principal,  # Carga puntual de la viga secundaria
    'a': 2.5  # Carga puntual aplicada en el centro
}

# Ejecutar los cálculos
calcular_viga(**datos_viga_secundaria)
calcular_viga(**datos_viga_principal)

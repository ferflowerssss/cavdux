import streamlit as st

# Título de la aplicación
st.title('Modelo de Inversión Flexible en Cavdux')

# Entrada de cantidad de inversión
investment = st.number_input('Cantidad de Inversión ($)', min_value=0, value=100000, step=5000)

# Entrada de porcentajes para los cuatro ejes
st.sidebar.header('Distribución de Inversión (%)')
family_percentage = st.sidebar.slider('Familia (Mapa)', min_value=0, max_value=100, value=25)
teachers_percentage = st.sidebar.slider('Maestros (Veriedu)', min_value=0, max_value=100, value=25)
youth_percentage = st.sidebar.slider('Jóvenes (Dux)', min_value=0, max_value=100, value=25)
directors_percentage = st.sidebar.slider('Directores (ADEM)', min_value=0, max_value=100, value=25)

# Asegurarse de que los porcentajes sumen 100
total_percentage = family_percentage + teachers_percentage + youth_percentage + directors_percentage

if total_percentage != 100:
    st.sidebar.warning('La suma de los porcentajes debe ser 100%. Actualmente es: {}%'.format(total_percentage))

# Barra deslizadora para nivel de calidad de formación
quality_level = st.select_slider(
    'Nivel de Calidad de Formación',
    options=[0, 25, 50, 75, 100],
    value=50,
    help='Izquierda: Priorizar Alcance, Derecha: Priorizar Calidad'
)

# Función para calcular el número de personas formadas
def calculate_people_formed(investment, quality_level, base_cost):
    # El costo efectivo por persona disminuye con el aumento del alcance (menor calidad)
    cost_per_person = base_cost * (1 + (100 - quality_level) / 100)
    return investment // cost_per_person

# Función para obtener descripción del programa según el nivel de calidad
def get_program_description(quality_level):
    if quality_level == 0:
        return "Programas: Webinars en línea, acceso a recursos digitales."
    elif quality_level == 25:
        return "Programas: Cursos en línea, talleres virtuales interactivos."
    elif quality_level == 50:
        return "Programas: Talleres presenciales, sesiones de mentoría."
    elif quality_level == 75:
        return "Programas: Programas de certificación, cursos especializados presenciales."
    elif quality_level == 100:
        return "Programas: Maestrías presenciales, programas avanzados de liderazgo."

# Cálculo de la distribución de la inversión y número de personas formadas
if total_percentage == 100:
    family_investment = investment * (family_percentage / 100)
    teachers_investment = investment * (teachers_percentage / 100)
    youth_investment = investment * (youth_percentage / 100)
    directors_investment = investment * (directors_percentage / 100)

    # Base cost per person for each category
    base_cost_family = 100
    base_cost_teachers = 200
    base_cost_youth = 150
    base_cost_directors = 250

    family_formed = calculate_people_formed(family_investment, quality_level, base_cost_family)
    teachers_formed = calculate_people_formed(teachers_investment, quality_level, base_cost_teachers)
    youth_formed = calculate_people_formed(youth_investment, quality_level, base_cost_youth)
    directors_formed = calculate_people_formed(directors_investment, quality_level, base_cost_directors)

    # Mostrar distribución de inversión en dólares
    st.write('### Distribución de la Inversión en Dólares')
    st.write(f'**Familia (Mapa):** ${family_investment:,.2f}')
    st.write(f'**Maestros (Veriedu):** ${teachers_investment:,.2f}')
    st.write(f'**Jóvenes (Dux):** ${youth_investment:,.2f}')
    st.write(f'**Directores (ADEM):** ${directors_investment:,.2f}')

    # Mostrar número de personas formadas y programas
    st.write('### Número de Personas Formadas')
    st.write(f'**Familia (Mapa):** {family_formed} personas')
    st.write(f'**Maestros (Veriedu):** {teachers_formed} personas')
    st.write(f'**Jóvenes (Dux):** {youth_formed} personas')
    st.write(f'**Directores (ADEM):** {directors_formed} personas')

    st.write('### Descripción de los Programas')
    st.write(get_program_description(quality_level))

    # Mostrar el total de personas formadas
    total_formed = family_formed + teachers_formed + youth_formed + directors_formed
    st.write(f'## Total de Personas Formadas: {total_formed} personas')

else:
    st.write('Por favor, asegúrese de que la suma de los porcentajes de inversión sea 100%.')

# Información adicional o llamada a la acción
st.write('## ¿Interesado en invertir?')
st.write('Contacte a Cavdux para más información sobre cómo puede contribuir y el impacto de su inversión.')







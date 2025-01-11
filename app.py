import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open("models/diabetes_precict_model.sav", "rb"))
heart_disease_model = pickle.load(open("models/heart_disease_model.sav", "rb"))
parkinson_model = pickle.load(open("models/parkinsons_detector_model.sav", "rb"))

with st.sidebar:
    
    selected = option_menu("Multiple Disease Prediction System",
                            ["Диабет",
                            "Сердечно-сосудистые заболевания",
                            "Болезнь Паркинсона"],
                            icons=["activity", "heart", "person"],
                            default_index=0)


if (selected == "Диабет"):
    
    st.title("Выявление Диабета с помощью ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Количество беременностей")
    
    with col2:
        Glucose = st.text_input("Количество глюкозы в крови")
    
    with col3:
        BloodPressure = st.text_input("Давление")
    
    with col1:
        SkinThickness = st.text_input("Значение толщины кожи")
    
    with col2:
        Insulin = st.text_input("Уровень инсулина")
    
    with col3:
        BMI = st.text_input("Индекс массы тела")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Уровень родословной диабета')
    
    with col2:
        Age = st.text_input("Возраст пациента")
    
    diagnos = ""
    
    if st.button("Показать Результат"):
        
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, 
                        Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        user_input = [float(x) for x in user_input]
        diagnos = diabetes_model.predict([user_input])
        
        if diagnos[0] == 1:
            diagnos = "У пациента есть Диабет"
        else:
            diagnos = "У пациента отсутствует Диабет"
    
    st.success(diagnos)


if (selected == "Сердечно-сосудистые заболевания"):
    
    st.title("Выявление ССЗ с помощью ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Возраст")
    
    with col2:
        sex = st.text_input("Пол")
    
    with col3:
        cp = st.text_input("Вид боли в груди")
    
    with col1:
        pressure = st.text_input("Среднее артериальное давление")
    
    with col2:
        chol = st.text_input("Уровень Холестерола")
    
    with col3:
        blood_sugar = st.text_input("Уровень сахара")
    
    with col1:
        ecg = st.text_input("ЭКГ")
    
    with col2:
        max_ch = st.text_input("Максимальная частота сердцебиения")
    
    with col3:
        stenokardia = st.text_input("Стенокардия")
    
    with col1:
        st_depression = st.text_input("Депрессия ST")
    
    with col2:
        st_naklon = st.text_input("Наклон сегмента ST")
    
    with col3:
        os_of = st.text_input("Основные сосуды, окрашенные флюорографией")
    
    with col1:
        defect_level = st.text_input("0 = нормальный; 1 = фиксированный дефект; 2 = обратимый дефект")
    
    diagnos = ""
    
    if st.button("Показать Результат"):
        
        user_input = [age, sex, cp, pressure, chol, blood_sugar, ecg, max_ch, stenokardia,
                        st_depression, st_naklon, os_of, defect_level]
        
        user_input = [float(x) for x in user_input]
        diagnos = heart_disease_model.predict([user_input])
        
        if diagnos[0] == 1:
            diagnos = "У пациента есть ССЗ"
        else:
            diagnos = "У пациента отсутствует ССЗ"
    
    st.success(diagnos)



if (selected == "Болезнь Паркинсона"):
    
    st.title("Выявление Б.Паркинсона с помощью ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    
    with col5:
        Jitter_abs = st.text_input("MDVP:Jitter(Adv)")
    
    with col1:
        RAP = st.text_input("MDVP:RAP")
    
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
    
    with col3:
        DDP = st.text_input("Jitter:DDP")
    
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
    
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
    
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
    
    with col3:
        APQ = st.text_input("MDVP:APQ")
    
    with col4:
        DDA = st.text_input("Shimmer:DDA")
    
    with col5:
        NHR = st.text_input("NHR")
    
    with col1:
        HNR = st.text_input("HNR")
    
    with col2:
        RPDE = st.text_input("RPDE")
    
    with col3:
        DFA = st.text_input("DFA")
    
    with col4:
        spread1 = st.text_input("spread1")
    
    with col5:
        spread2 = st.text_input("spread2")
    
    with col1:
        D2 = st.text_input("D2")
    
    with col2:
        PPE = st.text_input("PPE")
    
    diagnos = ""
    
    if st.button("Показать Результат"):
        
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_abs, RAP, PPQ,
                        DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR,
                        HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        
        user_input = [float(x) for x in user_input]
        diagnos = parkinson_model.predict([user_input])
        
        if diagnos[0] == 1:
            diagnos = "У пациента есть Б. Паркинсона"
        else:
            diagnos = "У пациента отсутствует Б. Паркинсона"
    
    st.success(diagnos)
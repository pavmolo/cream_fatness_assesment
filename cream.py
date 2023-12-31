import streamlit as st

def cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass):
  milk_share_mass = (1.15 * cream_target_mass * creamfat_target - cream_fatness * cream_target_mass) / (1.15 * (milk_fatness - cream_fatness))
  cream_share_mass = (cream_target_mass - milk_share_mass * 1.15) / 1.15
  sugar_share_mass = (milk_share_mass + cream_share_mass) * 0.15
  return [cream_share_mass, milk_share_mass, sugar_share_mass]
def condenced_milk(cream_fatness, milk_fatness, creamfat_target, cream_target_mass):
  cream_share_mass = ((cream_target_mass * (creamfat_target - milk_fatness)) + ((0.3 / 1.3) * cream_target_mass * (1 - milk_fatness))) / (cream_fatness - milk_fatness)
  milk_share_mass = cream_target_mass - cream_share_mass - (0.3 / 1.3) * cream_target_mass
  condenced_milk_share_mass = (milk_share_mass + cream_share_mass) * 0.3
  return [cream_share_mass, milk_share_mass, condenced_milk_share_mass]
st.markdown('''<a href="http://kaizen-consult.ru/"><img src='https://www.kaizen.com/images/kaizen_logo.png' style="width: 50%; margin-left: 25%; margin-right: 25%; text-align: center;"></a><p>''', unsafe_allow_html=True)
st.markdown('''<h1>Приложение для опеределния жирности сливок</h1>''', unsafe_allow_html=True)
st.markdown('''<h2>Введите данные:</h2>''', unsafe_allow_html=True)

cream_fatness = st.slider("Исходное значение жирности сливок, %", 35, 54, 48, 1)
milk_fatness = st.slider("Жирность молока, которым разбавляют сливки, %", 0.0, 5.0, 3.2, 0.2)
creamfat_target = st.slider("Целевое значение жирности сливок, %", 35, 54, 45, 1)
cream_target_mass = st.number_input(f"Сколько сливок целевой жирности нужно получить, кг", value=200)
sugar_mode = st.radio("Укажите, какой способ добавления слабости вы используете", ('Сахар', 'Сгущенка (8%)'))
if sugar_mode == 'Сахар':
  cream_output = cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass)
  if cream_output[1] > 0:
    st.markdown('''<h2> </h2>''', unsafe_allow_html=True)
    st.markdown('''<h2>Результаты расчетов:</h2>''', unsafe_allow_html=True)
    st.metric("Сколько лить сливок", f'{round(cream_output[0], 2)} КГ')
    st.metric("Сколько лить молока", f'{round(cream_output[1], 2)} КГ')
    st.metric("Сколько сыпать сахара", f'{round(cream_output[2], 2)} КГ')
  else:
    st.header(f'Если вы добавите к сливкам {cream_fatness}% жирности сахар в размере 150 г на 1 кг сливок, то получите сироп жирностью {round(cream_fatness/ 1.15, 2)}%, что ниже целевой жирности {creamfat_target}%')
else:
    cream_output_cm = condenced_milk(cream_fatness, milk_fatness, creamfat_target, cream_target_mass)
    st.markdown('''<h2> </h2>''', unsafe_allow_html=True)
    st.markdown('''<h2>Результаты расчетов:</h2>''', unsafe_allow_html=True)
    st.metric("Сколько лить сливок", f'{round(cream_output_cm[0], 2)} КГ')
    st.metric("Сколько лить молока", f'{round(cream_output_cm[1], 2)} КГ')
    st.metric("Сколько лить сгущенки", f'{round(cream_output_cm[2], 2)} КГ')




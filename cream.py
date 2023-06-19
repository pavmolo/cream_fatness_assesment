import streamlit as st

def cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass):
  coeff = (creamfat_target - milk_fatness) / (cream_fatness - creamfat_target)
  cream_share_mass = cream_target_mass * (coeff / (1 + coeff))
  milk_share_mass = cream_target_mass / coeff
  return [coeff, cream_share_mass, milk_share_mass]
st.markdown('''<a href="http://kaizen-consult.ru/"><img src='https://www.kaizen.com/images/kaizen_logo.png' style="width: 50%; margin-left: 25%; margin-right: 25%; text-align: center;"></a><p>''', unsafe_allow_html=True)
st.markdown('''<h1>Приложение для опеределния жирности сливок</h1>''', unsafe_allow_html=True)
cream_fatness = st.slider("Исходное значение жирности сливок, %", 35, 54, 48, 1)
milk_fatness = st.slider(f"Жирность молока, которым разбавляют сливки, %", 0.0, 5.0, 3.2, 0.2)
creamfat_target = st.slider(f"Целевое значение жирности сливок, %", 35, 54, 45, 1)
cream_target_mass = st.number_input(f"Сколько сливок целевой жирности нужно получить, кг", value=200)

cream_output = cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass)

st.metric("Коэффициент пропорции (сливки/молоко)", f'{round(cream_output[0], 2)}')
st.metric("Сколько сливок лить для разбавления", f'{round(cream_output[1], 2)} КГ')
st.metric("Сколько молока нужно лить для разбавления", f'{round(cream_output[2], 2)} КГ')

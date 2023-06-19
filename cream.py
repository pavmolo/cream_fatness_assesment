import streamlit as st

def cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass):
  coeff = (creamfat_target - milk_fatness) / (cream_fatness - creamfat_target)
  cream_share_mass = cream_target_mass * (coeff / (1 + coeff))
  milk_share_mass = cream_target_mass / coeff
  return [coeff, cream_share_mass, milk_share_mass]

cream_fatness = st.slider("Исходное значение жирности сливок", 35, 54, 45, 1)
milk_fatness = st.slider(f"Жирность молока, которым разбавляют сливки", 0, 5, 3.2, 0.2)
creamfat_target = st.slider(f"Целевое значение жирности сливок", 35, 54, 45, 1)
cream_target_mass = st.number_input(f"Сколько сливок целевой жирности нужно получить, кг", value=200)

cream_output = cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass)

col1, col2, col3 = st.columns(3)
col1.metric("Коэффициент пропорции (сливки/молоко)", cream_output[0], "")
col2.metric("Сколько сливок лить для разбавления", cream_output[1], "кг")
col3.metric("Сколько молока нужно лить для разбавления", cream_output[2], "кг")

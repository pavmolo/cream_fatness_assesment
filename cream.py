import streamlit as st

def cream(cream_fatness, milk_fatness, creamfat_target, cream_target_mass):
  coeff = (creamfat_target - milk_fatness) / (cream_fatness - creamfat_target)
  cream_share_mass = cream_target_mass * (coeff / (1 + coeff))
  milk_share_mass = cream_target_mass / coeff
  return [coeff, cream_share_mass, milk_share_mass]


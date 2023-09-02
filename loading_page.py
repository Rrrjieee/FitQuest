import os
import streamlit as st
import config as cfg

from scripts.css_recipe import CSSRecipe
from scripts.page_activity_data import PageActivityData

css_recipe          = CSSRecipe("static/loading_page.png")

st.set_page_config(
    page_title  = cfg.loading_screen.page_title,
    page_icon   = cfg.loading_screen.page_icon,
    layout      = cfg.loading_screen.page_layout,
)

st.markdown(
    str(css_recipe),
    unsafe_allow_html=True,
)

st.button(
    label       ="Submit",
    type        ="primary",
    on_click    = lambda: st.write("U smell like cow farts."),
)

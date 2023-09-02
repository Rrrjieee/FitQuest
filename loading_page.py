import os
import image_loader as image
import streamlit as stream
import config as cfg

from page_activity_data import PageActivityData

manual_style        = """
<style>
body {
    background-image: url("data:image/png;base64,app/static/loading_page.png");
    background-size: cover;
}
</style>
"""

stream.set_page_config(
    page_title  = cfg.loading_screen.page_title,
    page_icon   = cfg.loading_screen.page_icon,
    layout      = cfg.loading_screen.page_layout,
)

stream.markdown(
    manual_style,
    unsafe_allow_html=True,
)

# with stream.container():
#     stream.write("---")
#     stream.write("hax")
#     stream.write("##")
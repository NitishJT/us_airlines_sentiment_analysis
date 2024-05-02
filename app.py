import streamlit as st
from st_pages import Page, show_pages, add_page_title
import pandas as pd

# Optional -- adds the title and icon to the current page
add_page_title('SENTIMENT ANALYSIS')

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        # Page("pages/main.py", "DASHBOARD"),
        Page("pages/page1.py", "US AIRLINES"),
        Page("pages/page2.py", "CUSTOMERS COMPLAINTS"),
    ]
)

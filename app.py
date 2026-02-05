import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import streamlit as st

st.title("📊 Stock Table Generator")

csv_data = """
Date,Company,Daily_Change,Volume
2025-01-01,Apple,5,1200000
2025-01-02,Google,2,950000
2025-01-03,Microsoft,5,1100000
"""

df = pd.read_csv(StringIO(csv_data))

fig, ax = plt.subplots(figsize=(6, 2))
ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc="center",
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

st.pyplot(fig)

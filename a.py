import streamlit as st
import os

# Set the title of the app
st.title("Theory Assignments")

# Embed the PDF file in the app
pdf_file = "cn.pdf"
st.markdown(f'<iframe src="https://docs.google.com/viewer?url=https://your_domain.com/path_to_pdf/{pdf_file}&embedded=true" width="700" height="900"></iframe>', unsafe_allow_html=True)

# Provide a download button for the PDF
with open(pdf_file, "rb") as file:
    pdf_data = file.read()

st.download_button(
    label="Download PDF",
    data=pdf_data,
    file_name=pdf_file,
    mime="application/pdf",
)

# List and provide download links for .pkt files in the img folder
st.header("Topology Files")

img_folder = "img"
pkt_files = [f for f in os.listdir(img_folder) if f.endswith('.pkt')]

for pkt_file in pkt_files:
    pkt_path = os.path.join(img_folder, pkt_file)
    with open(pkt_path, "rb") as file:
        pkt_data = file.read()
    
    st.download_button(
        label=f"Download {pkt_file}",
        data=pkt_data,
        file_name=pkt_file,
        mime="application/octet-stream",
    )
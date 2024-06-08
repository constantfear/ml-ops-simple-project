import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

import streamlit as st

# interact with FastAPI endpoint
backend = "http://0.0.0.0:8000/"


def process(input_file, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", input_file, "file/csv")})

    r = requests.post(
        server_url,
        data=m,
        headers={"Content-Type": m.content_type},
        timeout=8000
    )

    return r


# construct UI layout
st.title("Simple ML-Ops project")


input_file = st.file_uploader("insert csv file")  # image upload widget

file_name = False

if st.button("Get predictions"):
    if input_file:
        r = process(input_file, f"{backend}/upload")
        if r.status_code == 200:
            data = r.json()
            file_name = data['filename']

            response = requests.get(f"{backend}/download/{file_name}")
            if response.status_code == 200:
                st.success(f"Prediction successfully saved in '{file_name}'")
                st.download_button(
                    label="Download file",
                    data=response.content,
                    file_name=file_name,
                    mime="text/csv",
                )
            else:
                st.error("File not found")

        print(file_name)
    else:
        # handle case with no image
        st.write("Insert csv file!")

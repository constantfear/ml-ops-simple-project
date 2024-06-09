import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
import streamlit as st
import io
import base64
from src.functions import draw_hist, download_link

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


def hist_plot(preds):
    plot_fig = draw_hist(preds)
    st.pyplot(plot_fig)
    fn = 'hist.png'
    # Преобразуем график в байтовые данные
    image_data = io.BytesIO()
    plot_fig.savefig(image_data, format='png')
    image_data.seek(0)

    # Кодируем байтовые данные в base64
    b64 = base64.b64encode(image_data.read()).decode()

    link = download_link(
        b64, fn,
        "data:image/png;base64",
        "Click here to download PNG"
    )
    st.markdown(link, unsafe_allow_html=True)


def preds_(file_name):
    response = requests.get(f"{backend}/download/{file_name}")
    if response.status_code == 200:
        st.success(f"Prediction successfully saved in '{file_name}'")
        b64 = base64.b64encode(response.content).decode()
        link = download_link(
            b64, file_name,
            "data:file/csv;base64",
            "Click here to download CSV"
        )
        st.markdown(link, unsafe_allow_html=True)
    else:
        st.error("File not found")


st.title("Simple ML-Ops project")

# Вывод важных признаков
features_response = requests.get(f"{backend}//feature_importances/5")
if features_response.status_code == 200:
    data = features_response.json()
    st.header("Top 5 Feature Importances")
    for i in data['features'].items():
        st.write(f"- {i[0]} - {i[1]}")
    js = json.dumps(data['features'], ensure_ascii=False).encode('utf8')
    b64 = base64.b64encode(js).decode('utf8')
    link = download_link(
        b64, 'Top 5 Feature Importances.json',
        "data:application/json;base64",
        "Click here to download JSON"
    )
    st.markdown(link, unsafe_allow_html=True)

st.header("Get predictions on your file")
input_file = st.file_uploader("Insert CSV file")  # image upload widget


if st.button("Get predictions"):
    if input_file:
        r = process(input_file, f"{backend}/upload")
        if r.status_code == 200:
            st.header("Your Predictions")
            data = r.json()
            file_name = data['filename']
            hist_plot(data['predictions'])
            preds_(file_name)
    else:
        # handle case with no image
        st.write("Insert csv file!")

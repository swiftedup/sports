import os
from tempfile import NamedTemporaryFile
from uuid import uuid4
import streamlit as st

from examples.soccer.main import main, Mode

st.title("Sports Video Analyzer")

uploaded = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
mode_option = st.selectbox("Select analysis mode", [m.value for m in Mode])
device_option = st.selectbox("Select device", ["cpu", "cuda"], index=0)

if uploaded is not None and st.button("Run analysis"):
    with NamedTemporaryFile(delete=False, suffix=".mp4") as src:
        src.write(uploaded.read())
        source_path = src.name

    os.makedirs("outputs", exist_ok=True)
    target_path = os.path.join("outputs", f"{uuid4()}.mp4")

    main(
        source_video_path=source_path,
        target_video_path=target_path,
        device=device_option,
        mode=Mode(mode_option)
    )

    st.success("Processing finished!")
    st.video(target_path)

import streamlit as st
from transformers import pipeline
from PIL import Image

# ---------------------------
# App Config
# ---------------------------
st.set_page_config(
    page_title="Rugged Plus — Skin Type Detector",
    page_icon="🧴",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------
# Custom Styling (Luxury Black Theme)
# ---------------------------
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
    }

    .title {
        font-size: 4rem;
        font-weight: 900;
        text-align: center;
        color: white;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        color: #cccccc;
        margin-bottom: 40px;
        font-weight: 300;
    }

    .result {
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        color: #ffffff;
        background: #111;
        padding: 20px;
        border-radius: 12px;
        margin-top: 30px;
        border: 1px solid #333;
    }

    h3 {
        color: white !important;
    }

    .stSuccess, .stInfo {
        background-color: #111 !important;
        border: 1px solid #333 !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 500;
    }

    .stButton>button {
        background: #ffffff;
        color: #000000;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0px 4px 15px rgba(255,255,255,0.2);
    }

    .stButton>button:hover {
        background: #e0e0e0;
        transform: scale(1.05);
        transition: all 0.3s ease-in-out;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Title & Intro
# ---------------------------
st.markdown("<h1 class='title'>Rugged Plus</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Men's Skincare — Personalized for Your Skin</p>", unsafe_allow_html=True)

st.write("📸 Upload your selfie below and let Rugged Plus detect your skin type instantly.")

# ---------------------------
# File Upload
# ---------------------------
uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Load ResNet model
    model_name = "microsoft/resnet-50"
    classifier = pipeline("image-classification", model=model_name)

    # Run classifier
    results = classifier(image)
    top_label = results[0]["label"].lower()

    # Mapping logic (fixed swap from earlier)
    if "dog" in top_label or "cat" in top_label:
        skin_type = "Dry"
    elif "person" in top_label or "face" in top_label:
        skin_type = "Oily"
    else:
        skin_type = "Normal"

    # ---------------------------
    # Display Result
    # ---------------------------
    st.markdown(f"<div class='result'>Detected Skin Type: {skin_type}</div>", unsafe_allow_html=True)

    # ---------------------------
    # Product Recommendations
    # ---------------------------
    st.markdown("<h3 style='margin-top:30px;'>Recommended Products 💡</h3>", unsafe_allow_html=True)

    if skin_type == "Oily":
        st.success("**Face Wash:** Rugged Plus – ClearForce (Acne Control Face Wash)")
        st.success("**Moisturizer:** Rugged Plus – MatteShield (Oil Control Moisturizer)")

    elif skin_type == "Dry":
        st.success("**Face Wash:** Rugged Plus – HydraFuel (Hydrating Face Wash)")
        st.success("**Moisturizer:** Rugged Plus – HydraCore (Deep Hydration Moisturizer)")

    else:  # Normal
        st.info("**Moisturizer:** Rugged Plus – SkinSync (Daily Balance Moisturizer)")

# ---------------------------
# Footer
# ---------------------------
st.markdown(
    """
    <hr style="border:1px solid #333; margin-top:40px;">
    <div style="text-align:center; color:#666; font-size:14px; margin-top:20px;">
        © 2025 <b>Rugged Plus</b> · Elevating Men's Skincare
    </div>
    """,
    unsafe_allow_html=True
)

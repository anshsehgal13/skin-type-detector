import streamlit as st
from transformers import AutoImageProcessor, AutoModelForImageClassification
from transformers import pipeline
from PIL import Image

st.title("Skin Type Detector — Demo (Oily vs Dry)")

uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Load a safe pre-trained ResNet-50 model from Hugging Face
    model_name = "microsoft/resnet-50"
    classifier = pipeline("image-classification", model=model_name)

    # Run classifier
    results = classifier(image)

    # Just for demo: pick one class from model and map to skin type
    top_label = results[0]["label"].lower()

    # Simple fake logic to map ResNet labels → skin type
    if "dog" in top_label or "cat" in top_label:
        skin_type = "Oily"
    elif "person" in top_label or "face" in top_label:
        skin_type = "Dry"
    else:
        skin_type = "Normal"

    st.write(f"**Detected skin type (demo):** {skin_type}")

    # Product recommendation
    if skin_type == "Oily":
        st.success("Suggested: Use **Oil-Control Serum** from your brand.")
    elif skin_type == "Dry":
        st.success("Suggested: Use **Hydrating Cream** from your brand.")
    else:
        st.info("Suggested: Use **Balanced Moisturizer** from your brand.")

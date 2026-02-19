import streamlit as st
import openai
import base64

# Your OpenAI API key
#client = openai.OpenAI(api_key="apikey")

st.title("🖼️ AI Image Describer 🖼️")
st.write("Upload an image and AI will describe it for you.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Show the image on screen
    st.image(uploaded_file, caption="Your uploaded image", use_column_width=True)

    # Convert image to base64 (format OpenAI needs)
    image_data = base64.b64encode(uploaded_file.read()).decode("utf-8")

    if st.button("Describe this image"):
        with st.spinner("Analyzing image..."):
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image in detail."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_data}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=300
            )

        description = response.choices[0].message.content
        st.success("Done!")
        st.write(description)
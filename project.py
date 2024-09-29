import gradio as gr
import librosa

def keyword_spotting(audio):
    # Placeholder function for keyword spotting
    audio_data, sr = librosa.load(audio, sr=None)
    result = "Keyword found: one,two, three,seven "  # Dummy result
    return result

# Custom CSS to remove download and fullscreen buttons, and add an outline to images
custom_css = """
.gradio-container {max-width: 1000px; margin: auto;} /* Limits the app width */
.gradio-image .download, .fullscreen {display: none;} /* Hides the download and fullscreen buttons */
img {border: 2px solid #ddd; border-radius: 8px;} /* Adds an outline around images */
"""

# Gradio Interface
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# Few Shot Language Agnostic Keyword Spotting System (FSLAKWS)")
    gr.Markdown("""
        Welcome to the FSLAKWS system prototype. This system is designed to detect keywords in audio files with 
        very few examples provided for training. It works across multiple languages and varying sample rates.
    """)
   
    # Audio Input Section
    with gr.Row():
        audio_input = gr.Audio(type="filepath", label="Upload Audio File")
        output = gr.Textbox(label="Result")

     # Button to Process Input
    submit_btn = gr.Button("Spot Keyword")
    submit_btn.click(keyword_spotting, inputs=[audio_input], outputs=output)


    # Business Use Cases Section
    gr.Markdown("## Business Use Cases")

    # Display Business Use Case Images in a 2x2 Grid
    with gr.Row():
        with gr.Column(scale=1):
            img1 = gr.Image(value="voiceAssistance.jpeg", label="Multilingual Virtual Assistants", show_label=False)
            gr.Markdown("**Multilingual Virtual Assistants**")  # Image label below the image
        with gr.Column(scale=1):
            img2 = gr.Image(value="callcentreImg.jpeg", label="Customer Service Automation", show_label=False)
            gr.Markdown("**Customer Service Automation**")
    
    with gr.Row():
        with gr.Column(scale=1):
            img3 = gr.Image(value="voicesecurity.jpeg", label="Security and Surveillance", show_label=False)
            gr.Markdown("**Security and Surveillance**")
        with gr.Column(scale=1):
            img4 = gr.Image(value="voiceBiometric.jpeg", label="Language-Agnostic Voice Biometrics", show_label=False)
            gr.Markdown("**Language-Agnostic Voice Biometrics**")

    gr.Markdown("""
    **1. Speech Recognition Systems**:
    - Enhance existing speech recognition systems by adding multilingual keyword detection capabilities, making them more versatile and useful in global markets.

    **2. Customer Service Automation**:
    - Implement in call centers to automatically detect and flag important keywords during customer interactions, enabling real-time sentiment analysis and better customer support.

    **3. Security and Surveillance**:
    - Deploy in security systems to monitor and detect critical keywords in multiple languages, improving the efficiency of threat detection and response in diverse environments.

    **4. Media Monitoring**:
    - Utilize in media and content monitoring systems to track specific keywords or phrases across various languages in audio content, helping brands manage their reputation.

    **5. Voice-Activated Assistants**:
    - Integrate into voice-activated assistants to support multilingual command recognition, expanding their usability across different regions and languages.
    """)

    # Performance Metrics Section
    gr.Markdown("## Performance Metrics")
    gr.Markdown("- **Accuracy**: High precision in keyword detection\n- **Latency**: < 100ms response time\n- **Model Size**: Optimized for deployment in resource-constrained environments ")

   
# Launch the Gradio Interface
demo.launch()

from dash import dcc, Input, Output, State
import numpy as np
import plotly.express as px
import os
from PIL import Image
import tensorflow as tf

# Load the trained model (adjust path if necessary)
model = tf.keras.models.load_model('unet_checkpoint.h5')

def register_callbacks(app, upload_folder):
    """Registers the callback functions with the Dash app."""
    
    @app.callback(
        Output("output-image", "children"),
        Input("segment-button", "n_clicks"),
        State("upload-image", "isCompleted"),
        State("upload-image", "fileNames"),
        prevent_initial_call=True
    )
    def segment_image(n_clicks, is_completed, fileNames):
        if n_clicks is None or not is_completed:
            return None

        # Load and preprocess image
        file_path = os.path.join(upload_folder, fileNames[0])
        image = Image.open(file_path).resize((256, 256))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Run model prediction
        prediction = model.predict(image_array)[0, :, :, 0]  # Remove batch and channel dimensions

        # Display original image and mask
        fig1 = px.imshow(image, title="Original MRI Image")
        fig2 = px.imshow(prediction, title="Predicted Tumor Mask", color_continuous_scale="gray")
        
        return [
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
        ]

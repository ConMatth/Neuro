import dash
import dash_uploader as du
from layout import create_layout
from callbacks import register_callbacks

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "MRI Tumor Segmentation"

# Configure upload folder
UPLOAD_FOLDER = "uploads"
du.configure_upload(app, UPLOAD_FOLDER)

# Set up layout and register callbacks
app.layout = create_layout(app)
register_callbacks(app, UPLOAD_FOLDER)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)

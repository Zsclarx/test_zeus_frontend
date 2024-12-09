from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Define route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define route to trigger running the tool
import os
import zipfile
import shutil

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/run_tool', methods=['POST'])
def run_tool():
    try:
        # Get the uploaded files and user input
        input_file = request.files['inputFile']
        test_data_file = request.files.get('testDataFile')  # Optional field
        api_key = request.form['apiKey']
        llm_model = request.form['llmModel']

        # Save the input file to disk temporarily
        input_file_path = os.path.join(UPLOAD_FOLDER, input_file.filename)
        input_file.save(input_file_path)

        test_data_directory = None
        if test_data_file:
            # Save the ZIP file containing the test data
            zip_file_path = os.path.join(UPLOAD_FOLDER, test_data_file.filename)
            test_data_file.save(zip_file_path)

            # Extract the ZIP file to a directory
            test_data_directory = os.path.join(UPLOAD_FOLDER, 'test_data')
            if os.path.exists(test_data_directory):
                shutil.rmtree(test_data_directory)  # Remove existing directory if any
            os.makedirs(test_data_directory)

            # Extract the contents of the ZIP file
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(test_data_directory)

            # Clean up the zip file after extraction
            os.remove(zip_file_path)

        # Build the command to run
        command = [
            "testzeus-hercules",
            "--input-file", input_file_path, 
            "--output-path", "../project_base/output", 
            "--test-data-path", test_data_directory,
            "--llm-model", llm_model,
            "--llm-model-api-key", api_key
        ]

        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Return the result of the command execution
        if result.returncode == 0:
            return jsonify({'output': result.stdout})
        else:
            return jsonify({'error': result.stderr}), 500

    except Exception as e:
        return jsonify({'error': f"Exception: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)

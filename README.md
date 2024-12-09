# TestZeus Frontend Setup and Usage Guide

This repository contains the frontend for the **TestZeus** tool, which helps you run tests with OpenAI models. Follow the instructions below to set up and use the application.

## Environment Setup

1. Clone the frontend repository:
   ```bash
   git clone https://github.com/Zsclarx/test_zeus_frontend.git
2. Install dependencies and run the application:
    ```bash
    python app.py
This will start the Flask application locally.

## Steps to Use the App

### 1. Provide Input Files:
- **Test Feature File (`test.feature`)**: Upload your `test.feature` file in the first input field.
- **Test Data Directory**: Provide your `test_data` directory in `.zip` format. This will be used to run the test.

### 2. API Key and Model Selection:
- **Enter a valid OpenAI API key**.
- **Select Model**: Choose the model you'd like to use (e.g., GPT-4, GPT-3.5).

### 3. Run the Tool:
- Click the **Run Model** button to start processing.

### 4. Optional: Live Browser View:
- If you want to see the process in a live browser, set the environment variable `HEADLESS=false`.


## Additional Information

For complete setup instructions related to the **TestZeus Hercules** backend, visit the [TestZeus Hercules GitHub repository](https://github.com/test-zeus-ai/testzeus-hercules).




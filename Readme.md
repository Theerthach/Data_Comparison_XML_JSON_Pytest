This project is designed to compare XML data from an S3 bucket with JSON data obtained via an API call using pytest.

## Project Structure

- **/tests**: Contains all the test cases for the project.
- **/utils**: Contains utility functions for data fetching and comparison.
- **/config**: Configuration files for S3 and API settings.

## Setup

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Configure S3 and API**:
    - Update the `config/s3_config.json` with your S3 bucket details.
    - Update the `config/api_config.json` with your API endpoint and credentials.

## Usage

1. **Run Tests**:
    ```bash
    pytest
    ```

2. **Test Cases**:
    - **test_fetch_s3_data.py**: Tests for fetching XML data from S3.
    - **test_fetch_api_data.py**: Tests for fetching JSON data from the API.
    - **test_compare_data.py**: Tests for comparing the XML and JSON data.

## Utility Functions

- **fetch_s3_data(bucket_name, file_key)**: Fetches XML data from the specified S3 bucket and file key.
- **fetch_api_data(api_endpoint, params)**: Fetches JSON data from the specified API endpoint with given parameters.
- **compare_data(xml_data, json_data)**: Compares the XML data with JSON data and returns the result.

## Configuration Files

- **s3_config.json**:
    ```json
    {
        "bucket_name": "your-bucket-name",
        "file_key": "path/to/your/file.xml"
    }
    ```

- **api_config.json**:
    ```json
    {
        "api_endpoint": "https://api.yourservice.com/data",
        "params": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    ```

## Example

Here is an example of how to use the utility functions in your tests:


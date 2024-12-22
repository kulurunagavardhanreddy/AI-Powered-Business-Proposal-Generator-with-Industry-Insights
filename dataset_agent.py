# dataset_agent.py


import requests


def is_valid_link(url):
    try:
        # Check if the URL is a valid one by sending a GET request
        response = requests.get(url, timeout=10)
        
        # Handle specific HTTP response codes
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            print(f"Error: Unauthorized access to {url}. Please check your credentials.")
            return False
        elif response.status_code == 404:
            print(f"Error: Dataset not found at {url}. The URL might be incorrect or the dataset might not exist.")
            return False
        else:
            print(f"URL {url} returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred with URL: {url}, Error: {e}")
        return False

def fetch_datasets(industry):
    datasets = {
        'Retail': [
            "https://www.kaggle.com/datasets/retail/retail-sales",
            "https://huggingface.co/datasets/retail_analysis"
        ],
        'Automotive': [
            "https://www.kaggle.com/datasets/automotive/vehicle-data",
            "https://huggingface.co/datasets/automotive_predictions"
        ],
        'Healthcare': [
            "https://www.kaggle.com/datasets/healthcare/patient-data",
            "https://huggingface.co/datasets/healthcare/diagnostics"
        ],
        'Technology': [
            "https://www.kaggle.com/datasets/tech/tech-industry-data",  # Ensure this is valid
            "https://huggingface.co/datasets/tech-analysis"  # Ensure Hugging Face dataset exists and is public
        ],
        'Advertising': [
            "https://huggingface.co/datasets/advertising_campaign_data",  # Ensure valid dataset
            "https://huggingface.co/datasets/advertising_marketing"  # Ensure valid dataset
        ],
        'AI': [
            "https://huggingface.co/datasets/ai_research_papers",  # Ensure valid dataset
            "https://huggingface.co/datasets/ai_industry_trends"  # Ensure valid dataset
        ]
    }

    valid_datasets = []
    industry_datasets = datasets.get(industry, [])
    
    # Filter out invalid dataset links
    for dataset in industry_datasets:
        if is_valid_link(dataset):
            valid_datasets.append(dataset)
    
    if not valid_datasets:
        print(f"No valid datasets found for the {industry} industry.")
    
    return valid_datasets

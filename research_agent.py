# research_agent.py

import requests
from bs4 import BeautifulSoup

def fetch_company_info(company_name):
    """
    Fetch social media and relevant links for the company.
    """
    search_url = f"https://www.google.com/search?q={company_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [link['href'] for link in soup.find_all('a', href=True) if 'linkedin' in link['href'] or 'twitter' in link['href']]
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching company info: {e}")
        return []

def fetch_competitor_info(industry):
    """
    Fetch competitor links for a given industry.
    """
    search_url = f"https://www.google.com/search?q={industry} competitors"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    try:
        response = requests.get(search_url, headers=headers)
        response.raise_for_status()  # Ensure valid response
        soup = BeautifulSoup(response.text, 'html.parser')
        competitors = [link['href'] for link in soup.find_all('a', href=True) if 'competitor' in link['href']]
        return competitors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching competitor info: {e}")
        return []

def fetch_industry_details_from_wikipedia(industry):
    """
    Fetch industry details and use cases from Wikipedia.
    """
    try:
        summary = wikipedia.summary(industry, sentences=3)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error for industry '{industry}': {e.options}")
        return "No clear details found for the specified industry."
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for industry: {industry}")
        return "No details found for the specified industry."
    except Exception as e:
        print(f"Error fetching details from Wikipedia: {e}")
        return "Error occurred while fetching details."

def fetch_use_cases_for_unknown_company(company_name):
    """
    Handle unknown companies by guessing the industry and fetching use cases.
    """
    guessed_industries = ["Technology", "Retail", "Healthcare", "Automotive"]  # Default guesses
    industry_details = {}

    for industry in guessed_industries:
        details = fetch_industry_details_from_wikipedia(industry)
        industry_details[industry] = details

    return industry_details

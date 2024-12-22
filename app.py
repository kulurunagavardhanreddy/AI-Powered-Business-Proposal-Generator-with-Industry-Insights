# app.py

import streamlit as st
import pandas as pd
import json
import os
from research_agent import fetch_company_info, fetch_competitor_info
from use_case_agent import generate_use_cases
from dataset_agent import fetch_datasets, is_valid_link
from pipeline import generate_proposal

# Load company industry data from a file (JSON or CSV)
def load_company_data(filename="industries.json"):
    file_path = os.path.join(os.getcwd(), filename)
    
    try:
        if filename.endswith(".json"):
            with open(file_path, "r") as file:
                data = json.load(file)
                # Ensure the data is in the expected format (dictionary where keys are company names)
                if isinstance(data, dict) and all(isinstance(value, list) for value in data.values()):
                    return data
                else:
                    raise ValueError("JSON file content should be a dictionary where keys are company names and values are lists of industries.")
        elif filename.endswith(".csv"):
            df = pd.read_csv(file_path)
            return df.to_dict(orient="records")
        else:
            raise ValueError("Unsupported file format. Please provide a JSON or CSV file.")
    except Exception as e:
        st.error(f"Error loading company data: {e}")
        return {}

# Fetch industries from the loaded company data
def fetch_industries_from_data(company_name, company_data):
    if not isinstance(company_data, dict):
        raise ValueError("company_data should be a dictionary where keys are company names.")
    
    company_name = company_name.strip()
    
    if company_name in company_data:
        return company_data[company_name]
    else:
        return ["Unknown Industry"]

# Function to generate the proposal content based on the selected inputs
def display_industry_content(selected_industry, company_name):
    if selected_industry:
        use_cases_by_industry = {
            "Technology": [
                "AI-powered Code Generation and Debugging",
                "Natural Language Processing for Chatbots",
                "AI-Driven Cybersecurity Solutions",
                "Cloud Resource Optimization with AI",
                "AI Models for Predicting User Behavior",
                "Generative AI for Content Creation",
                "Optimized Machine Learning Pipelines",
                "Augmented Reality AI Integration",
                "AI-Driven Search Engine Optimization"
            ],
            'Logistics': [
            'Route Optimization: AI calculates the most efficient delivery routes to reduce travel time and costs',
            'Predictive Maintenance: AI predicts equipment failures and schedules maintenance before issues occur',
            'Demand Forecasting: AI forecasts demand to optimize inventory and prevent stockouts or overstocking',
           'Warehouse Automation: AI-powered robots and systems automate picking, packing, and sorting in warehouses',
           'Delivery Tracking: AI tracks packages in real-time and provides estimated delivery times',
            'Fleet Management: AI analyzes vehicle performance, fuel consumption, and driver behavior for better fleet optimization',
            'Supply Chain Visibility: AI provides end-to-end visibility of the supply chain for better decision-making',
            'Inventory Management: AI optimizes stock levels and distribution based on real-time data and trends',
            'AI-powered Chatbots: AI-driven chatbots assist customers with delivery inquiries and issue resolution',
            'Dynamic Pricing for Shipping: AI adjusts shipping costs based on demand, distance, and delivery urgency'
        ],
            "Advertising": [
                "General AI applications in business",
                "AI-driven Decision Support Systems",
                "Automated Business Intelligence Reports",
                "AI Models for Operational Efficiency",
                "Real-time Data Analysis with AI",
                "AI-Powered Predictive Models for Growth"
            ],
            "Cloud Computing": [
                "Cloud Infrastructure Optimization using AI",
                "AI Models for Scalable Cloud Management",
                "AI for Predictive Cloud Resource Allocation",
                "Serverless Computing Optimization with AI",
                "AI-Powered Cloud Security Solutions",
                "Cloud Service Performance Monitoring with AI",
                "AI for Cloud Data Analytics"
            ]
        }

        company_links = fetch_company_info(company_name)
        competitors = fetch_competitor_info(selected_industry)
        datasets = fetch_datasets(selected_industry)
        proposal = generate_proposal(company_name, selected_industry, use_cases_by_industry.get(selected_industry, []), datasets, company_links + competitors)

        st.subheader(f"AI & GenAI Proposal for {company_name}")
        st.write(proposal)

        st.markdown("### Proposed AI & GenAI Use Cases: ")
        for case in use_cases_by_industry.get(selected_industry, []):
            st.markdown(f"- {case}")

        st.markdown("### Recommended Datasets: ")
        valid_datasets = [dataset for dataset in datasets if is_valid_link(dataset)]
        if valid_datasets:
            valid_datasets = sorted(valid_datasets)
            for dataset in valid_datasets:
                st.markdown(f"- [Valid Dataset Link]({dataset})")
        else:
            st.markdown("**No valid datasets found for this industry.**")

        st.markdown("### Competitor Insights: ")
        competitors = sorted(competitors)
        for link in competitors:
            st.markdown(f"- [Competitor Link]({link})")

# Main streamlit app flow
st.title("AI & GenAI Use Case Generator")

# Initialize session state
if 'company_name' not in st.session_state:
    st.session_state.company_name = ""
    st.session_state.selected_industry = None
    st.session_state.placeholder_message = "Enter Company Name"
    st.session_state.show_industry_selector = False

# Handle company name input and industry selection
def handle_company_name_input(company_data):
    if st.session_state.company_name == "":
        st.session_state.placeholder_message = "Please enter a company name"
    else:
        industry_options = fetch_industries_from_data(st.session_state.company_name, company_data)
        st.session_state.show_industry_selector = True
        return industry_options

# Load company data
company_data = load_company_data("industries.json")

# Show company selection dropdown (no search input)
company_list = list(company_data.keys())
selected_company = st.selectbox("Select a Company:", company_list, key="company_select")
st.session_state.company_name = selected_company

# When a company name is selected, fetch and display industry options
if st.session_state.company_name:
    industry_options = handle_company_name_input(company_data)

    if st.session_state.show_industry_selector:
        selected_industry = st.radio("Select Industry:", industry_options)

        # Handle the "Enter" button click event
        if st.button("Enter"):
            # Define the handle_enter_click function
            def handle_enter_click(selected_industry):
                if selected_industry:
                    display_industry_content(selected_industry, st.session_state.company_name)
                else:
                    st.error("Please select a valid industry.")
            
            handle_enter_click(selected_industry)

else:
    st.write("Please select a company to fetch details.")

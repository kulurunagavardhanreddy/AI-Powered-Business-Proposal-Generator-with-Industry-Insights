# use_case_agent.py

def generate_use_cases(industry):
    use_case_map = {
        'Retail': [
            'AI-powered Customer Personalization',
            'Supply Chain Optimization with ML',
            'Chatbot Integration for Customer Support',
            'Automated Pricing Strategies',
            'Customer Sentiment Analysis',
            'Fraud Detection in Transactions',
            'Sales Trend Prediction using Time Series Data',
            'Inventory Restocking Forecasting',
            'Geo-location Targeted Marketing Campaigns'
        ],
        'Automotive': [
            'Predictive Maintenance with IoT and AI',
            'Autonomous Vehicle Navigation',
            'Energy Optimization with ML',
            'Smart Traffic Management Systems',
            'Driver Behavior Analysis with AI',
            'AI-based Crash Prevention Systems',
            'Vehicle Component Quality Assessment',
            'Real-time Fleet Monitoring',
            'Battery Performance Forecasting for EVs'
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
        'Healthcare': [
            'AI-Assisted Diagnostics',
            'Personalized Medicine using Genomic Data',
            'Predictive Health Monitoring with Wearables',
            'AI-Powered Drug Discovery',
            'Medical Image Analysis for Early Detection',
            'Patient Risk Stratification Models',
            'Clinical Trial Data Analysis',
            'Hospital Resource Optimization',
            'AI-powered Virtual Health Assistants'
        ],
        'Technology': [
            'AI-powered Code Generation and Debugging',
            'Natural Language Processing for Chatbots',
            'AI-Driven Cybersecurity Solutions',
            'Cloud Resource Optimization with AI',
            'AI Models for Predicting User Behavior',
            'Generative AI for Content Creation',
            'Optimized Machine Learning Pipelines',
            'Augmented Reality AI Integration',
            'AI-Driven Search Engine Optimization'
        ]
    }

    # Default cases for emerging industries
    default_use_cases = [
        "General AI applications in business",
        "AI-driven Decision Support Systems",
        "Automated Business Intelligence Reports",
        "AI Models for Operational Efficiency",
        "Real-time Data Analysis with AI",
        "AI-Powered Predictive Models for Growth"
    ]
    
    return use_case_map.get(industry, default_use_cases)

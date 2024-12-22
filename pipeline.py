# pipeline.py

def generate_proposal(company_name, industry, use_cases, datasets, links):
    proposal = f"Business Proposal for {company_name} in the {industry} Industry\n\n"
    proposal += "Proposed Use Cases:\n"
    for use_case in use_cases:
        proposal += f"- {use_case}\n"

    proposal += "\nRelevant Datasets:\n"
    for dataset in datasets:
        proposal += f"- [{dataset}]({dataset})\n"

    proposal += "\nSocial Media and Competitor Links:\n"
    for link in links:
        proposal += f"- {link}\n"

    return proposal


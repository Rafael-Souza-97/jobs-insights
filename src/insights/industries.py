from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries = set()
    for row in read(path):
        if row['industry']:
            industries.add(row['industry'])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    all_filtered_industries = []
    for job in jobs:
        if job['industry'] == industry:
            all_filtered_industries.append(job)
    return all_filtered_industries

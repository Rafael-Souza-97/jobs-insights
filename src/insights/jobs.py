from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    data = []
    with open(path) as file:
        jobs = csv.DictReader(file)
        for job in jobs:
            data.append(job)
        return data


def get_unique_job_types(path: str) -> List[str]:
    job_types = set()
    for row in read(path):
        if row['job_type']:
            job_types.add(row['job_type'])
    return job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    all_filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            all_filtered_jobs.append(job)
    return all_filtered_jobs

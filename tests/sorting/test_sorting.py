from src.pre_built.sorting import sort_by


jobs = [
    {"max_salary": 3000, "min_salary": 500, "date_posted": "2023-01-01"},
    {"max_salary": 1000, "min_salary": 350, "date_posted": "2023-03-01"},
    {"max_salary": 2000, "min_salary": 100, "date_posted": "2023-02-01"}
]
jobs_min_salary = [
    {"max_salary": 2000, "min_salary": 100, "date_posted": "2023-02-01"},
    {"max_salary": 1000, "min_salary": 350, "date_posted": "2023-03-01"},
    {"max_salary": 3000, "min_salary": 500, "date_posted": "2023-01-01"}
]
jobs_max_salary = [
    {"max_salary": 3000, "min_salary": 500, "date_posted": "2023-01-01"},
    {"max_salary": 2000, "min_salary": 100, "date_posted": "2023-02-01"},
    {"max_salary": 1000, "min_salary": 350, "date_posted": "2023-03-01"}
]

jobs_date_posted = [
    {"max_salary": 1000, "min_salary": 350, "date_posted": "2023-03-01"},
    {"max_salary": 2000, "min_salary": 100, "date_posted": "2023-02-01"},
    {"max_salary": 3000, "min_salary": 500, "date_posted": "2023-01-01"}
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted

from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    all_salaries = []
    for column in read(path):
        if column['max_salary']:
            try:
                int_salary = int(column['max_salary'])
                all_salaries.append(int_salary)
            except ValueError:
                pass
    return max(all_salaries)


def get_min_salary(path: str) -> int:
    all_salaries = []
    for column in read(path):
        if column['min_salary']:
            try:
                int_salary = int(column['min_salary'])
                all_salaries.append(int_salary)
            except ValueError:
                pass
    return min(all_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])

    except KeyError:
        raise ValueError("'min_salary' e 'max_salary' são obrigatórios.")

    except TypeError:
        raise ValueError("'min_salary' e 'max_salary' devem ser números.")

    try:
        int_salary = int(salary)

    except TypeError:
        raise ValueError("O salário deve ser um número.")

    if min_salary > max_salary:
        raise ValueError("'max_salary' deve ser maior que 'min_salary'.")

    return max_salary >= int_salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

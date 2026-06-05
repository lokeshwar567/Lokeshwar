company_budget = 50000
def company_tracker():

    total_projects = 100
    def update_projects():
        nonlocal total_projects
        total_projects+=20
        global company_budget
        company_budget+=100000
        print(company_budget,total_projects)
    update_projects()
company_tracker()
from datetime import datetime

"""
    get current time

    Purpose:
    provide exact time for code review agent to write the time accurately
"""
def get_date():
    print(datetime.now())
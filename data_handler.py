import json
from datetime import datetime

def save_data(user_info, candidate):
    """ Save the vote and user information to a JSON file. """
    try:
        data = {'User': user_info, 'Vote': candidate}
        with open('votes.json', 'a') as file:
            json.dump(data, file)
            file.write("\n")
        return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def validate_date(date_str):
    """ Validate the date format 'YYYY-MM-DD'. """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

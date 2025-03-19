import sys
import requests

from events import EVENT_HANDLERS

def print_events(events):
    for event in events:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        handler = EVENT_HANDLERS.get(event_type)
        if handler:
            handler(event, repo_name)


def get_latest_events(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {
        'Accept': 'application/vnd.github+json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            events = response.json()
            if not events:
                print(f"No events found for {username}.")
                return 

            print_events(events)   
        else:
            print(f"Failed to retrieve events. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        get_latest_events(username)
    else:
        print("Please provide a GitHub username.")

import json
import requests
import os


def get_activities(access_token):
    url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        print("RESPONSE: \n", response.json)
        # Successful response returns the json data.
        return response.json()
    else:
        # Something went wrong so return None
        return None


def save_activities(activities):
    if activities:
        activities = get_activities(access_token=access_token)
        with open("activity_responses.json", "w") as f:
            json.dump(activities, f, indent=2)
    else:
        print("No activites availble to save.")
    return


if __name__ == "__main__":
    # Read access token from strava_tokens.json
    with open("strava_tokens.json", "r") as tokens_file:
        data = json.load(tokens_file)
        most_recent_tokens = data[-1]

    access_token = most_recent_tokens["access_token"]

    activities = get_activities(access_token=access_token)
    if activities:
        for activity in activities[:5]:  # just look at the first 5 for now
            print(activity["type"])
            # print(activity["name"], "-", activity["distance"], "meters")
    else:
        print("Failed to fetch activities.")

    save_activities(activities)

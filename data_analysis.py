import json
import requests
import os
import datetime

# Extract running stats for the last 7 days


def load_activities_file():
    # Bring in the activity responses file
    with open("activity_responses.json", "r") as activities_file:
        activities = json.load(activities_file)
    return activities


def get_running_stats(activities, numDays=7):
    total_distance = 0
    total_climb = 0
    total_moving_time = 0
    total_elapsed_time = 0
    current_date = datetime.datetime.now()
    for activity in activities:
        # TODO - there will eventually need to be a or loop here that
        # TODO   checks the activity was done in the last 7 days
        total_distance += activity["distance"]
        total_climb += activity["total_elevation_gain"]
        total_moving_time += activity["moving_time"]  # time is in seconds
        total_elapsed_time += activity["elapsed_time"]  # time is in seconds

    running_stats = [total_distance, total_climb, total_elapsed_time, total_moving_time]
    return running_stats


if __name__ == "__main__":
    activities = load_activities_file()
    running_stats = get_running_stats(activities=activities, numDays=7)

    print(running_stats)

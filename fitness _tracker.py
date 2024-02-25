import googlemaps
from datetime import datetime

class FitnessTracker:
    def __init__(self, user_type):
        self.user_type = user_type
        self.workouts = []

    def log_workout(self, activity, duration):
        workout = {'activity': activity, 'duration': duration, 'timestamp': datetime.now()}
        self.workouts.append(workout)

    def calculate_distance(self, start_location, end_location):
        gmaps = googlemaps.Client(key='YOUR_API_KEY')
        distance = gmaps.distance_matrix(start_location, end_location)['rows'][0]['elements'][0]['distance']['text']
        return distance

    def display_progress(self):
        total_duration = sum(workout['duration'] for workout in self.workouts)
        print(f"Total duration of workouts: {total_duration} minutes")

        if self.user_type == 'disabled':
            print("Since you are disabled, we're here to support you in your fitness journey!")
        else:
            total_distance = 0
            for i in range(len(self.workouts) - 1):
                start_location = self.workouts[i]['activity']
                end_location = self.workouts[i + 1]['activity']
                distance = self.calculate_distance(start_location, end_location)
                total_distance += float(distance.split()[0])
            print(f"Total distance covered: {total_distance} kilometers")

# Example Usage:
tracker = FitnessTracker(user_type='normal')
tracker.log_workout('Gym', 60)
tracker.log_workout('Park', 30)
tracker.log_workout('Swimming Pool', 45)
tracker.display_progress()

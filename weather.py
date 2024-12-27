import requests

def fetch_weather(city):
    """Fetch weather details for a given city."""
    api_key = "31895d271571d8b36da9d91f08d14d86"
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            "city": city,
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    except requests.exceptions.RequestException as e:
        return {"error": "Error fetching data. Please check the city name and try again."}

def display_weather(data):
    """Display weather details in a user-friendly format."""
    if "error" in data:
        print(f"\nError: {data['error']}")
        return

    print(f"\nWeather in {data['city']}, {data['country']}:")
    print(f"{'-' * 30}")
    print(f"Temperature: {data['temperature']}°C (Feels like: {data['feels_like']}°C)")
    print(f"Condition: {data['condition'].capitalize()}")
    print(f"Humidity: {data['humidity']}%")
    print(f"Wind Speed: {data['wind_speed']} m/s")
    print(f"{'-' * 30}\n")

def save_weather_to_file(data, filename="weather_report.txt"):
    """Save weather details to a file."""
    if "error" in data:
        print("\nCannot save data. There was an error fetching the weather information.")
        return

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Weather in {data['city']}, {data['country']}:\n")
        file.write(f"{'-' * 30}\n")
        file.write(f"Temperature: {data['temperature']}°C (Feels like: {data['feels_like']}°C)\n")
        file.write(f"Condition: {data['condition'].capitalize()}\n")
        file.write(f"Humidity: {data['humidity']}%\n")
        file.write(f"Wind Speed: {data['wind_speed']} m/s\n")
        file.write(f"{'-' * 30}\n")
    print(f"\nWeather details saved to {filename}.")

def main():
    """Main function to run the Weather Dashboard."""
    print("Welcome to the Weather Dashboard!")

    while True:
        print("\nOptions:")
        print("1. Get weather details")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            city = input("\nEnter the city name: ").strip()
            if not city:
                print("Please enter a valid city name.")
                continue

            weather_data = fetch_weather(city)
            display_weather(weather_data)

            save_option = input("Do you want to save this weather report to a file? (yes/no): ").strip().lower()
            if save_option == "yes":
                filename = input("Enter the filename (default: weather_report.txt): ").strip()
                if not filename:
                    filename = "weather_report.txt"
                save_weather_to_file(weather_data, filename)
        elif choice == "2":
            print("Thank you for using the Weather Dashboard. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

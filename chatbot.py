import random

# Define the chatbot's responses
hostel_info = {
    "rooms": "Our hostel has a variety of room types, including private rooms, shared dormitories, and family rooms. All rooms are clean, comfortable, and well-equipped.",
    "amenities": "We offer a range of amenities, including a common lounge, a shared kitchen, free Wi-Fi, and laundry facilities.",
    "location": "Our hostel is located in the heart of the city, just a short walk away from popular tourist attractions and public transportation.",
    "policies": "Our check-in time is 3 PM, and check-out time is 11 AM. We have a 24-hour front desk and a flexible cancellation policy.",
    "activities": "We organize various activities and events for our guests, such as walking tours, movie nights, and social gatherings.",
    "default": "I'm afraid I don't have specific information on that. However, I'd be happy to assist you with other questions about our hostel and its services."
}

# Define the chatbot function
def hostel_chatbot(prompt):
    """
    Generates a response to the user's input based on predefined information.

    Args:
        prompt (str): The user's input to the chatbot.

    Returns:
        str: The chatbot's response.
    """
    # Check if the user's input matches any of the predefined topics
    for topic, response in hostel_info.items():
        if topic.lower() in prompt.lower():
            return response

    # If no match is found, return a default response
    return hostel_info["default"]

# Run the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    response = hostel_chatbot(user_input)
    print(f"Chatbot: {response}")
import os
from googleapiclient.discovery import build
import google.generativeai as genai

genai.configure(api_key="AIzaSyDlhRFAffcNyYr8Se9QI5ZDvojNTqKkM18")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Initialize YouTube API
def initialize_youtube():
    api_key = os.getenv('YOUTUBE_API_KEY')
    if not api_key:
        raise ValueError("YouTube API key not found. Please set the YOUTUBE_API_KEY environment variable.")
    return build('youtube', 'v3', developerKey=api_key)

# Fetch YouTube data
def fetch_video_links(youtube, keyword, rate_limit):
    # Initialize an empty list to store video links
    video_links = []

    # Search for videos related to the keyword
    search_response = youtube.search().list(
        part="snippet",
        q=keyword,
        type="video",
        maxResults=rate_limit
    ).execute()

    # Iterate through search results
    for item in search_response.get("items", []):
        # Extract video ID and construct the video link
        video_id = item["id"]["videoId"]
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        
        # Append the video link to the list
        video_links.append(video_link)

    return video_links

# Function to extract keyword from user input
def extract_keyword(user_input):
    # Split the input into words and find the first word as the keyword
    words = user_input.split()
    keyword = words[0] if words else ""
    return keyword

# Function to generate content based on user input
def generate_content(user_input):
    sections = ["Definition:", "Awareness:", "Real-time Example:", "Context (points to consider):"]
    section_texts = []
    
    if user_input == 1:
        prompt = "Safety measures to avoid unnecessary problems for a student crossing a road:\n"
    elif user_input == 2:
        prompt = "Tracking moving objects which require sustained visual focus demands:\n"
    elif user_input == 3:
        prompt = "Identifying specific information that involves sensory classification:\n"
    elif user_input == 4:
        user_input = input("Enter your custom prompt: ")
        prompt = f"{user_input}:\n"
    else:
        return "Invalid input. Please choose a number from 1 to 4."

    for section in sections:
        prompt += section + "\n"
        response = model.generate_content(prompt)
        section_text = response.text.strip()
        prompt += section_text + "\n"
        section_texts.append(section_text)

    return "\n".join(section_texts)

# Main function to handle user interaction
def main():
    youtube = initialize_youtube()

    while True:
        print("\nChoose an option:")
        print("1. Safety measures to avoid unnecessary problems for a student crossing a road")
        print("2. Tracking moving objects which require sustained visual focus demands")
        print("3. Identifying specific information that involves sensory classification")
        print("4. Enter a custom prompt")
        print("5. Exit")

        option = input("Enter your choice (1-4): ")
        if option.isdigit():
            option = int(option)
            if 1 <= option <= 4:
                output = generate_content(option)
                print("\nGenerated Content:\n" + output)

                # Extract the keyword from the user input
                user_input = output.split("\n")[0]
                keyword = extract_keyword(user_input)
                rate_limit = 5  # Fetch maximum 5 related videos

                # Fetch and print video links related to the keyword
                video_links = fetch_video_links(youtube, keyword, rate_limit)
                if video_links:
                    print(f"\nVideos related to '{keyword}':")
                    for video_link in video_links:
                        print(video_link)
                else:
                    print(f"No videos found for the keyword '{keyword}'.")
                    
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

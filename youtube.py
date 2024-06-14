import os
from googleapiclient.discovery import build

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

# Example usage
def main():
    # Get input from the user
    keyword = input("Enter the keyword to search for: ")
    rate_limit = int(input("Enter the maximum number of videos to fetch: "))

    youtube = initialize_youtube()
    video_links = fetch_video_links(youtube, keyword, rate_limit)

    # Output video links
    if video_links:
        print("Video Links:")
        for video_link in video_links:
            print(video_link)
    else:
        print(f"No videos found for the keyword '{keyword}'.")

if __name__ == "__main__":
    main()

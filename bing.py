import webbrowser
import urllib.parse

def search_on_bing(query):
    # Encode the query for the URL
    encoded_query = urllib.parse.quote(query)
    
    # Construct the Bing Chat URL with the encoded query
    url = f"https://www.bing.com/chat?q={encoded_query}&qs=ds&form=CONVCP"
    
    # Open the URL in the default web browser
    webbrowser.open(url)

if __name__ == "__main__":
    # Get the search query from the user
    search_query = input("Enter your search query: ")
    
    # Call the function to search on Bing Chat
    search_on_bing(search_query)
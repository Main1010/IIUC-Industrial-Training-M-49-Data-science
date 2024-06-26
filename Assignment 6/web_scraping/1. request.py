"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com
Version: 1.0

This module demonstrates the usage of the `requests` library in Python for making HTTP requests.
It covers various real-world examples including GET and POST requests, handling response data,
and working with headers and parameters. This script is designed as an educational tool for
understanding web scraping and API interaction using Python.
"""
import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError
def get_example():
    # Replace with your API endpoint URL
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        # Send GET request to the API endpoint
        response = requests.get(api_url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse JSON response
            posts = response.json()
            
            # Iterate over each post and print its title
            for post in posts:
                print(post['title'])
        else:
            # Print an error message if request was unsuccessful
            print(f"Failed to retrieve posts. Status code: {response.status_code}")
    
    except ConnectionError:
        print("Error: Unable to connect to the URL.")
    except Timeout:
        print("Error: The request timed out.")
    except requests.exceptions as e:
        print(f"Error: An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




def post_example():
    """
    Demonstrates a simple POST request using the `requests` library.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'C201091 Mian'
    }
    response = requests.post(url, json=data)
    
    # Check if the request was successful
    if response.status_code == 201:
        print("POST request successful!")
        # Print response content
        print(response.json())
    else:
        print("Failed to post data")

def main():
    """
    Main function to execute the examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

if __name__ == "__main__":
    main()


# Assignments
# 1. Modify the GET Example: Change the get_example function to fetch a list of posts instead of just one. Analyze the JSON structure and print out the titles of all posts.

# 2. Error Handling: Add error handling to both functions to manage exceptions like connection errors or timeouts.


# Advanced requests
"""
This module discuss advanced features like custom headers, user agents, and error handling.


Custom Headers and User Agents: These are used to provide additional information to the server about the request being made. For example, the 
`User-Agent` header can be used to simulate requests from different browsers.

Error Handling: The `try-except` blocks are used to catch and handle different types of exceptions that might occur during the request, such as network problems or invalid responses.
"""


#!/bin/bash
# Check for the required arguments
if [ $# -ne 1 ]; then
   echo "Usage: $0 <data_file.json>"
   exit 1
fi

# Define the target URL
URL="http://0.0.0.0:5000/catch_me"

# Send the POST request using curl
response=$(curl -s -X POST "$URL" -d @"$1" -H "Content-Type: application/json")

# Extract the relevant part of the response containing "You got me!"
if [[ $response == *"You got me!"* ]]; then
  # Success - The message is found 
  echo "Success: Server responded with 'You got me!'"
else
  # Failure - The expected message is not in the response
  echo "Error: Unexpected response from the server."
fi


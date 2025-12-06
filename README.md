---
title: Binary Search Visualization
sdk: "gradio"
sdk_version: "6.0.2"
app_file: app.py
pinned: false
---

# CISC 121 Final Project
The binary search algorithm implemented in an interactive web app using Gradio.

Can be found on: [Hugging Face](https://huggingface.co/spaces/compsup/CISC121-FinalProject)

## Project showcase
![Showcase gif](showcase.gif)

## Project Design
### Decomposition

The algorithm can be split up into
- Look at the middle element
- Decide which half of the list to search next
- Select a new middle element

### Pattern Recognition
- If the middle element is bigger, the target must be in the left half
- If the middle element is smaller, it must be in the right half.

### Abstraction
The user only sees:
- List to search
- Number to search for

### Algorithm
- Compute the middle index.
- Compare the target with the middle value.
- If equal, found.
- If target < middle, repeat on left half.
- If target > middle, repeat on right half.
- Stop when low > high (not found).

## Steps to Run
- Install all required packages using `pip install -r requirements.txt`
- Then run the app using `python app.py`
- Navigate to the url printed out

In the application, you first hit the generate button to create a set of integers to search. Then, find a number you want to look for, enter that into the `number` field. Hit `step` until the number is found (or not).

# Testing
These edge cases in the program have been tested:
- Incorrectly inputting the search number (not a number)
- Not generating a set before stepping
- Searching for a number that does not exist

Descriptive error messages were added, for example if the user tries to step through without first generating a set it will say "Please generate a set first!" in an error message.

The program was also tested to make sure it functions as intended.

# Acknowledgements

Made by Lauren McQuat for the CISC121 Final Project @ Queen's University.

ChatGPT was used to work around and understand gradio's app lifecycle that is poorly documented.
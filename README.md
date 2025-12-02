---
title: Binary Search Visualization
sdk: "gradio"
sdk_version: "5.49.1"
app_file: app.py
pinned: false
---

# CISC 121 Final Project
The binary search algorithm implemented in an interactive web app using Gradio.

## Project showcase
![Showcase gif](example.gif)

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


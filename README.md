## Where In the World Is the International Space Station (ISS)?

### Objectives
- Use the `requests` package to query real-world data
- Improve skills with dictionaries and indexing

### Part A
Write a function that uses [this public API](http://api.open-notify.org/astros.json) to obtain a list of the astronauts who are currently in space. The function should print the total number of astronauts in space, their full names, and the spacecraft they are currently on board.

### Part B
Write another function that uses [this public API](http://api.open-notify.org/iss-now.json) to obtain the current location of the space station. The function should print the current geographic coordinates (lat/lon) of the space station along with a timestamp.

### Part C
Write another function that uses [this public API](http://api.open-notify.org/iss-pass.json) to find out the next time that the ISS will be overhead of Indianapolis, Indiana. The function should print the next passover time in a human-readable format.

*Note*: You will need to supply the lat/lon coordinates as query parameters to the API URL. The passover times are contained in the response as timestamps, so you will need to use the `time.ctime()` method to convert them to human-readable text.

## Submitting your work
To submit your solution for grading, you will need to create a GitHub [Pull Request (PR)](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). Refer to the `PR Workflow` article in your course content for details.

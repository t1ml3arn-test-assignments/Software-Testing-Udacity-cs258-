# Udacity's Software Testing course

A course about how to make software fail.

This repo contains some programming exercises from this course (not all of them, ~ the second half).

## Course links

- the course [itself](https://www.udacity.com/course/software-testing--cs258)
- its [wiki](https://www.udacity.com/wiki/cs258) 
- its [forums](https://discussions.udacity.com/c/standalone-courses/software-testing)

## Python coverage tool

- install it with `pip install coverage`
- run it with command `coverage run --branch your-file.py && coverage report && coverage html`
    - `--branch` also measures branch coverage (by default there is only statement coverage)
    - `report` shows coverage report in console output
    - `html` generates html report (you have to locate and open it manualy with your browser)

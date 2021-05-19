# Assessment 3: Django

## Important Grading Information
* TODO PUT RUBRIC HERE
* This assessment is worth 15% of your final grade. You need to get a 75% or better to pass.
* If you fail the assessment, you will have one week to retake it for a 10% penalty. We will not regrade passing assessments.

## Rules / Process
* This test is fully open notes and open Google, but is not to be completed with other students
* Do not open a pull request against this repository. We will evaluate your code individually with you.

## Challenge
Everyone loves going on Craigslist to find interesting people and interesting items. The joy of Craigslist is that it doesn't upgrade itself to stay up to date with the times - its the same old Craigslist that everyone knows and loves. This works out well for us as our client has asked for no styling. The core schema has also remained relatively unchanged over the years. Today, you will build a basic Craigslist CRUD app with nested routes. We will call this Craigslist Junior.

Here are a list of the routes you will need to build:
* `/categories`: A list of all the categories
* `/categories/new`: The form for a new category
* `/categories/:id`: See a specific category and a list of all of its associated posts
* `/categories/:id/edit`: Edit page for a specific category (also the ability to update/destroy categories)
* `/categories/:category_id/posts/new`: The form for a new post under a specific category
* `/categories/:category_id/posts/:post_id`: See a specific post for a specific category, have the ability go back to all of the post's category's other posts (`/categories/:category_id/posts`)
* `/categories/:category_id/posts/:post_id/edit`: Edit page for a specific post under a specific category (Also, the ability to update/destroy posts)

# Django Custom User Project
## Live Link - https://django-app-frfe.onrender.com/


This is a Django project that demonstrates the usage of a custom user model , that has 2 types of users 1. Dcotor 2. Patient with additional fields. It also allows doctors to post blogs and readers to read them.

## Features

- User Authentication
- Blog System Integration

## User Authentication

### User Types

- **Patient**
- **Doctor**

### Signup Form Fields

- First Name
- Last Name
- Profile Picture
- Username
- Email Id
- Password
- Confirm Password
- Address (line1, city, state, pincode)

### Dashboard

- Display user details entered during signup

## Blog System Integration

### Categories

- Mental Health
- Heart Disease
- Covid19
- Immunization
- (Add more categories as needed)

### Blog Post Creation

- Title
- Image
- Category
- Summary
- Content
- Mark as Draft option

### Drafts

- Ability to mark a blog post as a draft during creation

### Doctor View

- View and manage all blog posts created by the doctor
- Create new blog posts

### Patient View

- View lists of blog posts based on categories
- Display title, image, and a truncated summary (max 15 words)
- Read full blog post by clicking on a link

## How to Run

pip install -r requirements.txt <br>
python manage.py migrate <br>
python manage.py runserver <br>



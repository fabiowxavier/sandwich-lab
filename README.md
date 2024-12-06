# Sandwich Lab

Sandwich Lab is a web-based platform built using Django, providing users with a place to explore, manage, and review different sandwich recipes. Users can view a variety of sandwiches, read details, and even leave their own reviews. The project is part of the Code Institute’s Full-Stack Developer course, focusing on the Django framework, PostgreSQL database integration, and basic CRUD functionality.

### Sandwich Lab Homepage

- **Live site**: [Sandwich Lab](http://link-to-live-site.com)
- **For Admin access with relevant sign-in information, [click here](#).**
- **GitHub repository**: [Sandwich Lab GitHub](http://link-to-repository.com)

---

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
  - [Colour Scheme](#colour-scheme)
  - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
  - [Site Goals](#site-goals)
  - [Agile Methodologies](#agile-methodologies---project-management)
  - [MoSCoW Prioritization](#moscow-prioritization)
  - [Sprints](#sprints)
  - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
  - [Wireframes](#wireframes)
- [Database Schema - ERD](#database-schema---entity-relationship-diagram)
- [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [Role-Based Dashboard Features](#role-based-dashboard-features)
  - [Appointment Booking System](#appointment-booking-system)
  - [Messaging System](#messaging-system)
- [Technologies & Languages Used](#technologies--languages-used)
  - [Libraries & Frameworks](#libraries--frameworks)
  - [Tools & Programs](#tools--programs)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Heroku Deployment](#heroku-deployment)
- [Privacy Policy](#privacy-policy)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

---

## Overview

Sandwich Lab is a platform that allows users to:

- Browse a variety of sandwiches
- Add their own sandwich recipes and ingredients
- Leave reviews on different sandwiches
- Manage their profiles and view previously added sandwiches

This platform is designed to bring together people who love sandwiches and want to share their creations with the world.

---

## UX - User Experience

### Design Inspiration
The design of **Sandwich Lab** was inspired by my love of food and the joy of sharing great sandwich recipes. I wanted to create a space where people could share their sandwich ideas and recipes, interact with one another, and build a community of sandwich enthusiasts.

### Colour Scheme
- **Primary Color**: #FF6347 (Tomato Red)
- **Secondary Color**: #FFD700 (Golden Yellow)
- **Accent Color**: #FFFFFF (White)
- **Background**: #F5F5F5 (Light Grey)

This combination ensures a vibrant yet clean appearance, matching the food-related theme of the website.

### Font
- **Logo & Headers**: Bungee Shade
- **Body Text & Interactive Elements**: Roboto

---

## Project Planning

### Strategy Plane
The primary goal of **Sandwich Lab** is to offer a user-friendly platform for sandwich enthusiasts to create, share, and discover new sandwich recipes. This project aims to streamline the process of recipe-sharing and allow users to express their love for sandwiches.

### Site Goals
- Provide a platform for users to browse, create, and share sandwich recipes.
- Enable users to rate and leave reviews on various sandwiches.
- Allow users to manage their personal profiles and view their posted recipes.

### Agile Methodologies - Project Management
The project was managed using agile methodologies, breaking down the development process into sprints. Tasks were tracked using GitHub’s project board and issues.

### MoSCoW Prioritization
- **Must-Haves**: User registration and login, sandwich recipe creation, reviews, and profiles.
- **Should-Haves**: Sandwich recipe search functionality, improved UI/UX.
- **Could-Haves**: User-generated images for sandwiches, social media sharing.
- **Won’t-Haves**: Full payment integration.

### Sprints
1. **Sprint 1**: Set up Django project and environment.
2. **Sprint 2**: User authentication and profile creation.
3. **Sprint 3**: Sandwich recipe creation and review functionality.
4. **Sprint 4**: UI/UX improvements and search functionality.
5. **Sprint 5**: Deployment and final testing.

### User Stories
- As a **user**, I want to register securely so I can manage my sandwich recipes.
- As a **user**, I want to search for sandwiches by ingredients so I can find recipes I like.
- As a **user**, I want to leave reviews and ratings for sandwiches.
- As an **admin**, I want to manage users and sandwich submissions.

### Scope Plane
The **Sandwich Lab** platform includes the following MVP functionalities:

- User registration, login, and profile management.
- Sandwich recipe creation, viewing, and rating.
- CRUD operations for sandwich recipes and reviews.

### Wireframes
Wireframes were created for the following pages:
- **Home Page**: Displays featured sandwiches and an overview of the platform.
- **Sandwich Detail Page**: View detailed information about each sandwich recipe.
- **User Profile Page**: Users can view and manage their submitted sandwiches.
- **Admin Panel**: Admins can manage users and sandwich submissions.

Wireframes were designed using **Balsamiq** to ensure usability and clarity.

---

## Database Schema - ERD

The **Entity Relationship Diagram (ERD)** shows the relationships between **users**, **sandwiches**, and **reviews**. This is important to visualize how different data points interact within the PostgreSQL database.

---

## Security
The platform uses Django’s built-in security features to handle user authentication securely, and ensure that sensitive data is protected.

---

## Features

### User View - Registered/Unregistered
**Unregistered users** can view sandwich recipes and browse the platform. **Registered users** have full access to create, edit, and delete their recipes and reviews.

### Role-Based Dashboard Features
- **User Dashboard**: View and manage submitted sandwich recipes, ratings, and reviews.
- **Admin Dashboard**: Manage users and their submitted sandwiches.

### Profile Management
Users can view and edit their profiles, including their sandwich recipes and reviews.

---

## Technologies & Languages Used

### Libraries & Frameworks
- **Django**: Backend framework
- **PostgreSQL**: Database management system
- **Cloudinary**: For media storage
- **Whitenoise**: For static file management

### Tools & Programs
- **GitHub**: Version control and project management
- **Heroku**: Deployment and hosting
- **Balsamiq**: Wireframes

---

## Testing

### Validation Testing
- **HTML**: W3C HTML Validator.
- **CSS**: W3C CSS Validator.
- **Python**: PEP8 validation.

### User Testing
- **Browser Compatibility**: Tested across Chrome, Firefox, Safari, and Edge.
- **Responsiveness**: Ensured that the site works on mobile, tablet, and desktop.

---

## Deployment

### Connecting to GitHub
The project was connected to GitHub for version control and was deployed using Heroku. The necessary steps for deployment include configuring the `Procfile`, setting up environment variables, and using Git for version control.

### Heroku Deployment
- Deployed to Heroku by connecting the GitHub repository and configuring necessary environment variables such as `DATABASE_URL`, `CLOUDINARY_URL`, and `SECRET_KEY`.

---

## Privacy Policy
As part of this project, user data such as registration details and sandwich submissions are securely stored, with role-based access ensuring the privacy of personal information. The platform does not share personal data with third parties.

---

## Credits

### Code
- Django Documentation
- ChatGPT AI for code ideas and implementation suggestions
- Favicon.io for favicon generation
- Google Fonts for typography

### Media
- Icons and images from **Canva** and **ChatGPT**

---

## Acknowledgements
Special thanks to **Amy Richardson** and **Mark Brisco** for their mentorship, guidance, and valuable feedback throughout this project. Also, thanks to **Code Institute** for providing the resources and environment to complete the project.

---

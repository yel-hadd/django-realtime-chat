# Realtime Chat App

This application is a Realtime Chat App developed using Django and Django Channels.

## Setup

This project includes a Makefile for easy management of the app. Below are some useful commands to get started:

### Installation

To set up the virtual environment and install necessary dependencies:

```bash
make venv
```

### Initialize Database

Apply database migrations to sync the database schema:

```bash
make makemigrations
make migrate
```

### Create Superuser

Create a superuser to access the admin panel at `/admin`:

```
make createsuperuser
```

### Run Development Server

To run the development server:

```bash
make runserver
```

## Resources

Here are some the resources I used to create this project:

- [Django Documentation](https://docs.djangoproject.com/en/) - Official documentation for Django web framework.
- [Django Channels Documentation](https://channels.readthedocs.io/en/) - Documentation for Django Channels, enabling real-time capabilities in Django.
- [ Python Django Realtime Chat Project - Full Course ](https://www.youtube.com/watch?v=SF1k_Twr9cg) - Tutorial for Creating Realtime Chat App.
- [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework for rapidly building custom designs.
- [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) - WebSockets API documentation.
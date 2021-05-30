
<p align="center">
  <a href="https://github.com/mage1711/flashCards-django">
    <img src="https://img.icons8.com/ios/100/000000/flashcards.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Flash Cards App</h3>

  <p align="center">
    A flash card sharing app
    <br />
    <a href="http://206.189.58.188:1337/flashcards/">View Demo</a>
  </p>
</p>

<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
           <li><a href="#functionality">Functionality</a></li>
               <li><a href="#screenshots">Functionality</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
This app was Buit to give users the ability to share flash cards with each other_app sample login:
* email: test@test.com
* password: test1234

### Functionality
* [Homepage](http://206.189.58.188:1337/flashcards/)
* [Login](http://206.189.58.188:1337/flashcards/login/)
* [Signup](http://206.189.58.188:1337/flashcards/signup/)
* [Search](http://206.189.58.188:1337/flashcards/search/?csrfmiddlewaretoken=yC0QcYGm6YS4Jb1UmA1veaxQOEdkzGIVxr1XvzMoH55DnVoFXd0wQ4TvXrXRDeEw&search=Chemistry)


### Screenshots
<div align="center" style="margin-top:10px;"  >
<div style="margin:50px;">
<h2>landing page</h2>
<a href="http://206.189.58.188:1337/flashcards/" >
 <img src="https://drive.google.com/uc?export=view&id=1gEatie3kxd8raQF49iEz8XOqQTc-h7_K"  alt="ScreenShot.logo" width="1280"/>
</a>
</div>
<div style="margin:50px;">
<h2>Login</h2>
<a href="http://206.189.58.188:1337/flashcards/login/" >
 <img src="https://drive.google.com/uc?export=view&id=1VKVH5NeXheC_dYURQbkwFt8YCVGtLcCA"  alt="ScreenShot.logo" width="720"/>
</a>
</div>
<div style="margin:50px;">
<h2>Search</h2>
<a href="http://206.189.58.188:1337/flashcards/search/?csrfmiddlewaretoken=yC0QcYGm6YS4Jb1UmA1veaxQOEdkzGIVxr1XvzMoH55DnVoFXd0wQ4TvXrXRDeEw&search=Chemistry" >
 <img src="https://drive.google.com/uc?export=view&id=1FgKiPC9A4Vh1ieupQjs8FLe6gz6xAKm-"  alt="ScreenShot.logo" width="1280"/>
</a>
</div>
<div style="margin:50px;">
<h2>Add card</h2>
<a href="" >
 <img src="https://drive.google.com/uc?export=view&id=16um5xT5s4zSCZacNT5lAbclyhANk9vrI"  alt="ScreenShot.logo" width="1280"/>
</a>
</div>
<div style="margin:50px;">
<h2>Sign up</h2>
<a href="http://206.189.58.188:1337/flashcards/signup/" >
 <img src="https://drive.google.com/uc?export=view&id=1qBEzJ6msFkbbPqPwdwlxNdVROR78y__F"  alt="ScreenShot.logo" width="620"/>
</a>
</div>
</div>



### Built With

* [Django](https://www.djangoproject.com/)<img src="https://static.djangoproject.com/img/logos/django-logo-negative.png " alt="Dajngo.logo" width="25" style="margin-left: 10px;"/>
* [PostgreSQL](https://www.postgresql.org/)<img src="https://www.logo.wine/a/logo/PostgreSQL/PostgreSQL-Logo.wine.svg" alt="PostgreSQL.logo" width="30" style="margin-left: 5px;"/>
* [Docker](https://www.docker.com/)<img src="https://www.docker.com/sites/default/files/d8/2019-07/Moby-logo.png" alt="Docker.logo" width="25" style="margin-left: 10px;"/>
* [Nginx](https://www.nginx.com/)<img src="https://cdn.wpmentor.com/wp-content/uploads/2019/05/Nginx-1.png" alt="Nginx.logo" width="20" style="margin-left: 10px;"/>
* [Tailwind](https://tailwindcss.com/)<img src="https://seeklogo.com/images/T/tailwind-css-logo-5AD4175897-seeklogo.com.png" alt="Tailwind.logo" width="20" style="margin-left: 10px;"/>


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Docker
  ```sh
  sudo apt-get install docker-ce docker-ce-cli containerd.io
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mage1711/flashCards-django.git
   ```
2. cd into folder
   ```sh
   cd flashCards-django
   ```
2. create .env file
   ```sh
   mkdir .env
   ```
4. Build image
   ```sh
   docker-compose -f docker-compose.yml up -d --build
   ```
4. go to
   ```sh
   image will up at http://localhost:1337/
   ```




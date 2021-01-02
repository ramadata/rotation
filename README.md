# Rotation

While on Clubhouse (a new audio-only social media app) I spent time in an R&B room——my favorite genre of music——named 360RNB. The room consisted of journalists, A&Rs, musicians, music lovers, etc. who shared music from undiscovered, new, and established artists. It had to be the most calming and sonically enjoyable experiences I've had on the app (being that the app is audio-only and there is quite a bit of noise). I thought what if we had an app strictly for sharing music? So I decided to create "Rotation": an app for sharing the music you have in rotation.

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6d3401ba... updated views and urls
Check out video of the app running on a server: <https://github.com/ryreadme/rotation/blob/master/rotation_vid.mp4>

    <img src='https://github.com/ryreadme/rotation/blob/master/images/rotation.png' alt='home screen'>
    <img src='https://github.com/ryreadme/rotation/blob/master/images/join.png' alt='join page'>
    <img src='https://github.com/ryreadme/rotation/blob/master/images/create.png' alt='create room page'>
    <br>
    <img src='https://github.com/ryreadme/rotation/blob/master/images/admin.png' alt='admin login in'>
    <img src='https://github.com/ryreadme/rotation/blob/master/images/admin_logged_in.png' alt='admin logged in'>

<<<<<<< HEAD
=======
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls
## Project Setup

You must have NodeJS installed on your computer.
<https://nodejs.org/en/download/>

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6d3401ba... updated views and urls
1. `mkdir name_of_your_directory`
2. `cd name_of_your_directory`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip install django djangorestframework`
<<<<<<< HEAD
=======
>>>>>>> 9ae9138d... added spotify api
`mkdir name_of_your_directory`
`cd name_of_your_directory`
`python3 -m venv env`
`source env/bin/activate`
`pip install django djangorestframework`
<<<<<<< HEAD
=======
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls

### Backend

To set up the backend of the app: `django-admin startapp name`. After installing the djangorestframework, go into settings.py in your project folder and place 'rest_framework' in the INSTALLED_APPS list. Make sure to register your apps in the INSTALLED_APPS section of settings.py with the format `name.apps.NameConfig`. Make sure to open apps.py inside the apps.py and make sure it matches the name of the class. You will need to create models and serializers and then show them with views. That is very easily explained and demonstrated here:

Models & Serialization: <https://www.django-rest-framework.org/tutorial/1-serialization/>
Views: <https://www.django-rest-framework.org/tutorial/3-class-based-views/>

### Frontend

Create a new app for the frontend of the app using the same command in terminal: `django-admin startapp frontend`. Run the commands below in the terminal.

Frontend Packages:

<<<<<<< HEAD
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
>>>>>>> 6d3401ba... updated views and urls
1. `npm init -y`
2. `npm install react react-dom --save-dev`
3. `npm install react-router-dom`
4. `npm install @material-ui/core`
5. `npm install @material-ui/icons`
6. `npm install @babel/core babel-loader @babel/preset-react --save-dev`
7. `npm install @babel/preset-env --save-dev`
8. `npm install @babel/plugin-proposal-class-properties`
9. `npm install webpack webpack-cli --save-dev`
<<<<<<< HEAD
=======
>>>>>>> 9ae9138d... added spotify api
`npm init -y`
`npm install react react-dom --save-dev`
`npm install react-router-dom`
`npm install @material-ui/core`
`npm install @material-ui/icons`
`npm install @babel/core babel-loader @babel/preset-react --save-dev`
`npm install @babel/preset-env --save-dev`
`npm install @babel/plugin-proposal-class-properties`
`npm install webpack webpack-cli --save-dev`
<<<<<<< HEAD
=======
>>>>>>> c6e2a7fd... added spotify api
>>>>>>> 9ae9138d... added spotify api
=======
>>>>>>> 6d3401ba... updated views and urls

You will also need both a webpack.config.js and babel.config.json file. Webpack has a template for both configuration files:

1. <https://webpack.js.org/configuration/#options>
2. <https://webpack.js.org/loaders/babel-loader/>

#### Troubleshooting

1. As you continue to build the app and any other project using the Django REST framework, be sure to add paths in the urls.py file at each resepctive level of the project. If you don't you will receive HTTP 404 NOT FOUND warnings and the stack frames will collapse.

2. The frontend will require patience in terms of loading; sometimes it may take a bit for it load, so give it about 5-10 mins before refreshing if nothing pops up initially.

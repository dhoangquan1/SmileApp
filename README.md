# SMILE Application
*This project is a demo for educational purposes as part of course*

Feeling happy? Share it with the world! 
SMILE is a positive and uplifting forum where you can share anything, big or small, that bring you joy.

------------------------
## ⚙️ Technologies Used
-----------------------
[![My Skills](https://skillicons.dev/icons?i=js,html,css,flask,aws,docker,selenium)](https://skillicons.dev)

------------------------
## 🌟 Features
-----------------------
- Post a SMILE: Share what and how much something made you happy. Add a tag to show what your topic is about!
- Like a Post: Engage with others by liking their posts.
- Sort and Filer: Check out what is the most liked post in the forum.
- Authentication: Register an account to join the forum.

------------------------
## 🚀 Getting Started
-----------------------

### Set up dependencies:
- Create a python environment:
    ```
    python -m venv venv
    ```
- Activate the python environment:
    ```
    .\venv\Scripts\activate
    ```
- Download dependencies:
    ```
    pip install -r requirements.txt
    ```

------------------------
## 🖥️ Running the program
-----------------------

### To run this example:
- Start the application with the following command:
    ```
    python smile.py
    ```

### To run the tests:
- run the tests for Model (unittest)
    ``` 
    python -m unittest -v tests/test_models.py 
    ```
- run the tests for routes (pytest)
    ```
    python -m pytest -v tests/test_routes.py
    ```
- run the selenium tests
    * Download the Chrome webdriver for your Chrome browser version (https://chromedriver.chromium.org/downloads); extract and copy it under `C:\Webdriver` folder.
    * Run the SmileApp in a terminal window: 
        ```
            python smile.py
        ```
    * Run the selenium tests
        ```
            python tests/test_selenium.py
        ```

------------------------
## 🙏 Acknowledgements
-----------------------
- Professor Arslan Ay - CS-3733: Software Engineering
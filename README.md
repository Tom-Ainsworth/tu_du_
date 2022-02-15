# TU_DU_

To open links in a new tab,
hold 'Command' + click on Mac, and 'ctrl' on Windows

## Live Site

[Tu_Du_](
  https://tu-du-list.herokuapp.com/)

## Repository

[tu_du_](
  https://github.com/Tom-Ainsworth/tu_du_)

---

## Table of Contents

- [TU_DU_](#TU_DU_)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Table of Contents](#table-of-contents)
  - [Objective](#objective)
  - [Brief](#brief)
    - [Tu Du](#Tu-Du) 
  - [UX &#8722; User Experience Design](#ux--user-experience-design)
    - [User Requirements](#user-requirements)
      - [First Time User](#first-time-user)
      - [Returning User](#returning-user)
      - [Interested Party](#interested-party)
    - [Initial Concept](#initial-concept)
      - [Wireframes](#wireframes)
        - [Desktop](#desktop)
        - [Mobile](#mobile)
      - [Colour Scheme](#colour-scheme)
      - [Typography](#typography)
      - [Imagery](#imagery)
  - [Logic](#logic)
    - [Initial Plan](#initial-plan)
    - [Function Ideas](#function-ideas)
    - [Main Flow](#main-flow)
    - [Create List Flow](#create-list-flow)
    - [JSON Data Structure](#json-data-structure)
  - [Features](#features)
    - [Existing Features](#existing-features)
      - [UX](#ux)
      - [Keywords](#keywords)
    - [Features Left to Implement](#features-left-to-implement)
  - [Data Model](#data-model)
  - [Technologies Used](#technologies-used)
    - [Python Packages](#python-packages)
    - [Other Tech](#other-tech)
      - [VSCode Extensions](#vscode-extensions)
  - [Testing](#testing)
    - [Python Testing](#python-testing)
      - [Manual Python Testing](#manual-python-testing)
        - [Manual Testing Documentation](#manual-testing-documentation)
      - [PEP8 Testing](#pep8-testing)
      - [Other Python Testing](#other-python-testing)
    - [W3C Validator](#w3c-validator)
      - [HTML](#html)
      - [CSS](#css)
    - [JSHint](#jshint)
    - [Lighthouse](#lighthouse)
  - [Bugs](#bugs)
    - [Current](#current)
    - [Resolved](#resolved)
  - [Development](#development)
    - [GitHub](#github)
    - [VSCode](#vscode)
      - [Cloning](#cloning)
      - [Editing](#editing)
    - [Working With Python](#working-with-python)
      - [Venv](#venv)
      - [Packages](#packages)
      - [Debugging](#debugging)
    - [Google Sheets](#google-sheets)
      - [Creating Sheets](#creating-sheets)
      - [API Credentials](#api-credentials)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---



---

## Objective

Design and deploy an interactive To Do List that connects to a local JSON file to read and write user submitted tasks
The project should run in a CLI, deployed via Heroku, using Python.

***This project was created to expand my knowledge of the Python programming language, and to satisfy the requirements for my Portfolio Project 3 assessment at Code Institute***

---

## Brief

### Tu Du

The goal of this app is to provide the user with an easy to use, interactive to do list, to help them be more productive throughout the day.

The app should:

- Be programmatically error free
- Be written using Python
- Handle all user input errors gracefully and appropriately
- Give clear instructions regarding use and valid inputs
- Store user inputted data in a JSON file

---

## UX &#8722; User Experience Design

### User Requirements

Some example user stories which will affect the design

#### First Time User

> *"As a procrastinator, I would like to write down my daily goals to keep track of them and be more productive"*
>
> *"As a tech nerd I want to see if I can create a to do list app that functions properly and validates input"*
>
> *"As a developer new to Python, I would like to build my skills using a command line interface"*

#### Returning User

> *"As a returning user, I would like to create multitple lists to seperate my tasks into categories"*
>
> *"As a returning user, I would like to save my lists for the next time I come and use the app"*
>
> *"As a returning user, I would like to start again from scratch so I can create better lists now I know how to use the app"*

### Initial Concept

I intend to build a to do list inspired by the app Todoist on the Apple App Store. While my app will not be anywhere near as sofisticated, I plan on using either a JSON file to store the lists locally, and then use Python methods to read, write and remove data from the JSON file. To me this works in a similar fashion to connecting with a google sheets API, however having done that in the "Love Sandwiches" guided project, I thought using JSON would be an added challenge as I haven't worked with it as a separate file before.

#### Wireframes

Due to the nature of this project the wireframes are very basic. There is only
one page and the design does not change across any devices, only a change in
content.

##### Desktop

![Desktop Wireframe](readme-content/wireframes/desktop_wireframe.png)

---

## Logic

I used flowcharts and bullet lists to map out how the app would work, so that I had a better idea of what needed to be done, and how I could store and call data. At first I wrote down a list of possible functions, and how they would interact with each other. This formed the base for the project, but as I progressed, I found that extra functions, or different approached needed to be taken. I used the Apples built in [Notes](https://en.wikipedia.org/wiki/Notes_(Apple)) app to do the first list mockup and later [Lucid](https://lucid.app/) to create the flowcharts. It has a variety of symbols and is really intuitive for beginners like me.

### Initial Plan

![Initial Plan](readme-content/images/tu-du-list-flow.png)

### Function Ideas

![Function Ideas](readme-content/images/tu-du-function-ideas.png)

### Main Flow

![Main Flow Chart](readme-content/images/tu-du-main-flowchart.png)

### Create List Flow

![Create Lists Flow Chart](readme-content/images/tu-du-create-list-flowchart.png)

### JSON Data Structure

![JSON Structure](readme-content/images/tu-du-data-structure.png)

---

## Features

### Existing Features

#### UX

> *"As a procrastinator, **I would like to write down my daily goals**"*
- The app allows users to create a list using the "Create New List" option, and then "Add a Tu_Du"
  to add daily goals or other tasks.
> 
> *"As a tech nerd, **I want to create a to do list app that validates input**"*
- When users enter either a list name, or a Tu_Du_ name, code checks for both empty inputs,
  as well as whitespaces such as "      " as an input. It then prints a message and loops back around
  for the user to try again
>
> *"As a developer new to Python, **I would like to build my skills using a command line interface**"*
- By completing this project, I have demonstrated my ability to create a functioning CLI app, which has taken
  a lot of work and research to build.

---

> *"As a returning user, **I would like to create multitple lists to seperate my tasks into categories**"*
- Users can create as many lists as they wish and name them whatever they choose. This could include "shopping",
  "Cleaning" "Work" as a few examples.
>
> *"As a returning user **I would like to save my lists**"*
- The "Save All Lists" menu option commits all lists and tasks to the lists.json file, so on the next load,
  users can continue where they left off.
>
> *"As a returning user **I would like to start again from scratch**"*
- The "Reset All Lists menu option will erase all user created lists, and load the default "Example List". This option
  doesn't require the user to save as it will commit the changes to lists.json as well.

---

### Features Left to Implement

I am really pleased with the final result of this app. To further develop it,
the following features would be very useful:

- Username and/or Password validation
  - Users can currently Save or Reset lists, but should another
  user use the app, they could overwrite the original work.
- Completed Tasks score
  - Users get a message once they have completed a Tu_Du_, but knowing how many they
    have completed in total would create a positive emotional response.
- Mouse Click support
  - Currently the app relies on up/down/enter keys to choose options. PyInquirer does support
    mouseclicks, however with the options being so close together, I opted not to add this yet
    to avoid unwanted user error and frustration.
- Nested lists
  - Should a user want to create a subfolder within a primary list, this could be quite useful.

---

## Data Model

A local JSON file was used to hold the lists. I went through a few iterations before landing on the current design. I haven't used separate JSON files before, and it was something that I wanted to implement on my previous project [Sorting Hat Quiz](https://github.com/Tom-Ainsworth/sorting-hat-quiz). I first thought of using a Google Sheet to hold the data, however as mentioned in the Initial Concept section, I was brand new to using JSON, and therefore opted to challenge myself. The current version makes use of a nested dictionary within the "Lists" list within the lists.json file. The keys are the list names, and their values are a nested list of tasks or Tu-Du's. This made it easy to access the data, and meant that the object never gets too deep.

## Technologies Used

### Python Packages

- [json](https://www.json.org/json-en.html)
  - JavaScript Object Notation, used for displaying and storing all lists and tasks. (See Data Model Section)
- [time](https://docs.python.org/3/library/time.html#time.sleep)
  - sleep: stalls the program for a defined time
- [art](https://pypi.org/project/art/)
  - tprint: Prints blown up strings in various fonts. I chose the default,
    but there are some really interesting ones! 
- [PyInquirer](https://pypi.org/project/PyInquirer/)
  - prompt: Define a list of questions and hand them to "Prompt" which gives
    back a list of "Choices" to be selected. Used for all of the menus.

---

### Other Tech

- *[Python](https://en.wikipedia.org/wiki/Python_(programming_language))*
  - Used to create the content of the app itself.
- *[HTML](https://en.wikipedia.org/wiki/HTML)*
  - Code Institute template files to create the terminal when deployed.
- *[CSS](https://en.wikipedia.org/wiki/CSS)*
  - Code Institute template files to create the terminal when deployed.
- *[JavaScript](https://en.wikipedia.org/wiki/JavaScript)*
  - Code Institute template files to create the terminal when deployed.
- *[Balsamiq](https://balsamiq.com/)*
  - Balsamiq was used to create wireframes for the project.
- *[PEP8 online](http://pep8online.com/)*
  - An online Python code validation service.
- *[Heroku](https://www.heroku.com/)*
  - Used to deploy and host the app
- *[Gitpod](https://www.gitpod.io/)*
  - IDE used for creation and version control via Github.
- *[Tiny PNG](https://tinypng.com/)*
  - Used to compress all images features in this readme.

---

## Testing

### Python Testing

#### Manual Python Testing

The specification within the project requires manual testing. I have performed
multiple tests on the deployed site and during the development stage to ensure
data is handled correctly and all functions are carrying out their intended
actions.

Where user inputs are required, strip() has been used to test for empty inputs,
or whitespace inputs.

All other functions of the app use the Prompt feature, so users can only select from
a list of set inputs.

There were only 2 warnings found, one is a known error. The other is because I used
the "global" keyword within a function. While not ideal practice having global variables
of any kind, the keyword was necessary in order to properly update the json file, and allow
the app to continue operating with the most recent data.

The warnings can be seen here:

![Pylint Warnings](readme-content/validation/pylint_validation.png)

#### PEP8 Testing

The Python files have all been run through
[PEP8 online](http://pep8online.com/). The results are displayed
[here](readme-content/validation.md). No warnings or errors were found.

![PEP* Warning](./readme-content/images/validation/w503-warning.png)

I have chosen to leave the code with the warnings in place. Having consulted
the [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator),
I have found the latest advice is to write code as I have done so. It results
in the code being more reader-friendly.

![Binary operator style explanation](./readme-content/images/validation/binary-operator-line-breaks.png)

#### Other Python Testing

Two Python linters were used during the creation of this project.

- [Flake8](https://flake8.pycqa.org/en/latest/)
- [Pylint](https://pypi.org/project/pylint/)

While I found for the majority of the time they both alerted me to
identical issues. They both had their individual uses to keep my code
looking tidy and running properly.

---

## Bugs

### Current

- Unwanted text appears if user presses enter before prompt appears.
  ![Text Bug](readme-content/images/current_bug.png)

  I'm not completely sure how to fix this, as adding something to catch the error
  would throw up more unwanted text. The bug itself does not negatively affect anything
  major. The first Prompt activates after the opening text finished, which in this instance
  opens the Instructions Page (which I would rather people use initially anyway.)

  If a user pressed enter before any of the other prompts show, it will also choose the first
  option on the list. If this happens when an input is required, it will not enter the blank input.

---

### Resolved

1. App wasn't deploying to Heroku properly
- [Commit: 3177ccf](https://github.com/Tom-Ainsworth/tu_du_/commit/3177ccfec5b04b8f425ab8e78ce2a6b7336a1fb0?diff=split)
  To fix this I had to add the installed packages to `requirements.txt`. I then made sure to do this each time I added
  a new library/package.

2. `QUESTIONS` formerly named `main_menu` only had local scope and so wasn't very repeatable
- [Commit: d9f96d0](https://github.com/Tom-Ainsworth/tu_du_/commit/d9f96d06cba3f91ddf1e96b1c2c438e96c013f4c)
  As mentioned, `main_menu` is now named `questions` to avoid confusion with the `show_main_menu()`.
  Originally this was placed within the function, however I realised it wasn't very repeatable and I was
  having to copy/paste the entire dict to change `choices` key. I opted to make this a global variable, allowing me
  to edit `choices` in various places, and keep the prompts unified throughout the app.

3. Deciding how to read/write to `lists.json`
- [Commit: 705d537](https://github.com/Tom-Ainsworth/tu_du_/commit/705d5375d60261170b19e11057e33c95e32c538d)
- [Commit: 6409c25](https://github.com/Tom-Ainsworth/tu_du_/commit/6409c25528c77c57e77a198f7d117d7eb05af51f)
- [Commit: 4965ebc](https://github.com/Tom-Ainsworth/tu_du_/commit/4965ebce072c8e4f3108e28845b016268ad75844)
- [Commit: 226da97](https://github.com/Tom-Ainsworth/tu_du_/commit/226da975b2db6c0ea8a8e57b5c4626ff3e05400d)
  The above commits all relate to the same issue. As I am new to using JSON files, I went through several ways
  of accessing the data in `lists.json`. At first, I was using `with open()` statements for reading, then writing
  data `Commit: 705d537`. This was a long winded way of doing it, as it wasn't necessary to update the list after each user change.
  I instead finally opted to open the file at the start of the program `Commit: 6409c25`. Then write to it only when necessary, in the
  `save_all_lists()` and `reset_all_lists()` functions. All other manipulation took place within the program, so users
  could still see the changes `Commit: 4965ebc`, `Commit: 226da97`.

---

## Development

The site was made using [GitHub](#GitHub) and [VSCode](#VSCode)

### GitHub

[GitHub Website](https://github.com)

- Sign in to GitHub.
- I used a template created by Code Institute that can be accessed
  [here](https://github.com/DaveyJH/template) and is available for public use
  via the **Use this template** button.

![Use Template](./readme-content/images/development/use-template.png)

*Alternatively*

- Click ![GitHub Icon](./readme-content/images/development/github.png) and select
  **New** from the panel on the left, next to **Repositories**

![New Repository](./readme-content/images/development/new-repo.png)

- Select the template you wish to use

![Select Template](./readme-content/images/development/template.png)

- Give the repository a name and description and then click **Create repository**

![Create Repo](./readme-content/images/development/create-repo.png)

The repository has now been created and is ready for editing

---

### VSCode

[VSCode Website](https://code.visualstudio.com/)

For general information on using GitHub with VSCode see their documentation
[here](https://code.visualstudio.com/docs/editor/github).  
*This section assumes you have successfully linked your GitHub account to the
application.*

#### Cloning

- Open the command panel using your keyboard shortcut or **View** > **Command
  Palette...**

![View>Command](./readme-content/images/development/view-command.png)

- With the command palette open, type *clone* and click **Git: Clone** and then
  **![GitHub Icon](./readme-content/images/development/git-icon.png)Clone from
  GitHub**

![Command Palette](./readme-content/images/development/commands.png)

- Type the GitHub username followed by / and the repository you wish to work on

![Repo Clone](./readme-content/images/development/clone.png)

- Click the repository from the drop-down list and save it in a local directory
  of your choosing

The repository is now ready for development

#### Editing

- The explorer tab enables viewing of the files within the repository

![Explorer](./readme-content/images/development/explorer.png)

- Open files from the explorer tab in the editor window and perform changes as
  necessary

![Editor](./readme-content/images/development/editor-tab.png)

- Save files as appropriate, add, commit and push them. There are multiple ways
  to do this
  - VSCode Source Control
    - Select the **Source Control** tab that looks like a repository branch

    ![Source Control](./readme-content/images/development/source-control.png)

    - Click the **+** sign next to files you wish to add to staged changes

    ![SC Add](./readme-content/images/development/sc-add-commit.png)

    - Type a commit message and click the tick icon to commit

    ![SC Commit](./readme-content/images/development/commit-tick.png)

    - When ready to push your repository back to GitHub click the push/pull icon
      in the bar at the bottom of the application
  
    ![SC Push](./readme-content/images/development/sc-push.png)

    - *I have many keyboard shortcuts set to speed up this process, they are
      configurable within the VSCode settings*

  - Terminal  
  *These steps assume you are in the root directory of your repository and typing
  in the terminal*
    - Type `git add .` and press Enter to add all modified or untracked file

    ![Terminal All](./readme-content/images/development/terminal-add-all.png)

    - Type `git add fileNameHere.extension assets/anotherFileHere.extension` and
      press Enter to add specific files, remembering to include sub-directories
      where necessary
  
    ![Terminal Add](./readme-content/images/development/terminal-add.png)

    - Type `git commit -m "meaningful message here"` to commit your staged files
      with the typed commit message

    ![Terminal Commit](./readme-content/images/development/terminal-commit.png)

    - Type `git push` to push your repository to the remote repository held at
    GitHub

    ![Terminal Push](./readme-content/images/development/terminal-push.png)

    - *There are many other stages to editing, such as branches, git stash,
      reverting commit messages and others. For more information,
      refer to the [git documentation](https://git-scm.com)*

### Working With Python

This section assumes you have python installed on your machine and added to
PATH. *I am unfamiliar with macOS so these steps may be different.*

#### Venv

A virtual environment is advised when working with Python. I chose to use
`venv`.

- With the terminal in the route directory of my project I used
  `python -m venv .venv` to create a virtual environment in the `.venv`
  directory.
- I the used `source .venv/scripts/activate` to enable the virtual environment.
- The `(.venv)` displayed above the current directory show the venv is active.  
  ![Venv active](./readme-content/images/development/venv-active.png)

This allows local installation of packages within the virtual environment and
can help to prevent errors with global installs.

#### Packages

To install all packages within this repo you can run `pip3 install -r
requirements.txt` in the terminal. This installs all packages from the text
file. The text file was created using `pip3 freeze > requirements.txt`.

To install individual packages you need to review the appropriate
documentation for the install command. All packages I have found and used were
installed using something similar to `pip3 install py-getch`. The documentation
files are linked above under the [python packages](#python-packages) heading.

To run a file from the terminal I type `python -m file_name_here`, where
'file_name_here' is the name of the file I wish to run.

It is also possible to run small snippets of python code by typing `python` and
pressing enter. This allows me to create variables and run functions without
saving any data. Using this live python terminal, you can also import files
you have already created by typing `import file_name_here`.

#### Debugging

VSCode has a built in debugger. I set breakpoints at points in my files to
enable me a step by step view of how my variables were being manipulated. This
allowed for quick fault finding and ensuring data is being handled as expected.

- Select breakpoints by clicking to the left of the line number.  
  ![Breakpoint selected](./readme-content/images/development/debug-dot.png)
- Select 'Debug Python File'.  
  ![Run in debug mode](./readme-content/images/development/debug-file.png)
- File will run until a breakpoint is reached. It will pause and highlight the
  selected line before it is carried out.  
  ![Debug paused](./readme-content/images/development/debug-reached.png)
- Step through each line individually or skip through functions as necessary.  
  ![Debug step](./readme-content/images/development/debug-step.png)
- View variables and data as it is being created or manipulated.  
  ![Debug variables](./readme-content/images/development/debug-vars.png)
- Press play to continue to the next breakpoint or stop to end the file.

### Google Sheets

This application uses Google Sheets to store data.

#### Creating Sheets

- Navigate to [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
- Create a Blank sheet.  
  ![Naming google sheet](./readme-content/images/development/sheets-blank.png)
- Edit the sheet name.  
  ![Google sheets name](./readme-content/images/development/sheets-name.png)
- The name used must match the name called in the `open()` method.
  
  ```python
  `GSPREAD_CLIENT.open('example')`
  ```

- Input data if required:
  - *Google Sheets data works differently to most python objects. The 'list'
    of columns and rows starts at an index of 1.*  
  ![Google sheets tokens](
    ./readme-content/images/development/sheets-tokens.png)  
  ![Google sheets scores](
    ./readme-content/images/development/sheets-scores.png)
- Assign 'Named ranges' if necessary:
  - Either highlight the range to be named, right click and select 'Define
    named range' from 'View more cell actions'.  
    ![Google sheets right click naming ranges](
      readme-content/images/development/sheets-right-click-named-range.png)
  - OR Select 'Data' from the toolbar and click 'Named ranges'.  
    ![Google sheets data named ranges](
      readme-content/images/development/sheets-data-name-ranges.png)
  - Named ranges can be viewed via the second option and can be edited if
    needed.  
    ![Google sheets named ranges](
      readme-content/images/development/sheets-ranges.png)
  - Named ranges can be accessed using the `worksheet.range('range_name')`
    method.

    ```python
    import gspread
    SHEET = GSPREAD_CLIENT.open("ci_p3_quiz")
    SCORES_SHEET = SHEET.worksheet("scores")
    current_highscore_values_cells = SCORES_SHEET.range("values")
    ```

- The `gspread` package allows many operations including retrieving, updating
  and adding new data.

#### API Credentials

To allow access from the project to Google Sheets, credentials must be
generated and provided.

- Navigate to the [Google Cloud Platform](https://console.cloud.google.com/)
- Click 'Select a project', this may have an existing project name in place.  
  ![Cloud select a project](
    readme-content/images/development/cloud-select-project.png)
- Click 'NEW PROJECT'.  
  ![Cloud new project](./readme-content/images/development/cloud-new-project.png)
- Give the project a name.  
  ![Cloud project name](
    readme-content/images/development/cloud-project-name.png)
- Click 'CREATE'.  
  ![Cloud create](./readme-content/images/development/cloud-create.png)
- From the project's dashboard, select 'APIs and services' and then
  'Library'.  
  ![Cloud library menu](
    readme-content/images/development/cloud-library-menu.png)
- Search for, and enable, Google Drive API.  
  ![Cloud Google Drive API](
    readme-content/images/development/cloud-google-drive-selection.png)  
  ![Cloud enable](./readme-content/images/development/cloud-enable.png)
- Click 'CREATE CREDENTIALS'.  
  ![Cloud create credentials](
    readme-content/images/development/cloud-create-creds.png)
- Select 'Google Drive API' from the drop down list.  
  ![Cloud API selection](readme-content/images/development/cloud-which-api.png)
- Select 'Application data' from the first set of radio buttons.  
  ![Cloud accessing app data](
    readme-content/images/development/cloud-application-data.png)
- Select 'No, I', not using them' from the second set of radio buttons.  
  ![Cloud not using cloud functions](
    readme-content/images/development/cloud-cloud-functions.png)
- Click 'DONE' and then enter a name and description for the service account
  details.  
  ![Cloud service account details](
    readme-content/images/development/cloud-service-account.png)
- Select a role of 'Editor' from the options available.  
  ![Cloud editor](readme-content/images/development/cloud-editor.png)
- Click 'DONE' to create the service account.
- Click on the service account on the credentials page.  
  ![Cloud edit service account](
    readme-content/images/development/cloud-edit-service-account.png)
- Select 'KEYS' from the menu bar.  
  ![Cloud keys](readme-content/images/development/cloud-keys.png)
- Select 'Create new key' from the 'ADD KEY' menu.  
  ![Cloud create key](readme-content/images/development/cloud-add-key.png)
- Select 'JSON' and click 'CREATE'.  
  ![Cloud JSON option](readme-content/images/development/cloud-json.png)
- The JSON file will be downloaded to your computer. Copy the contents into
  a `creds.json` file within the repository. **Make sure to add this file to
  the `.gitignore` file.**

## Deployment

### Heroku

- Navigate to your [heroku dashboard](https://dashboard.heroku.com/apps)
- Click "New" and select "Create new app".  
  ![New heroku](./readme-content/images/deployment/heroku-new.png)
- Input a meaningful name for your app and choose the region best suited to
  your location.  
  ![Create new app](./readme-content/images/deployment/heroku-create.png)
- Select "Settings" from the tabs.  
  ![Settings tab](./readme-content/images/deployment/heroku-settings.png)
  - Click "Reveal Config Vars".  
    ![Config vars button](
      readme-content/images/deployment/heroku-config-vars.png)
  - Input `PORT` and `8000` as one config var and click add.  
  - Input `CREDS` and the content of your Google Sheet API creds file as another
    config var and click add.  
    ![Config vars values](
      readme-content/images/deployment/heroku-config-vars-values.png)
  - Click "Add buildpack".  
    ![Add buildpack](./readme-content/images/deployment/heroku-add-buildpacks.png)
  - Add "nodejs" and "python" from the list or search if necessary, remember to
    click save.  
    ![Select buildpacks](
      readme-content/images/deployment/heroku-select-buildpacks.png)
  - Python must be the first buildpack. They can be dragged into the correct
    position if needed.  
    ![Buildpacks added](
      readme-content/images/deployment/heroku-buildpacks-added.png)
- Select "Deploy" from the tabs.  
  ![Settings tab](./readme-content/images/deployment/heroku-deploy-tab.png)
  - Select "GitHub - Connect to GitHub" from deployment methods.  
    ![Select GitHub](./readme-content/images/deployment/heroku-select-github.png)
  - Click "Connect to GitHub" in the created section.  
    ![Connect to GitHub](
      readme-content/images/deployment/heroku-connect-github.png)
  - Search for the GitHub repository by name.  
    ![Heroku repo search](./readme-content/images/deployment/heroku-search.png)
  - Click to connect to the relevant repo.  
    ![Heroku connect to repo](
      readme-content/images/deployment/heroku-connect-repo.png)
  - Either click `Enable Automatic Deploys` for automatic deploys or `Deploy
    Branch` to deploy manually. Manually deployed branches will need
    re-deploying each time the repo is updated.  
    ![Heroku deploy branch](
      readme-content/images/deployment/heroku-deploy-branch.png)
  - Click `View` to view the deployed site.  
    ![Heroku view](./readme-content/images/deployment/heroku-view.png)
- The live site can also be accessed from your repo in GitHub from the
  environments section of the repo.
  - Click the link to view deployments history.  
    ![GitHub environments](
    readme-content/images/deployment/github-environments.png)
  - Click `View deployment`. This page also shows all the deployment history.  
    ![GitHub view deployment](
      readme-content/images/deployment/github-view-deployment.png)

The site is now live and operational

---

## Credits

### Content

- The question database and API functionality was obtained through
  [opentdb.com](https://opentdb.com/)
- The terminal function and template for the deployable application was
  provided by [Code Institute](https://codeinstitute.net), with special mention
  to [Matt Rudge](https://github.com/lechien73)

### Media

- The background image was sourced from [pexels.com](https://pexels.com) and
  was provided by [Wendy Wei](
    https://www.pexels.com/@wendywei?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

### Acknowledgements

- Thank you to [Fiona Tracey](https://github.com/fiona-t). I reached out in the
  Code Institute Slack community with a minor issue. Fiona provided a
  wonderfully simple solution to prevent some unused variable warnings as
  detailed below:

  ```Python
  string = "this is a string" # This string was from the KEYWORDS list
  line = ""
  for char in string:
      line += "="      # 'char' variable is unused 
  # Above was my original code to create an underline of '='s for some titles
  # Below is a neater solution that led to a better approach to other code
  # within the repo
  line = "=" * len(KEYWORDS[index])
  ```

- Thank you to [David Bowers](https://github.com/dnlbowers) for saving me from
  having to trawl through previous Slack messages. Within minutes of asking, he
  provided a link to the exact information I was looking for, detailed below.
  He also has some really awesome work available to look through on his GitHub
  profile, well worth a look.

- Thank you to [Matt Boden](https://github.com/MattBCoding) for sharing his
  project. From there I was able to see the easiest way to style my own project
  to give a more pleasing UX. Matt has a fantastic approach to code, I highly
  recommend a review of his work.

- A big thanks to [Jim Morel](https://www.linkedin.com/in/jim-morel/) and many
  more of the Code Institute slack community members. Jim was able to point me
  in the right direction regarding virtual environments on VSCode and has an
  eternally-positive attitude that really helps in many ways.

- A final huge thank you to [Abi Harrison](https://github.com/abibubble.com)
  and [Emanuel Jose Felisberto Dos Santos Moreira Da Silva](
    https://github.com/manni8436),
  *what an amazing name!* With a great attitude to continued development,
  encouragement along the way, and testing whenever it was needed - These
  two continue to make my developer journey thoroughly enjoyable.
  ![Nerd Life](./readme-content/images/nerd-life-text.png)


# Electromagnetic Wave Scattering
Developers: [Noah Templet](https://github.com/w3aseL); [Michael Sheppard III](https://github.com/MilsonCodes); [James Carter](https://github.com/JacobACarter); [Joel  Keller](https://github.com/joelkeller31)\
Research Supervisor: [Stephen Shipman](https://www.math.lsu.edu/~shipman)

## Developer Setup
Install Git
https://git-scm.com/downloads

Install Visual Studio Code
https://code.visualstudio.com/download

Get the code next. In Visual Studio Code, you should see the Explorer view in the left-hand window, if not press `ctrl+shift+P` to open it.  There you should see and click the option `Clone Repository`.  Next, type in the repository URL for the EMWS code when prompted.  For my example, I used my own fork of the code at `https://github.com/awelters/EMWS-2020.git`. Finally, select (or create) the local directory into which you want to clone the project and when prompted make sure to click `Add to Workspace`.

Open the integrated terminal in Visual Studio code by pressing ```ctrl+shift+` ```for the next series of commands.

By default for the EMWS repo the branch of code when cloned is `master`. If for example you wanted to work on the `improve-developer-experience` branch then run the following command:

`git checkout improve-developer-experience`

Install the Python plugin extension to help with IntelliSense with the following command, you should see a success message,
something like "Extension 'ms-python.python' v2023.18.0 was successfully installed":

```code --install-extension ms-python.python```

Download miniconda, ensure path set correctly, in windows easiest to use the installer
https://docs.conda.io/projects/miniconda/en/latest/

Update to the latest version with the following command:

```conda update -n base -c defaults conda```

Create your environment from the environment file with the following command:

```conda env create --file environment.yaml```

Activate your environment to starting using it with the following command:

```conda activate emws```

In Visual Studio Code, press `ctrl+shift+P` to open the command palette. Next, type `Python: Select Interpreter` in the search box. Now, scroll down to where you see the current project and click it, in my case it's `EMWS-2020`.  Finally, select the Python version that includes the `emws` keyword.  By default your now developing in the right emws environment.

If you are not using Conda/Visual Studio Code then take a look at the `environment.yaml` file to see the required version of python and libraries installed.  Your mileage may differ ;)

## Starting the App

### Starting the Frontend
In Visual Studio Code, press `ctrl+shift+D` to open the debugger. Next, in the upper left from the 'RUN AND DEBUG' options select `Python: Frontend (EMWS-2020)`.  Finally, click the play button to run it locally.  This creates a HTTP server in the frontend directory.  You can now open your browser to http://localhost:8000/ to use it. Note: you will also need to start the backend api in order to have the app completely working.

If you are not using Conda/Visual Studio Code and are just running it from the command line with Python already installed using the following commands:

```
cd frontend
python -m http.server
```

### Starting the Backend Api
In Visual Studio Code, press `ctrl+shift+D` to open the debugger. Next, in the upper left from the 'RUN AND DEBUG' options select `Python: Backend API (EMWS-2020)`.  Finally, click the play button to run it locally. You can now open your browser to http://localhost:5000/ to see it is working. Note: you will also need to start the frontend in order to have the app completely working.

If you are not using Conda/Visual Studio Code and are just running it from the command line with Python already installed using the following commands:

```
cd backend/api
python app.py
```

## Debugging the App

### Debugging the Frontend
Your best friend when debugging the frontend is to simply open the frontend in the Chrome browser and then press `F12`.  This will open the Inspector and Debugger tool.  From here you can see console output, network traffic, etc.  You can also put breakpoints in the source.  Details on usage is beyond the scope of this document.

### Debugging the Backend Api

If you are using Visual Studio Code you can simply place a breakpoint anywhere in the backend api python code and when the api runs and hits that line it will break so you can inspect the code. Details on further usage is beyond the scope of this document.

### Debugging a Backend script

If you are using Visual Studio Code, first make sure you open a python script.  Put breakpoints where you'd like.  Next, press `ctrl+shift+D` to open the debugger and then in the upper left from the 'RUN AND DEBUG' options select `Python: Debug File (EMWS-2020)`.  Finally, click the play button to run the python script to debug it. When the script runs and hits those lines it will break so you can inspect the code. Details on further usage is beyond the scope of this document.

## Deployment
[Backend Deployment Instructions](https://docs.google.com/document/d/1Hm3J-an80XWGBYOH-XYcGJwbcKlsgqoGKKTIXb3xzgI/edit?usp=sharing)

## Helpful Conda commands

Save environment for others to use (shallow dependencies) - make sure to remove the `prefix: ...` line
```conda env export --from-history > environment.yaml```

Save environment for others to use (deep dependencies) - make sure to remove the `prefix: ...` line
```conda env export > environment.yml```

Deactivate environment
```conda deactivate```

Remove environment
```conda env remove -n emws```
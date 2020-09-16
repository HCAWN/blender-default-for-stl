# blender_default_for_mesh
Open stl, obj and dae files in Blender rather than 3D Viewer or Paint 3D

## What
Do you open stl and obj files in Blender often?
Are you annoyed at having to open blender and then import models via the internal file browser
Then this is for you.
3o seconds to setup and then you'll be able to double click on stl or obj files to automatically open and import the file into blender

## Usage
- download `.py` and `.bat` files for opening stl files
    - Put them somewhere safe where they won't move
- Ensure `blender` is in the `PATH` variable
    - Search for `Environment Variables` in START and click on "Edit the system environment variables
    - System Properties, opened to the Advanced tab should open up
    - Click `Environment Variables`
    - Select to the `Path` variable in the "User variables for USERNAME" table and click `Edit...`
    - Click new and paste the path location of your `blender.exe` file e.g. `"C:\Program Files\Blender Foundation\Blender\`
    - Okay Save etc. test if you've done it by opening up `CMD` after making the change, entering `blender` and confirming that blender opens.
- Set the `.bat` files as the default application to open the 3D files with
    - Right click on an `STL` or `OBJ` file
    - Open with
    - Choose another app
    - Check `Always use this app to open 'stl' files
    - More apps (at the bottom of the application list)
    - navigate to the `openMeshinBlender.bat` file

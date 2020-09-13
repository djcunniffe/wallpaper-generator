# Wallpaper Generator
Using the Unsplash API to update your desktop wallpaper with a random photo

To use, create a config.ini in the programs root directory like so:

    [API Credentials]
    client_id = 
    client_secret = 
    redirect_uri = 

    [Photo Config]
    orientation = 
    query = 
    featured = 

Obtain your Unsplash API credentials by registering as a developer and add them to the API Credentials section of config file.

To fine tune the photos that are returned, you can specify certain options in the Photo Config section.

- orientation - valid values are (landscape, portrait, squarish)
- query - a search query to use
- featured - either True or False


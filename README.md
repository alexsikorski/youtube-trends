# youtube-trends
Software designed to analyse trending videos and display what tags are popular.

## Language
Python 3.8

## Setup
##### Libraries
Google APIs Client
##### Pip
* pip install --upgrade google-api-python-client
* pip install --upgrade google-auth-oauthlib google-auth-httplib2
##### Note
Download YOUR_CLIENT_SECRET_FILE.json and place in directory, this is done following the api setup tutorial provided by Google.

## Running
1) Run get_data.py, this will produce Json files containing popular YouTube videos with respective meta data.
2) Run transform.py, this extracts the desired analytical data and and simplifies the format for further processing.

*Optional: Run tag_definer.py if tag definitions are outdated and/or you would like to customise them.*
## Author
Alex Sikorski
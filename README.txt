This is a README file.
Bing RSS feed retriever accesses the RSS feed of Bing news everyday at https://www.bing.com/news?format=RSS. This is retrieved as XML, before being processed by this python3 script. All headlines for the daily news is extracted and input into a new file for each day, with the file name simply being the relevant date in ISO format. All the files containing each day's headlines are saved for access at a later time. This script was designed for Linux OS and can be run in the background by the command:
nohup python3 bing-rss-feed.py & 

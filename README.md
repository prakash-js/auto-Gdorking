# auto-Gdorking
Auto-Gdorking is a Python-based tool designed to automate the process of Google Dorking. It helps users efficiently search for sensitive or publicly exposed information using advanced Google search operators. This tool is ideal for penetration testers, security researchers, and anyone interested in exploring the power of Google search operators for advanced querying.

## Features

Automates the process of Google Dorking using API keys and search IDs.

Easily add extra payloads later by simply editing the payload.txt file, with each new payload on a separate line.


Easily configurable API key and search ID setup for accessing Google search results.

# Prerequisites

Before using Auto-Gdorking, you need to register for two services to get the necessary credentials:

###    Google Cloud Console - Custom Search API Key:
    
  Go to [Google Cloud Console](https://console.cloud.google.com/).
    
  Create a new project (or select an existing one).
        
  Enable the Custom Search API for your project.
        
  In the APIs & Services section, go to Credentials, then create an API key.
        
  Copy this API key as you'll need it for the tool.

    
    
    
  ### Google Programmable Search Engine - Search ID:
  Go to [Programmable Search Engine](https://programmablesearchengine.google.com).
        
  Create a new custom search engine (CSE) or use an existing one.
        
  After creating it, you'll get a unique Search ID (CX).
        
  Copy this Search ID, as you'll also need it for the tool.



# First-Time Setup

When running the tool auto-Gdorking.py will prompt you to enter your API key and Search ID. Here's what to expect:


`Do you want to change API or SearchID (Y/N)`


Type Y (Yes) to proceed and enter your API Key and Search ID when prompted:
```
Enter your API Key: your_api_key_here
Enter your Search ID: your_search_id_here
```

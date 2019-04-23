# GitHub Streaming Library
> Class that streams batches of data from GitHub out to the caller

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

Implementation of a class that streams batches of data from GitHub, more exactly it enables its user to get multiple types of data on multiple repositories owned by the same owner/organization using a single API.


## Usage example

In the code it can be seen how can the functions in the class can be called.

e.g. gh = GitHub('moby', ['moby', 'buildkit'], ['issues','pulls'])
	 data = gh.read()
	 while data is not None:
     for result in data:
        print('url: {}\tlen(result): {}'.format(result['url'], len(result['result'])))
     gh.getAvatar()

## Development setup

In order to run this script requests and urllib.request modules are needed. Later on, json will be added in the project.

## Meta

Manea Sebastian – [@linkedin](https://www.linkedin.com/in/sebastian-manea/) – YourEmail@example.com

[https://github.com/yourname/github-link](https://github.com/SebastianMm/)

## Purpose

Project was implemented as part of an interview challenge, it caught my attention due to learning something new, and I will continue to improve on it to strengthen my knowledge about the subject in matter.

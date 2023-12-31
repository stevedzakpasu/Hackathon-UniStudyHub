# Hackathon-UniStudyHub-Backend


This repository houses the server-side components that power our application, and it's built on two powerful frameworks: FastAPI and SQLModel. 
[![PyPI version](https://badge.fury.io/py/fastapi.svg)](https://badge.fury.io/py/fastapi)

<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" style="width: 20%;"></a>
<a href="https://sqlmodel.tiangolo.com"><img src="https://sqlmodel.tiangolo.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

Resource Storage Platform 
Mega
<a href="https://pypi.org/project/mega.py/"><img class="avatar mr-2 d-none d-md-block" alt="Owner avatar" src="https://avatars.githubusercontent.com/u/64530241?s=48&amp;v=4" width="24" height="24"></a>


Front-end repo :point_right: (https://github.com/elitekaycy/unistudyhub-web)

<p align="center">
  <a href="#Introduction">Introduction</a> ▪️
  <a href="#key-features">Key Features</a> ▪️
  <a href="#Install">Install</a> ▪️
  <a href="#Project-Structure">Project Structure</a>▪️
  <a href="#credits">Credits</a> ▪️
  <a href="#related">Related</a>
</p>

## Introduction
This project, aptly named "Bridging the Gap in Educational Materials Sharing Among Students," aims to revolutionize the way students access and share educational resources. In a world where learning materials are abundant but often scattered, our goal is to create a seamless and efficient platform for the exchange of knowledge.
We recognize the challenges students face in accessing diverse learning resources, and we aspire to provide a solution that simplifies this process. By fostering a collaborative environment, we aim to empower students to easily discover, share, and engage with educational content.

## Key Features

* Share Resource with Friends
* Get Access to Educational Materials for FREE
* Create a community of learners and Educators
* Earn Points while you learn


## Install

To clone and run this application, you'll need [Python3.10.5](https://www.python.org/downloads/release/python-3105/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/stevedzakpasu/Hackathon-UniStudyHub.git

# Go into the repository
$ cd Hackathon-UniStudyHub

# create a virtual env annd activate
- on cmd
python -m venv myvenv
myvenv\Scripts\activate

# Install Requirements
$ pip install -r requirements.txt

# manually delete any version of the migration
# add the .env file with the details

# make migrations with
$ alembic revision --autogenerate -m "the message"

# go into the migration file (Under - alembic folder -> versions) and add the import below
import sqlmodel.sql.sqltypes

# upgrade head
$ alembic upgrade head

# Run 
$ uvicorn main:app --reload

# proceed to the url, and authenticate
http://127.0.0.1:8000/docs

```
simple!! :smiley:

## Project-Structure

## Credits

- [Stephen](https://github.com/stevedzakpasu)

- [Frank](https://github.com/dacostafrankaboagye)



This software uses the following open source packages:

- [Uvicorn](https://www.uvicorn.org/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)




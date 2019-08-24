# Maintainers' validation

## Getting started with Docker

In order to continue, you have to install Docker on your computer.
Can be helpful reading a bit about how Docker works and its basic concepts

Install Docker: docs.docker.com/install/ <br>
Docker concepts: docs.docker.com/get-started/

## Running the software

After you have Docker installed, download this project and, on the commandline you enter inside the folder project

To download and enter in the project

    git clone https://github.com/chiaramasci/maintainers_analysis.git
    cd maintainers_analysis

Afterwards, you can run the software with this command:

    docker-compose up

You will have to wait few minutes for the completion of the downloads and the starting up of the software.
The first time you run it will take longer due to some required downloads, but the next time it will not.

Afterwards, in the browser:

    sharing.localhost

to see the online cloud and

    bitz_access.localhost

to have access to the website managing the bitz API (not implemented for these tasks)

## Shut down the software

In order to shut down the software, press CTRL + C on the command line and then execute the following command

    docker-compose down

## The tasks

The following tasks can be completed also in more days and each one separately. <br>
In case there are issues at running the software, do not hesitate to contact me directly. <br>
You can use any resource that you wish to complete the tasks: internet, books, asking people... <br>
The most important thing is that you answer to the survey honestly and the most precisely as possible; by doing this
you are contributing to making software that is based also on the developers' needs.

Remember: the software is the one that is being evaluated, not you. Feel free to make mistakes, not being able to complete the tasks and having doubts... <br>
This means not that you are not able to accomplish it, but that the software and its documentation are not as good as they could be :)

### Zero task: install Docker and answer the first survey

The first task, if you have not done it already, is to install Docker and get the software running.
To do so, follow the paragraphs "Getting started with Docker" and "Running the software".

Important is to then reply to the following surveys (about 15 questions each).
The aim of the first survey is to know which tools are commonly available to the maintainers and the way to receive new information they are more comfortable with.
The aim of the second one is to evaluate the outcome of the installation and the running of the software.

Survey 1: https://forms.gle/3398agKymgiCKBiB7
Survey 2: https://forms.gle/ueatWAVpq9W6KG3f7

### First task: add a Wordpress website

The first task is to add a Wordpress container for making an homepage.
The homepage has to reacheable with the following link: homepage.localhost
You can use the already build Wordpress container on the Docker Hub (https://hub.docker.com/_/wordpress/) and add the code in the docker-compose.yml file

You can then complete the third survey in order to give me a feedback about the experience (4 questions)

Survey 3: https://forms.gle/eGRN4Zz7UKs5kd72A

### Second task: add a Flask custom container

The second task is similar to the previous one, but it might be that you will encounter some differences.
There is the need of a Flask container in order to create an API; your job is to create this container so that when api.localhost/hello is typed is in the browser
on the screen there is "super cool API".

You can then complete the fourth survey in order to give me a feedback about the experience (4 questions)
Survey 4: https://forms.gle/qSM6Lf2aQGaA1wLU7

### Third task: modify a custom container

The last task is related to the container bitz_access already existing.
It is a Flask container which works as an API for a Raspberry Pi.
The aim is to obtain on the screen "Cool, I have done it" when bitz_access.localhost/yes is searched in the browser

You can then complete the fifth survey in order to give me a feedback about the experience (4 questions)
Survey 5: https://forms.gle/3urYEXNig2pYVQk88

## In case of doubts or issues, contact me :)

## I thank you for your help and time

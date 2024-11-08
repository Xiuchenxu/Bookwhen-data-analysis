# Bookwhen-data-analysis

**Bookwhen-data-analysis** Includes two Python applications designed to analyse exported data from the [Bookwhen](https://bookwhen.com/) website. (Built for a dance studio in London)

The Bookings over time analyses ticket sales over time, and helps visualise this data of all classes in one single table. The data is normalised, so day 0 is when each class takes place, and it shows how tickets sell in the days leading up.

Client analysis helps give insights to number of recurring clients, average spending of each client, and number of unique clients (based on how many unique email addresses.)

## Features
- Scrapes event data from Bookwhen using API and generates structured message in English and Chinese that could be sent on WeChat and WhatsApp. Message Generation App.
- Generates social media captions in both English and Chinese, by interacting with ChatGPT via API.


## Usage
Please fill out your API tokens for Bookwhen and ChatGPT inside the code then run the application.
Message generation and Social media caption generation are located in two seperate .py files.

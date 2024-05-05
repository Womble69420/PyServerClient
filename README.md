# Remote Command Execution with Python Sockets

This project demonstrates a simple client-server application for executing remote commands on a Linux server using Python socket programming.

## Features

- Allows the client to send multiple requests concurrently.
- Executes Linux commands on the server and returns the output.
- Handles batch processing of requests on the server.
- Returns response objects in any order within an array.
- Uses JSON for communication between client and server.

## Usage

1. **Run the server:**
   ```bash
   python server.py
   ```
This will start the server listening for incoming connections.

2. **Run the client:**
   ```
   python client.py
   ```
Follow the prompts to enter the number of requests and the commands to execute. The client will send the requests to the server and display the responses.

## Code Structure

  * server.py: Contains the server-side implementation using socket programming. It listens for incoming connections, processes requests, executes commands, and sends back responses.
  * client.py: Contains the client-side implementation using socket programming. It prompts the user to enter commands, sends requests to the server, and displays the responses.

## Requirements

  * Python 3.x
  * Linux environment for server execution

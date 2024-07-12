# MarsRover_ChatGPT
How chatGPT would solve the MCG Mars Rover test

## Project Overview  
The Mars Rover project simulates the movement of a rover exploring a rectangular plateau on Mars. The rover receives a set of instructions that tell it how to explore the plateau. The project is designed to demonstrate the application of object-oriented programming principles and to provide a platform for practicing unit testing.  
  
## Features  
- Simulate rover movements based on commands.  
- Handle multiple rovers on the same plateau.  
- Prevent rovers from moving off the plateau.  
  
## Getting Started  
  
### Prerequisites  
- Python 3.8 or higher  
  
### Setting Up Your Environment  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/KodyFernandes/MarsRover_ChatGPT.git 
   cd MarsRover_ChatGPT
   ```
   
2. (Optional) Set up a virtual environment:
    ```bash
   conda create -n mars_rover_env
    ```
   
3. Install dependencies:
     *Currently no external dependencies are required

### Running the Program
To run the Mars Rover program with an input file:
1. Create an input file or use an existing one in the resources directory. Example of input format:
    ```
        5 5  
        1 2 N  
        LMLMLMLMM  
        3 3 E  
        MMRMMRMRRM
   ```
2. Run the program using:
    ```bash
      python -m src.main < resources/input1.txt 
    ```

### Running Tests
To run automated tests for this project:
1. Navigate to the project root directory.
2. Run the following command
    ```bash
        python -m unittest discover -s tests
   ```
   
## Contributing
Contributions to the Mars Rover project are welcome. Please ensure to update tests as appropriate.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Prompting
### System Message
The following is the system message for the chatGPT instance:

"You are a hyper advanced software engineering AI assistant."


### Prompt
The following is the prompt that was used to generate this application. 

"I have a coding test I would like you to do. Please provide all necessary classes and related code that will solve the problem.

Please provide tests for both happy path and edge case scenarios.

Please provide documentation where necessary.

Here is the problem:

_Pasted the mars rover document_

"
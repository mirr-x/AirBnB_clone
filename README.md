# AirBnB Clone - The Console

![blabla](https://i.ibb.co/ncJ1H6Z/65f4a1dd9c51265f49d0.png)

Welcome to the AirBnB clone project! This project involves building a command interpreter to manage AirBnB objects, creating a simple flow of serialization/deserialization, and implementing a file storage engine.

## Project Overview

The primary goal of this project is to create a command interpreter that allows users to:

- Create new objects (e.g., User, State, City, Place)
- Retrieve objects from a file or database
- Perform operations on objects (e.g., count, compute stats)
- Update attributes of an object
- Destroy an object

## Installation

```
git clone https://github.com/mirr-x/AirBnB_clone.git
```
```
cd AirBnB_clone
```
```
./console.py
```
## Usage

### Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) quit
$

```

The interactive mode allows you to enter commands directly in the console.

### Non-Interactive Mode

```bash
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
$
```

In non-interactive mode, you can pass commands through standard input.

## Supported Commands

## Supported Commands

| Command   | Description                                                  |
| --------- | ------------------------------------------------------------ |
| **create** | Creates a new instance of the specified class.               |
| **show**   | Prints the string representation of an instance.             |
| **destroy**| Deletes an instance that was already created.                |
| **all**    | Prints string representation of all instances or of all instances of a specified class. |
| **update** | Updates an instance attribute if it exists, otherwise creates it. |
| **help**   | Show all commands or display information about a specific command. |
| **quit**   | Exit the console.                                            |
| **EOF**    | Exit the console. (ctrl + d)                                 |

## Commands Usage

Commands usage is as follows:

- **create, destroy, and update commands**: Save changes into a JSON file.

### Examples

```bash
$ ./console.py
(hbnb) create BaseModel
d81b20ec-5b06-42d3-aefe-ea3798892a19
(hbnb) all
["[BaseModel] (d81b20ec-5b06-42d3-aefe-ea3798892a19) {'id': 'd81b20ec-5b06-42d3-aefe-ea3798892a19', 'created_at': datetime.datetime(2022, 10, 30, 22, 39, 14, 426961), 'updated_at': datetime.datetime(2022, 10, 30, 22, 39, 14, 426981)}"]
(hbnb) show BaseModel d81b20ec-5b06-42d3-aefe-ea3798892a19
[BaseModel] (d81b20ec-5b06-42d3-aefe-ea3798892a19) {'id': 'd81b20ec-5b06-42d3-aefe-ea3798892a19', 'created_at': datetime.datetime(2022, 10, 30, 22, 39, 14, 426961), 'updated_at': datetime.datetime(2022, 10, 30, 22, 39, 14, 426981)}
(hbnb) quit
$
```

## Contributors

- mohammed lahrache

## License

This project is licensed under the [MIT License](LICENSE).

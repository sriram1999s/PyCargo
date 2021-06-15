# PyCargo
## A Package Manager for Python, similar to Rust's Cargo

## Functionalities

  - [help](#Help)
  - [new](#Creating-Package)
  - [init](#Initializing directory)
  - [run](#Running)
  - [update](#Updation)
  - [create_toml](#TOML-creation)

## Dependancies

  - python3 or greater
  - pip3 or greater

# Installation

1. Clone the repository
2. Run the install script (install.sh)
3. add this to your shell config file : ```export PATH=$PATH":<enter-path-to-directory>/src```

Test your install by running:
```shell
PyCargo help help
```

Your output should look like this:
```shell
PyCargo, a package manager for python binary applications!

	 help - Woah!! I see what you did there :D
```

# Usage

## Help

lists all command possibilities

```shell
PyCargo help
```

## Creating Package

Creates a new package in the current working directory

```shell
PyCargo new <name>
```

Also creates the following:

  - PyCargo.toml : a file to specify package details and dependencies  

## Initializing directory

Initializes the current working directory as a PyCargo managed directory

```shell
PyCargo init
```

### Make sure to be in a PyCargo managed directory for the following commands!
## Running

Automatically installs necessary packages specified in PyCargo.toml

```shell
PyCargo run
```

Also creates the following:

  - PyCargo.lock : to lock updation/installation of dependencies

## Updation

Explicitly update/install dependancies

```shell
PyCargo update
```

## TOML creation

Creates new toml file

```shell
PyCargo create_toml
```

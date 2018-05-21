# selt example

This is an example of a selt project.

## Installation

1- Clone the selt-example to your local machine.

`
$ git clone git@github.com:kcarcia/selt-example.git
`

2- Install selt. (I recommend installing selt in a virtual environment. I will provide instructions below on how to do this using the [virtualenv command line tool](https://virtualenv.pypa.io/en/stable/installation/). If you do not wish to use a virtual environment, skip to step 2c)

2a- Create a new virtual environment.

`
$ mkvirtualenv selt_test
`

2b- Active the virtual environment.

`
$ source <path_to_virtual_env>/bin/activate
`

2c- Install selt. (Note: selt is not yet on PiPy.)

`
$ pip install "git+https://github.com/kcarcia/selt.git"
`

3- Install the [chrome driver, firefox driver, and gecko driver](https://www.seleniumhq.org/download/). Ensure your ~/.setup.cfg file is pointing to the right driver paths.

4- Run selt.
```
$ cd selt-example
$ selt
```

## Note
* selt is a proof of concept. Therefore, there may be bugs. Please let me know if you have any issues getting this to run.
* Only 1 test is enabled for this example. The delete_email_draft test does not work. The create_email_draft requires a password. I am only giving that password upon request.
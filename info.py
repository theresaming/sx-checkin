# Use this to create your temporary python "install"
# (Assuming that is the correct path to the python interpreter you want to use.)
virtualenv -p /usr/bin/python2.7 --distribute temp-python

# Type this command when you want to use your temporary python.
# While you are using your temporary python you will also have access to a temporary pip,
# which will keep all packages installed with it separate from your main python install.
# A shorter version of this command would be ". temp-python/bin/activate"
source temp-python/bin/activate

# When you no longer wish to use you temporary python type
deactivate

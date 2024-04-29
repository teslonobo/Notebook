# IBM DataScience Capstone

Presentation of my Final Project

## Installing

To install the whole Repo


~~~
git clone https://github.com/teslonobo/Notebook.git
~~~

To install just the Final Project

Step 1: First, clone the repository (this will not checkout any file):

~~~
git clone --no-checkout https://github.com/teslonobo/Notebook.git
~~~

Step 2: Navigate to the repository’s directory:

~~~
cd Notebook
~~~

Step 3: Enable sparse-checkout:

~~~
git sparse-checkout init
~~~

Step 4: Set the directories you want to checkout:

~~~
git sparse-checkout set IBM_DataScienceCapstone

~~~

## Executing Program

You'll find several files and folders but for the most part, it's pretty self-explanatory.

But within you'll find:

    - App
    - Data
    - Notebooks 
    - CapStone.pdf

### App

A Dash app to dynamically display analytical SpaceX data. 

To run the app after installing the repo via git, you'll have to install some dependencies.

#### Environment/Dependencies

Requirements.txt is located in the root of the IBM_DataScienceCapstone directory

Virtual Env

Once you have activated your Venv.

```
pip install requirements.txt

```

### Data

Contains our cleaned data, a template capstone_pptx for our final report, and a db that was created 

### Notebooks

Tasks 1 - 8

A quick note Task 7 is just a template the app is actually in the App directory

## Author

Teslonobo

## Acknowledgements

[Coursera](https://www.coursera.org/professional-certificates/ibm-data-science?)

[Pratiksha Verma](https://www.linkedin.com/in/pratiksha-verma-6487561b1/)

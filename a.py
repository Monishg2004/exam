import streamlit as st

# Function to load markdown content
def load_markdown():
    return """
    # Theory Assignment 1
    ## Title of Assignment 1
    Description and details of the theory assignment 1...

    ---

    # Theory Assignment 2
    ## Title of Assignment 2
    Description and details of the theory assignment 2...

    ---

    # Theory Assignment 3
    ## Title of Assignment 3
    Description and details of the theory assignment 3...

    ---

    # Theory Assignment 4
    ## Title of Assignment 4
    Description and details of the theory assignment 4...

    ---

    # Theory Assignment 5
    ## Title of Assignment 5
    Description and details of the theory assignment 5...

    ---

    # Theory Assignment 6
    ## Title of Assignment 6
    Description and details of the theory assignment 6...

    ---

    # Theory Assignment 7
    ## Title of Assignment 7
    Description and details of the theory assignment 7...

    ---

    # Theory Assignment 8
    ## Title of Assignment 8
    Description and details of the theory assignment 8...

    ---

    # Theory Assignment 9
    ## Title of Assignment 9
    Description and details of the theory assignment 9...

    ---

    # Theory Assignment 10
    ## Title of Assignment 10
    Description and details of the theory assignment 10...
    """

# Set up the Streamlit app
st.title("Theory Assignments")
st.markdown(load_markdown())


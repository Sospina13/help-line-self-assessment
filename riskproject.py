import streamlit as st

# Define the questions and their weights
questions = [
    {
        'question': 'How advanced do you feel your digital channel implementation is?',
        'weight': 0.059,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How complete is your technology stack for digital channels?',
        'weight': 0.084,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'Is your current fundraising strategy enough and steady to cover yout cost in the short and long term?',
        'weight': 0.106,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'To what extent does the helplines maintains confidentiality and ensures the privacy of children seeking help?',
        'weight': 0.155,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How satisfied are you with the timeliness and responsiveness of the helpline service in addressing the needs of the children?',
        'weight': 0.086,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?',
        'weight': 0.091,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How knowledgeable are the helpline staff about the specific issues and challenges faced by children in your country?',
        'weight': 0.055,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?',
        'weight': 0.178,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages (by adults or peers)?',
        'weight': 0.083,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },
    {
        'question': 'How satisfied are you with the accessibility of helplines for children in terms of availability and ease of contact?',
        'weight': 0.104,
        'recomendations': 
        {
            1: 'Recomendation for Question 1 - Answer 1. <br> This is the first recommendation.',
            2: 'Recomendation for Question 1 - Answer 2. <br> This is the second recommendation.',
            3: 'Recomendation for Question 1 - Answer 3. <br> This is the third recommendation.',
            4: 'Recomendation for Question 1 - Answer 4. <br> This is the fourth recommendation.',
            5: 'Recomendation for Question 1 - Answer 5. <br> This is the fifth recommendation.'
        }
    },

    # Add more questions here...
]

# Set background image URL
background_image_url = 'https://e1.pxfuel.com/desktop-wallpaper/188/942/desktop-wallpaper-survey-survey.jpg'

# Streamlit app layout
def app():
    st.title('Helpline Self-Assessment App')
    st.image("https://media.giphy.com/media/g3bKgbTctP1kI/giphy.gif", width=300)
    st.markdown('This app enables online helplines to self-assess by answering 10 relevant questions. It provides actionable recommendations to improve daily operations and enhance the overall experience for children')

    # Set background image
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url("{background_image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display questions and collect answers
    answers = {}
    for i, question in enumerate(questions):
        st.subheader(question['question'])
        answer = st.slider(f'Select your answer for Question {i+1}', min_value=1, max_value=5, step=1, key=f'question_{i}')
        answers[i] = {
            'answer': answer,
            'recomendation': question['recomendations'][answer]
        }

    # Calculate score
    score = sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values()))

    # Display score and recommendations
    st.subheader('Quiz Result')
    st.markdown(f'Your score: {score}')

    st.subheader('Recommendations')
    for i, answer in enumerate(answers.values()):
        st.markdown(f"**Question {i+1}:** {answer['recomendation']}")

# Run the app
if __name__ == '__main__':
    app()
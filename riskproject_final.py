import streamlit as st

# Define the questions and their weights
questions = [
    {
        'question': 'How advanced do you feel your digital channel implementation is?',
        'weight': 0.059,
        'recomendations': 
        {
            1: 'Prioritize enhancing the digital infrastructure by investing in reliable technologies and addressing critical issues. Seek expert guidance and allocate more resources. Develop a clear roadmap for advancement.',
            2: 'Conduct analysis to identify weaknesses. Improve user experience through research and testing. Develop a strategy to address issues. Provide training and monitor KPIs for progress.',
            3: 'Optimize the user interface based on feedback and industry best practices. Implement engaging features and establish partnerships for insights. Update the digital channel based on emerging trends.',
            4: 'Ensure reliability and scalability. Gather user feedback for continuous improvement. Introduce additional support channels. Regularly assess against benchmarks.',
            5: 'Share success stories and invest in research for continuous improvement. Establish a user community. Celebrate achievements to motivate the team. Collaborate with stakeholders to advocate for digital channels in preventing violence against children.'
        }
    },
    {
        'question': 'How complete is your technology stack for digital channels?',
        'weight': 0.084,
        'recomendations': 
        {
            1: 'Prioritize enhancing the infrastructure by investing in necessary components. Conduct a comprehensive review, seek expert guidance, allocate resources, and develop a clear roadmap.',
            2: 'Analyze the technology stack, invest in necessary components, develop a strategy, provide training, and monitor performance.',
            3: 'Optimize the technology stack based on feedback and best practices. Fill missing components, evaluate, refine, establish partnerships, and stay updated.',
            4: 'Expand and enhance the technology stack, assess against benchmarks, update and upgrade, seek feedback, and embrace innovation',
            5: 'Share success stories and best practices, invest in R&D, collaborate with experts, celebrate achievements, and advocate for a complete technology stack.'
        }
    },
    {
        'question': 'Is your current fundraising strategy enough and steady to cover your cost in the short and long term?',
        'weight': 0.106,
        'recomendations': 
        {
            1: 'Prioritize reviewing and revising the current approach. Identify critical gaps and develop a comprehensive plan to address them. Seek expert guidance or consult with organizations experienced in successful fundraising. Explore alternative fundraising avenues and diversify the strategy. Develop a clear roadmap outlining specific steps and milestones for achieving long-term sustainability.',
            2: 'Conduct a thorough analysis of the current fundraising strategy to identify areas for improvement. Enhance the strategy by exploring new fundraising opportunities and diversifying revenue streams. Develop a plan to address short-term funding gaps and ensure a stable financial outlook in the long run. Seek expert advice and stay updated on effective fundraising practices.',
            3: 'Focus on optimizing the existing fundraising strategy based on feedback and best practices. Identify potential areas for improvement and explore innovative fundraising approaches. Establish relationships with potential donors or sponsors and strengthen existing partnerships. Continuously evaluate the performance of the strategy and adapt it to meet short and long-term funding needs.',
            4: 'Expand the fundraising efforts to ensure sufficient coverage of costs in the short and long term. Explore new funding sources and diversify the donor base. Develop a comprehensive fundraising plan with specific targets and milestones. Regularly assess and refine the strategy based on evolving needs and trends. Strengthen relationships with existing donors and explore collaborative fundraising opportunities with other organizations.',
            5: 'Celebrate the success and effectiveness of the fundraising strategy. Share best practices and success stories with other organizations or stakeholders. Continuously innovate and explore new fundraising methods to maintain a steady and sustainable financial outlook. Foster strong relationships with donors and sponsors by recognizing their contributions. Engage in strategic partnerships to amplify fundraising efforts and ensure long-term financial stability.'
        }
    },
    {
        'question': 'To what extent do the helplines maintain confidentiality and ensures the privacy of children seeking help?',
        'weight': 0.155,
        'recomendations': 
        {
            1: 'Conduct a comprehensive review of protocols and policies to identify gaps. Invest in secure technology solutions to protect sensitive information. Provide comprehensive training to staff members on privacy protection and ethical considerations. Develop and enforce strict protocols for handling and storing data. By implementing these measures, the helpline can improve confidentiality and ensure the privacy of children seeking help.',
            2: 'Assess the existing confidentiality measures and identify areas for improvement. Strengthen policies and procedures to ensure the protection of privacy. Enhance the security of data storage and transmission systems to safeguard sensitive information. Provide regular training and guidance to staff members on maintaining confidentiality and complying with privacy regulations. By addressing these aspects, the helpline can enhance its commitment to privacy and confidentiality.',
            3: 'Helpline should focus on optimizing confidentiality and privacy measures based on industry best practices. Continuously review and update policies and protocols to meet evolving standards. Invest in secure technology solutions to protect data and information. Train staff members on privacy principles and encourage a culture of confidentiality within the organization. Regularly assess potential vulnerabilities and address them promptly to maintain a high level of privacy for children seeking help.',
            4: 'Helpline can take additional steps to further enhance confidentiality and privacy. Expand existing measures to ensure robust privacy protection. Regularly update policies to align with the latest privacy regulations and industry standards. Implement advanced encryption and security measures for data storage and transmission. Conduct regular audits and risk assessments to identify any potential privacy gaps. Continuously train and educate staff members on privacy practices and maintain a proactive approach to privacy protection.',
            5: 'Celebrate its strong commitment to confidentiality and privacy. Share best practices and success stories with other organizations or stakeholders to inspire and encourage them to prioritize privacy. Continue to invest in cutting-edge technologies for enhanced data security. Conduct regular independent audits to ensure compliance and identify areas of further improvement. Foster a culture of privacy within the organization and maintain a transparent and open dialogue with users regarding confidentiality measures. These actions will ensure that the helpline maintain the highest level of privacy for children seeking help.'
        }
    },
    {
        'question': 'How satisfied are you with the timeliness and responsiveness of the helpline service in addressing the needs of the children?',
        'weight': 0.086,
        'recomendations': 
        {
            1: 'Prioritize a comprehensive review of current processes and identify areas for improvement. Streamline internal workflows and communication channels to enhance efficiency. Invest in training and capacity building for staff members to respond promptly to the needs of children. Implement robust monitoring and evaluation mechanisms to track response times and identify bottlenecks. Regularly collect user feedback to identify areas for further improvement',
            2: 'Assess the existing timeliness and responsiveness of helpline services and identify areas for enhancement. Streamline processes and communication channels to expedite response times. Provide additional training to staff members on effective and timely service delivery. Implement regular monitoring and evaluation practices to identify and address any delays or inefficiencies. Gather user feedback to gain insights into areas requiring improvement',
            3: 'Focus on optimizing the timeliness and responsiveness of helpline services based on user feedback and industry best practices. Identify potential bottlenecks in the current processes and implement strategies to address them. Enhance communication and coordination among staff members to ensure prompt responses. Regularly evaluate and refine service delivery processes to minimize delays. Implement mechanisms to solicit user feedback and make adjustments accordingly.',
            4: 'Further enhance the timeliness and responsiveness of helpline services. Streamline processes to ensure efficient handling of the needs of children. Provide ongoing training and support to staff members to enhance their skills and responsiveness. Establish clear protocols for prioritizing and addressing urgent cases. Continuously monitor response times and make necessary improvements. Gather regular feedback from users to gauge satisfaction and identify areas for refinement.',
            5: 'Celebrate the high level of satisfaction of the helpline with the timeliness and responsiveness of services. Maintain a culture of continuous improvement by regularly reviewing and refining processes. Provide advanced training to staff members to ensure prompt and efficient service delivery. Utilize technology and automation to expedite response times. Actively seek user feedback and incorporate it into service improvements. '
        }
    },
    {
        'question': 'How confident are you in the overall quality and impact of helpline services for improving the well-being and safety of children?',
        'weight': 0.091,
        'recomendations': 
        {
            1: 'Conduct a thorough review of the helpline services, seeking expertise if necessary, to identify critical gaps and limitations. Develop a strategic plan to revamp the services, incorporating best practices and evidence-based approaches to rebuild confidence and enhance the well-being and safety outcomes for children.',
            2: 'Invest in comprehensive training programs for helpline staff, focusing on areas such as active listening, empathy, trauma-informed care, and cultural sensitivity. Implement ongoing supervision and support mechanisms to ensure the staff feels equipped and empowered to provide effective assistance to callers.',
            3: 'Evaluate the efficiency and effectiveness of the helpline service delivery process. Identify any bottlenecks, streamline procedures, and optimize response times to enhance the user experience and instill greater confidence in the ability of the helpline to address the concerns of children and caregivers effectively.',
            4: 'Develop outreach and awareness campaigns to promote the helpline services among the target audience. Utilize various channels such as social media, schools, community centers, and healthcare providers to increase awareness about the helpline and its role in supporting the well-being and safety of children.',
            5: 'Continuously monitor and evaluate the helpline services to ensure they maintain the highest quality standards. Regularly review protocols, training materials, and performance indicators to identify areas for improvement and implement measures to enhance the effectiveness and impact of the helpline services.'
        }
    },
    {
        'question': 'How knowledgeable is the helpline staff about the specific issues and challenges faced by children in your country?',
        'weight': 0.055,
        'recomendations': 
        {
            1: 'Seek external training and consultation from experts in child welfare and related fields to address any gaps in the knowledge of helpline staff. Engage consultants or organizations specializing in child protection to provide specific training sessions and workshops that focus on challenges faced by children in the country.',
            2: 'Encourage a culture of knowledge sharing and peer learning amongst the helpline staff. Facilitate regular team meetings, case discussions, and sharing of best practices to create a platform for staff to learn from the experiences of each other and to expand their understanding of the issues faced by children in the country.',
            3: 'Foster partnerships and collaborations with subject matter experts in child welfare, mental health, education, and other relevant fields. Establish a network of professionals who can provide guidance, resources, and support to helpline staff, ensuring they stay updated on the latest research, practices, and interventions for addressing the challenges faced by children.',
            4: 'Conduct regular needs assessments to gauge the specific issues and challenges faced by children in the country. Encourage feedback from helpline staff, volunteers, and stakeholders to identify emerging trends and areas where additional training or resources may be required. Use information to further enhance the knowledge base of helpline staff.',
            5: 'Ensure that helpline staff undergoes comprehensive training programs specifically tailored to the issues and challenges faced by children in the country. Provide continuous professional development opportunities, including workshops, seminars, and lectures, to deepen their knowledge and expertise in addressing the unique needs of children.'
        }
    },
    {
        'question': 'To what extent are helpline services tailored to meet the diverse cultural and linguistic needs of children in your country?',
        'weight': 0.178,
        'recomendations': 
        {
            1: 'Conduct frequent audits to assess the extent to which helpline services are meeting the diverse cultural and linguistic needs of children. Gather feedback from service users and stakeholders through surveys, focus groups, and consultations. Use this information to identify gaps and areas for improvement, and implement strategies to enhance the cultural and linguistic responsiveness of helpline services.',
            2: 'Provide ongoing cultural competency training to helpline staff to enhance their understanding of the diverse cultural norms, values, and traditions in the respective country. This should emphasize the importance of respecting and valuing different cultural backgrounds and equip staff with the skills to adapt their communication styles and approaches accordingly.',
            3: 'Foster partnerships with community organizations, cultural associations, and religious institutions to better understand and address the cultural and linguistic needs of children. Conduct outreach programs and awareness campaigns to engage diverse communities and gather feedback on the accessibility and relevance of helpline services. Use this input to make necessary adjustments and improvements.',
            4: 'Offer translation and interpretation services to ensure that children from different linguistic backgrounds can access helpline services effectively. Collaborate with language experts or utilize technology solutions to provide real-time translation support during helpline calls or online interactions. Regularly review the language needs of the target population and update language resources accordingly.',
            5: 'Ensure helpline services are designed and delivered with a strong emphasis on cultural sensitivity and linguistic diversity. Recruit staff members who are fluent in multiple languages prevalent in the country and provide training on cultural competency. Develop and maintain a comprehensive database of resources and support services that cater to the diverse cultural backgrounds of children.'
        }
    },
    {
        'question': 'How effective are helplines in providing age-appropriate guidance and support to children based on their developmental stages (by adults or peers)?',
        'weight': 0.083,
        'recomendations': 
        {
            1: 'Establish mechanisms to gather feedback from children and their caregivers regarding the effectiveness of helpline services in providing age-appropriate guidance and support. Conduct regular evaluations to assess the alignment of services with the needs of children. Use this feedback to make improvements and adjustments to ensure the services remain effective and relevant.',
            2: 'Provide ongoing training to helpline staff on age-related issues, such as cognitive, emotional, and social development. Equip them with the knowledge and skills to identify and respond to the unique challenges faced by children in different age groups. Encourage continuous professional development to stay updated on best practices in age-appropriate guidance and support.',
            3: 'Develop a comprehensive range of age-targeted information resources, including fact sheets, videos, and interactive tools, that address the specific needs and concerns of children at different developmental stages. Ensure these resources are easily accessible through helpline website, online platforms, and other communication channels.',
            4: 'Establish peer support programs where trained peer volunteers, who have undergone appropriate screening and training, provide guidance and support to children within similar age groups. Promote opportunities for children to connect with their peers through helpline services, online platforms, or moderated group discussions to share experiences and seek advice.',
            5: 'Implement a comprehensive framework for providing age-appropriate guidance and support to children based on their developmental stages. Train helpline staff on child development and age-specific issues to ensure they can adapt their communication and support strategies accordingly. Collaborate with child development experts to develop resources, materials, and guidelines specifically tailored to different age groups.'
        }
    },
    {
        'question': 'How satisfied are you with the accessibility of helplines for children in terms of availability and ease of contact?',
        'weight': 0.104,
        'recomendations': 
        {
            1: 'Frequently evaluate the accessibility of helpline services through user feedback, surveys, and data analysis. Identify any barriers or challenges that children may face when trying to access helplines and take proactive measures to address and overcome these obstacles. Continuously strive to enhance the availability and ease of contact to improve overall satisfaction.',
            2: 'Conduct awareness campaigns to educate children, parents, caregivers, and the general public about the availability and ease of contact for helpline services. Utilize various channels, including social media, schools, community centers, and healthcare facilities, to spread the word and ensure that helpline services are widely known and easily accessible.',
            3: 'Improve the ease of contact by developing user-friendly platforms and interfaces for helpline services. Create intuitive websites, mobile applications, and online portals that are easy to navigate, and provide clear instructions on how to initiate contact and access support services.',
            4: 'Expand the accessibility of helplines by offering various communication channels, such as phone, email, live chat, and text messaging. Allow children to choose the method that best suits their preferences and comfort level, ensuring they can easily reach out for help when needed.',
            5: 'Ensure helplines for children are available 24 hours a day, 7 days a week, to provide immediate support and assistance. Implement a robust system that ensures helpline staff are readily accessible and responsive to calls, messages, and inquiries by children.'
        }
    },

    # Add more questions here...
]

# Set background image URL
background_image_url = 'https://e1.pxfuel.com/desktop-wallpaper/188/942/desktop-wallpaper-survey-survey.jpg'

# Streamlit app layout
def app():
    image_url = 'https://pngimg.com/d/un_PNG3.png'  # Replace with the actual URL of the image

    # Display the image with centered CSS styling
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{image_url}" style="width: 60%; height: auto;">'
        f'</div>',
        unsafe_allow_html=True
    )

    
        # Centered title
    st.markdown(
        '<h1 style="text-align: center;">Helpline Self-Assessment App</h1>',
        unsafe_allow_html=True
    )
    
    image_url_2 = "https://media.giphy.com/media/g3bKgbTctP1kI/giphy.gif"
    st.markdown(
        f'<div style="display: flex; justify-content: center;">'
        f'<img src="{image_url_2}" style="width: 70%; height: auto;">'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown('This app enables online helplines to self-assess by answering 10 relevant questions. It provides actionable recommendations to improve daily operations and enhance the overall experience for children.')
    st.markdown('')
    st.markdown('Please answer the following questions by dragging the sliders (1 = weak, 5 = Strong).')

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
    score = round(sum(answer['answer'] * question['weight'] for question, answer in zip(questions, answers.values())), 2)

    # Display score and recommendations
    st.subheader('Quiz Result')
    display_result = st.button("Display Result")

    if display_result:
        # Set the style for the score based on the score range
        score_style = ''
        if score < 2:
            score_style = 'color: red; font-size: 40px; text-align: center;'
        elif score < 4:
            score_style = 'color: orange; font-size: 40px; text-align: center;'
        else:
            score_style = 'color: green; font-size: 40px; text-align: center;'

        # Display the score with the selected style
        st.markdown(f'<p style="{score_style}">Your score: {score}</p>', unsafe_allow_html=True)
        st.subheader('Recommendations')
        for i, answer in enumerate(answers.values()):
            st.markdown(f"**Question {i+1}:** {answer['recomendation']}")


# Run the app
if __name__ == '__main__':
    app()
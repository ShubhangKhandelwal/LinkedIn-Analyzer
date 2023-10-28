<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# Fetch API keys from environment variables
# PROXYCURL_API_KEY = # your Key here
# OPENAI_API_KEY = # your key here

openai.api_key = OPENAI_API_KEY

API_ENDPOINT = 'https://nubela.co/proxycurl/api/v2/linkedin'
HEADERS = {'Authorization': f'Bearer {PROXYCURL_API_KEY}'}
LINKEDIN_PARAMS = {
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}
app = Flask(__name__)
# app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    linkedin_url = request.form.get('linkedin_url')
    linkedin_data = get_linkedin_data(linkedin_url)
    session['linkedin_data'] = linkedin_data  # Store data in session
    return redirect(url_for('question'))


@app.route('/question', methods=['GET', 'POST'])
def question():
    linkedin_data = session.get('linkedin_data')  # Retrieve data from session
    if request.method == 'POST':
        question_text = request.form.get('question')
        answer = run_llm_chain(linkedin_data, question_text)
        return render_template('question.html', answer=answer, linkedin_data=linkedin_data)
    return render_template('question.html', linkedin_data=linkedin_data)


def get_linkedin_data(linkedin_url):
    LINKEDIN_PARAMS['url'] = linkedin_url
    response = requests.get(API_ENDPOINT, params=LINKEDIN_PARAMS, headers=HEADERS)
    return response.json()


def run_llm_chain(result, question):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)

    mytemp = """
    given is the information about someone's LinkedIn profile: {someon}, now you have to answer the following question
    ---
    {question}
    """

    my_prompt_template = PromptTemplate(input_variables=['someon', 'question'], template=mytemp)
    mychain = LLMChain(llm=llm, prompt=my_prompt_template, verbose=True)
    return mychain.run(someon=result, question=question)

if __name__ == '__main__':
    app.run(debug=True)

# linkedin_params =
=======
from flask import Flask, render_template, request, redirect, url_for, session
import requests
import openai
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os

# Fetch API keys from environment variables
# PROXYCURL_API_KEY = # your Key here
# OPENAI_API_KEY = # your key here

openai.api_key = OPENAI_API_KEY

API_ENDPOINT = 'https://nubela.co/proxycurl/api/v2/linkedin'
HEADERS = {'Authorization': f'Bearer {PROXYCURL_API_KEY}'}
LINKEDIN_PARAMS = {
    'extra': 'include',
    'github_profile_id': 'include',
    'facebook_profile_id': 'include',
    'twitter_profile_id': 'include',
    'personal_contact_number': 'include',
    'personal_email': 'include',
    'inferred_salary': 'include',
    'skills': 'include',
    'use_cache': 'if-present',
    'fallback_to_cache': 'on-error',
}
app = Flask(__name__)
# app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    linkedin_url = request.form.get('linkedin_url')
    linkedin_data = get_linkedin_data(linkedin_url)
    session['linkedin_data'] = linkedin_data  # Store data in session
    return redirect(url_for('question'))


@app.route('/question', methods=['GET', 'POST'])
def question():
    linkedin_data = session.get('linkedin_data')  # Retrieve data from session
    if request.method == 'POST':
        question_text = request.form.get('question')
        answer = run_llm_chain(linkedin_data, question_text)
        return render_template('question.html', answer=answer, linkedin_data=linkedin_data)
    return render_template('question.html', linkedin_data=linkedin_data)


def get_linkedin_data(linkedin_url):
    LINKEDIN_PARAMS['url'] = linkedin_url
    response = requests.get(API_ENDPOINT, params=LINKEDIN_PARAMS, headers=HEADERS)
    return response.json()


def run_llm_chain(result, question):
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)

    mytemp = """
    given is the information about someone's LinkedIn profile: {someon}, now you have to answer the following question
    ---
    {question}
    """

    my_prompt_template = PromptTemplate(input_variables=['someon', 'question'], template=mytemp)
    mychain = LLMChain(llm=llm, prompt=my_prompt_template, verbose=True)
    return mychain.run(someon=result, question=question)

if __name__ == '__main__':
    app.run(debug=True)

# linkedin_params =
>>>>>>> main

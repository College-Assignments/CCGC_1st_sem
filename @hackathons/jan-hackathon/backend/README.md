# For Mac:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```
# For Windows:
```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
 
# To send email
1. Go to your Google Account settings.
2. Click on "Security"
3. Under "Signing in to Google," click on "App Passwords"
4. Select "Other (Custom Name)"
5. Enter a name for the application you are using to send email (e.g. "Python Script").
6. Click on "Generate"
7. The App Password will be displayed. Use this password in the script instead of your regular password.
1. go to https://beta.openai.com/account/api-keys > Top right corner > View API keys
2. Create new secret key
3. Copy the key to .env in this format OPENAI_API_KEY=sk-fxlzrsVQsoDs11tzlxxxxxxxxxxx
Reference: 
https://github.com/openai/openai-python
https://beta.openai.com/docs/api-reference/introduction


# To use OpenAI API
1. go to https://beta.openai.com/account/api-keys > Top right corner > View API keys
2. Create new secret key
3. Copy the key to .env in this format OPENAI_API_KEY=xxxxxx
Reference: 
https://github.com/openai/openai-python
https://beta.openai.com/docs/api-reference/introduction
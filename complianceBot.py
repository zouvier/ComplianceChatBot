import streamlit as st
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


compliance_template = "./complianceTemplates/anyTaskCompliance.txt"




def complianceChecker(_media):
    with open(compliance_template) as comp_temp:
        prefix = f'''
        You are a compliance expert at a top 100 company and are tasked with making sure the given media is compliant with company policy. 
        here is the copy of the company policy: {comp_temp.readlines()}.
         
        check and verify that the following media is compliant. please make sure if the letters are properly capitalized
        Media:{_media}'''

    return prefix



def generate_output(prompt, temperature=1, model="gpt-4-0613"):
    """Generate output using the OpenAI API."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            n=1,
            stop=None,
            temperature=temperature
        )
        message = response.choices[0].message.content
        return message
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def main(_media):
    complianceReturned = complianceChecker(_media)
    holder = generate_output(complianceReturned)
    
    print("TEST:"+holder)
    return holder
    # return holder

    



 


CompliantHolder = ["Explore thousands of Tasks at AnyTask.com",
           "Explore thousands of Sellers at AnyTask.com",
           "AnyTask.com is a freelance platform.",
           "This is AnyTask.com",
           "AnyTask.com"] 
NotCompliantHolder = ["Explore thousands of tasks at anytask",
                      "Explore thousands of sellers at anytask",
                      "anytask is a marketplace.",
                      "We are Anytask.com",
                      "Anytask.com"]






st.title("Compliance Bot")
input_text = st.text_area("Enter the media here:", height=300)
print("TEST!:"+input_text)
if st.button("Submit"):
    result = main(input_text)
    st.markdown(f"**Result:**\n{result}")

# st.file_uploader()
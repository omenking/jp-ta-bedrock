import os
import json
import streamlit as st
import boto3
from dotenv import load_dotenv
load_dotenv()

bedrock = boto3.client('bedrock-runtime')

# If we were doing streaming....
#def stream(resp):  
# full_response = ""
# for event in resp.get('stream'):
#   if 'messageStart' in event:
#     print("Response started:", event['messageStart']['role'])
#   elif 'contentBlockDelta' in event:
#     chunk = event['contentBlockDelta']['delta'].get('text', '')
#     full_response += chunk
#     print(chunk, end='', flush=True)  # Print chunks as they arrive
#   elif 'messageStop' in event:
#     print("\n\nResponse completed. Stop reason:", event['messageStop']['stopReason'])
#   elif 'metadata' in event:
#     print("\nMetadata:", json.dumps(event['metadata'], indent=2))  
# return full_response  

def query_bedrock(chat_history):
  # open the system prompt file on every query
  # so we can dynamically change it.
  with open('./prompts/system_prompt.md', 'r') as file:
    system_prompt = file.read()

  model_id = os.environ.get("MODEL_ID")
  if not model_id:
    st.error("MODEL_ID not found in environment variables.")
    return "Error: MODEL_ID is not set."

  # Convert messages format to expected format for Amazon Bedrock
  messages = []
  for msg in chat_history:
    messages.append({
      "role": msg["role"],
      "content": [{"text": msg["content"] }]
    })

  #resp = bedrock.converse_stream(
  resp = bedrock.converse(
    modelId=model_id,
    messages=messages,
    system=[{"text": system_prompt}]
  )
  #text = stream(resp)
  text = resp['output']['message']['content'][0]['text']
  print(text)
  return text

st.title("Chat with Bedrock Agent")

# Set the default messages state to an empty array
if "messages" not in st.session_state:
  st.session_state.messages = []

# Render the markdown content to HTML
for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    st.markdown(msg["content"])

if prompt := st.chat_input("Say something"):
    # append the user's input to the message history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # and render it as markdown content.
    with st.chat_message("user"):
      st.markdown(prompt)
    
    with st.chat_message("assistant"):
      # if we were doing streaming....
      message_placeholder = st.empty()
      #full_response = ""
      #response = query_bedrock(st.session_state.messages)
      
      #for chunk in response.split():
      #  full_response += chunk + " "
      #  message_placeholder.markdown(full_response + "▌")
      
      #message_placeholder.markdown(full_response)
      full_response = query_bedrock(st.session_state.messages)
      message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

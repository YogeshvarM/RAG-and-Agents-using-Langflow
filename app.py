import streamlit as st 
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "10e7b18a-333b-434c-8ad5-aecb61d2817e"
FLOW_ID = "9c5dfd71-adf9-4a6c-96ab-5b8f98b9571f"
APPLICATION_TOKEN = os.environ.get("APPLICATION_TOKEN")
ENDPOINT = "Customer" # You can set a specific endpoint name in the flow settings

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# def main():
#     st.title("Chat Interface")
    
#     message = st.text_area("Message", placeholder="Ask something...")
    
#     if st.button("Run Flow"):
#         if not message.strip():
#             st.error("Please enter a message")
#             return
    
#         try:
#             with st.spinner("Running flow..."):
#                 response = run_flow(message)

#             response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
#             st.markdown(response)
#         except Exception as e:
#             st.error(str(e))

def main():
    st.title("Chat Interface")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "How can I help you?"}
        ]
    
    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    # Chat input
    if message := st.chat_input():
        
        print(message)
        print(type(message))
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": message})
        st.chat_message("user").write(message)
        try:
            print("hey bro")
            response = run_flow(message)
            print(response)
            response_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            st.chat_message("assistant").write(response_text)
                
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()

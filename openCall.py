from langchain_openai.llms import OpenAI                                                             
from dotenv import load_dotenv

def get_openai_api_key():
    """
    Loads the OpenAI API key from the environment or a .env file.
    Raises an error if not found.
    """
    load_dotenv()  # Load environment variables from .env if present
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Please set it in your environment or .env file.")
    
    return api_key

                                                                                     
# Initialize the language model                                                                  
llm = OpenAI(api_key="your_openai_api_key")                                                      
                                                                                                  
 # Use the language model to generate text                                                        
prompt = "Once upon a time"                                                                      
response = llm(prompt)                                                                           
                                                                                                  
print(response)                                                                                  



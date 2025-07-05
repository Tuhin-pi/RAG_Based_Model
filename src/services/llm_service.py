from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from core.config import settings


class LLMService:

    def __init__(self):
        load_dotenv()
        self.__chatmodel_openai=ChatOpenAI(model='gpt-4o',
                             temperature=0.2)
        # chatmodel_anthropic=ChatAnthropic()

        self.__embeddingmodel_openai = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=settings.VECTOR_DIMENSION)

    def getChatModel(self,provider:str):
        if(provider=='OpenAI'):
            return self.__chatmodel_openai
        
        else:
            return None 
        
    def getEmbeddingModel(self,provider:str):
        if(provider=='OpenAI'):
            return self.__embeddingmodel_openai
        else:
            return None
        

llmservice=LLMService()

    

    

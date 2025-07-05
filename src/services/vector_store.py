from abc import ABC, abstractmethod
from langchain_community.vectorstores import Chroma
from uuid import uuid4
from core.config import settings
from .llm_service import llmservice

class BaseVectorStore(ABC):
    @abstractmethod
    def __init__(self):
        self.addStatus=False
        self.deleteStatus = False
        self.retriveStatus = False
        self.description = None
        
    @abstractmethod
    def add_Documents(self,documents:list):
        pass
    @abstractmethod
    def as_Retrever(self,query:str,video_id:str):
        pass
    # @abstractmethod
    # def similarity_search_by_vector(self,query:str,video_id:str):
    #     pass
    @abstractmethod
    def delete(self,video_id:str):
        pass

class ChromaVectorStore(BaseVectorStore):
    def __init__(self,provider:str):
        embedder = llmservice.getEmbeddingModel(provider=provider)
        self.vector_store =Chroma(collection_name=settings.VECTOR_COLLECTION,
                             persist_directory=".\YoutubeTranscript",
                             embedding_function=embedder)
        
    def add_Documents(self, documents):
        try:
            uuids = [str(uuid4()) for _ in range(len(documents))]
            self.vector_store.add_documents(documents=documents,ids=uuids)
            self.addStatus = True
        except Exception as e:
            self.description = str(e)
        return {'status':self.addStatus,
                'description':self.description}
    
    def as_Retrever(self, query, video_id):
        try:
            retrived_documents = self.vector_store.as_retriever(query,search_type = 'mmr',filter = {'video_id':video_id})
            self.retriveStatus = True
        except Exception as e:
            self.description = str(e)

        return {'status':self.retriveStatus,
                'description':self.description,
                'documents':retrived_documents}
    # def similarity_search_by_vector(self, query, video_id):
    #     try:
    #         retrived_documents = self.vector_store.similarity_search_by_vector(query,,filter = {'video_id':video_id})
    #         self.retriveStatus = True
    #     except Exception as e:
    #         self.description = str(e)

        # return {'status':self.retriveStatus,
        #         'description':self.description,
        #         'documents':retrived_documents}

    def delete(self, video_id):
        try:
            self.vector_store.delete(where={'video_id':video_id})
            self.deleteStatus = True
        except Exception as e:
            self.description=str(e)
        return {'status':self.addStatus,
                'description':self.description}


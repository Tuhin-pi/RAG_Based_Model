from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from core import settings
from services.llm_service import llmservice


class TextSpliter:
    def __init__(self):
        self.textspliter=RecursiveCharacterTextSplitter(separators=settings.CHUNK_SEPARATORS,chunk_size=settings.CHUNK_SIZE
                                                        ,chunk_overlap=settings.CHUNK_OVERLAP)
        self.statusFlag=False
        self.documents=None
        self.Description=None
        
        

    def splitText(self,transcript:str,video_id:str)->dict:
        if transcript:
            try:
                splitted_text = self.textspliter.split_text(transcript)
                self.documents = self.textspliter.create_documents(splitted_text,metadatas=[{"video_id":video_id} for _ in splitted_text])
                self.statusFlag=True
            except Exception as e:
                self.Description=str(e)
        return {"statusFlag":self.statusFlag,
                "video_id":video_id,
                "documents":self.documents,
                "Description": self.Description}
    
class documentEmbeder:
    def __init__(self,provider:str):
        self.embedder=llmservice.getEmbeddingModel(provider)
        self.embeddedDocument=None


    def embedde_document(self,document):
        texts = [doc.page_content for doc in document]
        metadatas=[doc.metadata for doc in document]
        vectors=self.embedder.embed_documents(texts)

        self.embedde_document = [Document({'page_content':text,'vector':vector, 'metadata':metadata} for 
                                 text,vector,metadata in zip(texts, vectors, metadatas))]
        
        return self.embedde_document
        
    
    
textspliter=TextSpliter()

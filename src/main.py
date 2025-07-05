from core import settings
from services.youtube_service import youtubeService
from services.embedding_service import textspliter, documentEmbeder
from services.llm_service import llmservice


transcript=youtubeService.script_loader(video_link=r'https://www.youtube.com/watch?v=2C8zYFArnKY&ab_channel=Ruhi%C3%87enet')
doc=textspliter.splitText(transcript=transcript['transcript'],video_id=transcript['video_id'])

documents = doc['documents']

embedder = documentEmbeder('OpenAI')

embeded_documents=embedder.embedde_document(documents)

print(embeded_documents[0])



# print(doc['documents'][10])

# model=llmservice.getChatModel('OpenAI')
# result=model.invoke("Hi Who are you?")
# print(result.content)
# s="ansdkjd"
# if s:
#     print("ok")
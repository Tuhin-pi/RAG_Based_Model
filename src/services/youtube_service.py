import re
from youtube_transcript_api import YouTubeTranscriptApi
class YoutubeService:
    def __init__(self):
        self.transcript=""
        self.statusFlag = True
    def script_loader(self,video_link:str)->dict:
        """
        Loading Youtube Transcript

        Args:
            "video_link" : string

        Returns:
            Dict: {"statusFlag":...,
                "video_id":...,
                "transcript":...,
                "Description": ...}.
        """
        
        Description = "Transcrpit Using Google Transcript API"
        match = re.search(r"v=([a-zA-Z0-9_-]{11})", video_link)
        VideoId = match.group(1) if match else None
        try:
            transcript_chunk = YouTubeTranscriptApi.get_transcript(video_id=VideoId,languages=["en","hi"])
            if transcript_chunk:

                self.transcript =  "".join(chunk["text"] for chunk in transcript_chunk)

        except Exception as e:
            self.statusFlag = False
            Description = "Transcript not available"

        return {"statusFlag":self.statusFlag,
                "video_id":VideoId,
                "transcript":self.transcript,
                "Description": Description}
    
youtubeService=YoutubeService()
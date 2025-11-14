import requests
from typing import Dict

class ArtInstituteAPI:
    BASE_URL = "https://api.artic.edu/api/v1"
    
    @staticmethod
    def search_artworks(query: str = "", page: int = 1, limit: int = 12) -> Dict:
        """Search for artworks"""
        params = {
            'q': query,
            'page': page,
            'limit': limit,
            'fields': 'id,title,artist_display,date_display,image_id,thumbnail'
        }
        response = requests.get(f"{ArtInstituteAPI.BASE_URL}/artworks/search", params=params)
        return response.json()
    
    @staticmethod
    def get_artwork(artwork_id: int) -> Dict:
        """Get a specific artwork by ID"""
        response = requests.get(f"{ArtInstituteAPI.BASE_URL}/artworks/{artwork_id}")
        return response.json()
    
    @staticmethod
    def get_image_url(image_id: str, size: str = "843") -> str:
        """Generate IIIF image URL"""
        if not image_id:
            return ""
        return f"https://www.artic.edu/iiif/2/{image_id}/full/{size},/0/default.jpg"
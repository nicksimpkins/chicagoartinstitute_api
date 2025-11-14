from django.shortcuts import render
from django.http import JsonResponse
from .services import ArtInstituteAPI

def home(request):
    """Main page with search interface"""
    return render(request, 'home.html')

def search_artworks(request):
    """API endpoint for searching artworks"""
    query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    api = ArtInstituteAPI()
    results = api.search_artworks(query, page)
    
    # Process results to include image URLs
    if 'data' in results:
        for artwork in results['data']:
            if artwork.get('image_id'):
                artwork['image_url'] = api.get_image_url(artwork['image_id'])
    
    return JsonResponse(results)

def artwork_detail(request, artwork_id):
    """View for a single artwork"""
    api = ArtInstituteAPI()
    artwork = api.get_artwork(artwork_id)
    
    # Add image URL
    if artwork.get('data', {}).get('image_id'):
        artwork['data']['image_url'] = api.get_image_url(
            artwork['data']['image_id'], 
            size="1686"
        )
    
    return render(request, 'detail.html', {'artwork': artwork['data']})
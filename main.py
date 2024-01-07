import flickrapi
api_key = 'd1923e858f167569488c4a12cfefd399'
api_secret = '7d22b25f1c64f5f9'
flickr = flickrapi.FlickrAPI(api_key,api_secret, format='parsed-json')

photos = flickr.photos.getPopular(per_page=20)

photo_to_post = photos['photos']['photo'][0]  # Select the first photo
photo_id = photo_to_post['id']


try:
    blog_id = 'iamarshbajaj18'
    title = 'Blog Post Title'
    description = 'Blog post description...'
    response = flickr.blogs.postPhoto(blog_id=blog_id, photo_id=photo_id, title=title, description=description)

    if response.attrib['stat'] == 'ok':
        print("Photo posted to blog successfully!")
    else:
        print("Error posting photo:", response.attrib['code'], response.attrib['message'])
except flickrapi.exceptions.FlickrError as e:
    print("Flickr API error:", e)
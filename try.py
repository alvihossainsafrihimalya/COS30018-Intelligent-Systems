from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://www.example.com')
print(response.html.text[:100])  # Print the first 100 characters of the page

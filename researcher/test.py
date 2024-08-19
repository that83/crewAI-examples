# Import the function from the module
from tools.browser_tools import BrowserTools

# Define a list of URLs to be passed to the function
websites = "https://www.example1.com"
urls = [
    'https://www.simform.com/blog/microservices-framework/',
    'https://www.clariontech.com/blog/5-best-technologies-to-build-microservices-architecture',
    'https://www.serverless.direct/post/top-10-microservices-frameworks',
    'https://insights.sei.cmu.edu/blog/8-steps-for-migrating-existing-applications-to-microservices/'
]
urls = [
    "https://www.simform.com/blog/microservices-framework/",
    "https://www.clariontech.com/blog/5-best-technologies-to-build-microservices-architecture",
    "https://www.serverless.direct/post/top-10-microservices-frameworks",
    "https://insights.sei.cmu.edu/blog/8-steps-for-migrating-existing-applications-to-microservices/"
]
# Assuming the expected schema requires a key 'urls' that maps to the list of websites
#input_data = {
#    "urls": websites  # Use the list of websites here
#}

# Call the function with the dictionary
result = BrowserTools.scrape_and_summarize_website(urls)

# Print the result to verify the function's output
print(result)
# Call the function with the list of URLs
#result = BrowserTools.scrape_and_summarize_website(websites)

# Print the result to verify the function's output
#print(result)
from urllib.request import urlopen, Request
from http.client import HTTPResponse
from time import sleep
from json import dumps

def main():
    urls = [
        ["http://127.0.0.1:5000/posts", "POST", {
                    "title": "My First Blog Post",
                    "content": "This is the content of my first blog post.",
                    "category": "Technology",
                    "tags": ["Tech", "Programming"]
                }],
        ["http://127.0.0.1:5000/posts/", "PUT", {"title": "Title", 
                                                 "content": "example content", 
                                                 "category": "category example", 
                                                 "tags": ["yabadabado"]
                                                 }
         ],
        # ["http://127.0.0.1:5000/posts/", "DELETE", None],
    ]
    
    counter = 35
    while True:
        for test_case in urls:
            data = None
            url = test_case[0]
            
            if test_case[1] in ["POST", "PUT"]:
                data = dumps(test_case[2]).encode()
            
            if test_case[1] not in ["POST"]:
                url = f"{test_case[0]}{str(counter)}"
                print(f"{test_case[0]}{str(counter)}")
                counter+=1
            
            try:
                request = Request(url, method=test_case[1], data=data)
                request.add_header("Application", "application/json")
                request.add_header("Authorization", "Bearer 0")
                
                with urlopen(request) as Response:
                    if isinstance(Response, HTTPResponse):
                        print(Response.headers)
            except Exception as e:
                print(e)
            
            
        sleep(3.0)
    
if __name__ == "__main__":
    main()
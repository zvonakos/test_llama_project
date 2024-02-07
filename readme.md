1. pip install -r requirements.txt
2. python app.py 
3. http://127.0.0.1:8080/add_document POST body:{
	"filename": "flasks.txt",
    "content": "If a syntax error is already present when calling flask run, it will fail immediately and show the traceback rather than waiting until the site is accessed. This is intended to make errors more visible initially while still allowing the server to handle errors on reload."
}
4. http://127.0.0.1:8080/question?question=when will it fail immediately? GET
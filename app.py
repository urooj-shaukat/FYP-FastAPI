from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

#function to get updated file
def read_file(file):
    content = ""
    with file.file:
        content = file.file.read().decode("utf-8")
    return content

def vectorize(text):
    return TfidfVectorizer().fit_transform(text).toarray()

#similarity score finder
def similarity(doc1, doc2):
    return cosine_similarity([doc1, doc2])

def write_similarity_details(file_a, file_b, similarity_score, similar_content):
    return {
        "similarity": round(similarity_score, 3),
        "similarity_percentage": round(similarity_score * 100, 3),
        "similar_content": similar_content,
        "file_a_content": file_a,  # Include file_a content in the response
    }

def check_plagiarism(file_a_content, file_b_content):
    vectors = vectorize([file_a_content, file_b_content])

    sim_score = similarity(vectors[0], vectors[1])[0][1]
    if sim_score >= 0:
        similar_content = find_similar_content(file_a_content, file_b_content)
        return write_similarity_details(file_a_content, "File B", sim_score, similar_content)

    return {}

def find_similar_content(content_a, content_b):
    words_a = set(content_a.split())
    words_b = set(content_b.split())
    common_words = words_a.intersection(words_b)
    return ' '.join(common_words)

@app.post("/get_plagiarism")
async def get_plagiarism(file_a: UploadFile = File(...), file_b: UploadFile = File(...)):
    file_a_content = read_file(file_a)
    file_b_content = read_file(file_b)

    result = check_plagiarism(file_a_content, file_b_content)
    return JSONResponse(content=result, status_code=200)

# Dependency for handling CORS (if needed)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
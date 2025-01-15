from fastapi import FastAPI, File, UploadFile
import uvicorn
from main import classify_image  # Import the function from Step 1

app = FastAPI()

@app.post("/classify/")
async def classify(file: UploadFile = File(...)):
    with open("uploaded_image.jpg", "wb") as image_file:
        image_file.write(await file.read())
    result = classify_image("uploaded_image.jpg")
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

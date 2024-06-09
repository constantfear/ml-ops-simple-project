import os
from fastapi.responses import FileResponse
from datetime import datetime
from src import preprocess, scorer
import shutil
from fastapi import FastAPI, File, UploadFile


app = FastAPI(
    title="Simple Ml-Ops project",
    version="0.1.0",
)


@app.post("/upload")
def get_scores(file: UploadFile = File(...)):

    filename = file.filename
    # Store imported file locally
    new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
    save_location = os.path.join('input', new_filename)

    try:
        with open(save_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as ex:
        print(ex)

    preprocessed_df = preprocess.import_and_prepare_data(save_location)

    # Run scorer to get submission file for competition
    submission = scorer.make_pred(preprocessed_df, save_location)

    predictions = submission['preds'].to_list()

    submission.to_csv(save_location.replace('input', 'output'), index=False)

    return {"filename": new_filename, "predictions": predictions}


@app.get("/download/{filename}")
def download_file(filename: str):
    file_location = f"output/{filename}"
    if os.path.exists(file_location):
        return FileResponse(path=file_location, filename=filename)
    return {"error": "File not found"}


@app.get("/feature_importances/{n}")
def top_n_feature_importances(n: int):
    top_n_features = scorer.get_feature_importances(n)
    return {"features": top_n_features}

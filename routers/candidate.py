"""
    Candidate router

"""

import io
from uuid import uuid4, UUID
import bson
import pandas as pd
from fastapi import APIRouter, status, Security
from fastapi.responses import JSONResponse, StreamingResponse
from core.schemas import CandidateSchema, CandidateReadSchema, CandidateUpdateSchema
from core.database import candidates
from core.security import get_current_active_user

router = APIRouter()

@router.post("/")
async def create_candidate(
    candidate: CandidateSchema, _ = Security(get_current_active_user)
    ) -> CandidateReadSchema:
    """
        Create candidate

        - **first_name**: Candidate first name (str)
        - **last_name**: Candidate last name (str)
        - **email**: Candidate email (str)
        - **career_level**: Candidate career level (str)
        - **job_major**: Candidate job major (str)
        - **years_of_experience**: Candidate years of experience (int)
        - **degree_type**: Candidate degree type (str)
        - **skills**: Candidate skills (list)
        - **nationality**: Candidate's nationality (str)
        - **city**: Candidate's city (str)
        - **salary**: Candidate's salary (int)
        - **gender**: Candidate's gender (str)
    """

    # Check if candidate exists
    if candidates.find_one({"email": candidate.email}):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Candidate already exists"}
            )

    uuid = bson.Binary.from_uuid(uuid4())
    document = {"uuid": uuid, **candidate.dict()}
    candidates.insert_one(document)
    return document


@router.get("/generate-report/", status_code=status.HTTP_200_OK)
async def generate_candidate_csv(_ = Security(get_current_active_user)) -> StreamingResponse:
    """
        Generate csv file of all candidates!
    """
    # convert all candidates to csv
    df = pd.DataFrame(list(candidates.find()))
    stream = io.StringIO()
    df.to_csv(stream, index=False)

    response = StreamingResponse(
        iter([stream.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=candidates.csv"
        }
    )

    return response


@router.get("/{uuid}")
async def get_candidate(uuid: UUID, _ = Security(get_current_active_user)) -> CandidateReadSchema:
    """
        Get candidate

        - **uuid**: Candidate UUID (str)
    """
    document = candidates.find_one({"uuid": bson.Binary.from_uuid(uuid)})
    if document:
        return document
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Candidate not found"}
    )

@router.put("/{uuid}")
@router.patch("/{uuid}")
async def update_candidate(
    uuid: UUID,
    candidate: CandidateUpdateSchema,
    _ = Security(get_current_active_user)) -> CandidateReadSchema:
    """
        Update candidate

        - **first_name**: Candidate first name (str)
        - **last_name**: Candidate last name (str)
        - **email**: Candidate email (str)
        - **career_level**: Candidate career level (str)
        - **job_major**: Candidate job major (str)
        - **years_of_experience**: Candidate years of experience (int)
        - **degree_type**: Candidate degree type (str)
        - **skills**: Candidate skills (list)
        - **nationality**: Candidate's nationality (str)
        - **city**: Candidate's city (str)
        - **salary**: Candidate's salary (int)
        - **gender**: Candidate's gender (str)
    """

    document = candidates.find_one({"uuid": bson.Binary.from_uuid(uuid)})
    if document:
        document = candidate.dict()
        candidates.update_one({"uuid": bson.Binary.from_uuid(uuid)}, {"$set": document})
        return {"uuid": uuid, **document}
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": "Candidate not found"}
        )


@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_candidate(uuid: UUID, _ = Security(get_current_active_user)):
    """
        Delete candidate

        - **uuid**: Candidate UUID (str)
    """
    document = candidates.find_one_and_delete(filter={"uuid": bson.Binary.from_uuid(uuid)})
    if not document:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Candidate not found"}
        )


@router.get("/",)
async def get_candidates(_ = Security(get_current_active_user)) -> list[CandidateReadSchema]:
    """
        Get candidates
    """
    return list(candidates.find())

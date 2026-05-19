
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

from typing import Annotated
import secrets

from starlette.responses import FileResponse

security = HTTPBasic()

# correct credentials of user to gain access
def check_creds(credentials:HTTPBasicCredentials = Depends(security)):
    correct_username = "16295191"
    correct_password = "16295191"

      # check the values are correct
    user_correct = secrets.compare_digest(credentials.username, correct_username)
    pasw_correct = secrets.compare_digest(credentials.password, correct_password)

  #fallback for wrong answers
    if not (user_correct and pasw_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password - try again",
            headers={"WWW-Authenticate": "Basic"},
        )


    return credentials.username



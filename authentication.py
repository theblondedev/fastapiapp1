
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status

from typing import Annotated
import secrets

from starlette.responses import FileResponse

security = HTTPBasic()

# Function to verify authentication of user
def check_creds(credentials:HTTPBasicCredentials = Depends(security)):
    correct_username = "16295191"
    correct_password = "16295191"

    # The input credentials
 #  current_username = credentials.username.encode()
 #current_password = credentials.password.encode()

    # Now compare them with the "correct" values
    user_correct = secrets.compare_digest(credentials.username, correct_username)
    pasw_correct = secrets.compare_digest(credentials.password, correct_password)

    # Action to take if authentication fails - here raise an HTTP exception
    # with 401 status. This will result in the client asking again for credentials
    if not (user_correct and pasw_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password - try again",
            headers={"WWW-Authenticate": "Basic"},
        )


    return credentials.username

# Start the application and make it depend upon the successful
# completion of the check crecentials function


# All endpoints below require authentication
#@app.get("/")
#async def root():
 #   return {"message": "Hello World"}

#@app.get("/form1", response_class=FileResponse)
#async def form1():
 #   return 'static/form1.html'

#@app.get("/form2", response_class=FileResponse)
#async def form2():
  #  return 'static/form2.html'


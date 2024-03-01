from http.client import HTTPException
from fastapi import FastAPI, BackgroundTasks
import subprocess
import os

app = FastAPI()
process_ids = {}

@app.get("/generate-workload")
async def generate_workload(rate: int = 500, allocated_users: int = 250, duration: str = '60s'):
    k6_script_path = "/home//miketz/Desktop/Cloud_Orchestration/Load_Testing/script.js"
    allocated_users = 5000
    # Build the command to run k6 with your script
    command = ["k6", "run","-e", f"RATE={rate}","-e", f"PRE_ALLOCATED_VUS={allocated_users}", "-e", f"DURATION={duration}",k6_script_path]
    process = subprocess.Popen(command)
    process_id = process.pid

    return {"message": "Script is being executed in the background.", "process_id": process_id}
    
@app.get("/cancel-script")
async def cancel_script_endpoint(process_id: int):
    try:
        # Terminate the k6 process using the process ID
        os.kill(process_id, 15)  # Signal 15 is SIGTERM (terminate)
    except ProcessLookupError:
        pass  # Process has already terminated or doesn't exist
    return {"message": f"Canceling k6 script for {process_id}."}

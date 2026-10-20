import os
import time
import secrets
from typing import Any
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="GoldSniper 3R relay", version="0.1.0")
API_TOKEN = os.getenv("API_TOKEN", "")

# Development-only in-memory state. Restart loses commands and status.
_state: dict[str, Any] = {
    "connected": False,
    "last_seen": None,
    "account_mode": "DEMO",
    "symbol": "XAUUSD",
    "robot_enabled": False,
    "equity": None,
    "balance": None,
    "open_positions": [],
    "last_signal": "No signal reported",
}
_commands: list[dict[str, Any]] = []
_next_id = 1

def auth(authorization: str | None):
    if not API_TOKEN:
        raise HTTPException(503, "API_TOKEN is not configured")
    expected = f"Bearer {API_TOKEN}"
    if not authorization or not secrets.compare_digest(authorization, expected):
        raise HTTPException(401, "Unauthorized")

class CommandIn(BaseModel):
    action: str = Field(pattern="^(START|PAUSE_ENTRIES|RESUME_ENTRIES|CLOSE_ALL)$")
    created_at: float = Field(default_factory=time.time)

class StatusIn(BaseModel):
    connected: bool = True
    account_mode: str = "DEMO"
    symbol: str = "XAUUSD"
    robot_enabled: bool = False
    equity: float | None = None
    balance: float | None = None
    open_positions: list[dict[str, Any]] = []
    last_signal: str = "No signal reported"

@app.get("/health")
def health():
    return {"ok": True, "service": "GoldSniper 3R relay", "production_ready": False}

@app.get("/v1/status")
def get_status(authorization: str | None = Header(default=None)):
    auth(authorization)
    return _state

@app.post("/v1/status")
def update_status(body: StatusIn, authorization: str | None = Header(default=None)):
    auth(authorization)
    _state.update(body.model_dump())
    _state["last_seen"] = time.time()
    return {"ok": True}

@app.post("/v1/commands")
def create_command(body: CommandIn, authorization: str | None = Header(default=None)):
    global _next_id
    auth(authorization)
    command = {"id": _next_id, "action": body.action, "created_at": body.created_at, "claimed": False}
    _next_id += 1
    _commands.append(command)
    return {"ok": True, "command": command}

@app.get("/v1/commands/next")
def next_command(authorization: str | None = Header(default=None)):
    auth(authorization)
    for command in _commands:
        if not command["claimed"] and time.time() - command["created_at"] < 60:
            command["claimed"] = True
            return command
    return {"id": None, "action": "NONE"}

from fastapi import APIRouter

# Using relative dots (.) instead of 'app.api'
from .health import router as health_router
from .jobs import router as jobs_router
from .agents import router as agents_router
from .resume import router as resume_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(jobs_router, prefix="/v1/jobs", tags=["jobs"])
api_router.include_router(agents_router, prefix="/v1/agents", tags=["agents"])
api_router.include_router(resume_router, prefix="/v1/resume", tags=["resume"])

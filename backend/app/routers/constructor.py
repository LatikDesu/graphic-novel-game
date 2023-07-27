from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/constructor", tags=["constructor"])


@router.get("/", response_class=HTMLResponse)
async def render(request: Request):
    return templates.TemplateResponse("constructor.html", {"request": request, "id": 1})

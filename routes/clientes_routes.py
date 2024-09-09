from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from util.templates import obter_jinja_templates

router = APIRouter(prefix="/cliente")
templates = obter_jinja_templates("templates/cliente")

@router.get("/centroPessoal/perfil", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/perfil.html", {"request": request})

@router.get("/centroPessoal/contaalterarsenha", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/contaalterarsenha.html", {"request": request})

@router.get("/centroPessoal/contaalterarnome", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/contaalterarnome.html", {"request": request})

@router.get("/centroPessoal/contaalterardata", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/contaalterardata.html", {"request": request})

@router.get("/centroPessoal/contaalteraremail", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/contaalteraremail.html", {"request": request})

@router.get("/centroPessoal/enderecossalvos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/enderecossalvos.html", {"request": request})

@router.get("/centroPessoal/cartoescadastrados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/cartoescadastrados.html", {"request": request})


@router.get("/centroPessoal/todosospedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/todosospedidos.html", {"request": request})

@router.get("/centroPessoal/pedidosnaopagos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/pedidosnaopagos.html", {"request": request})

@router.get("/centroPessoal/processandopedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/processandopedidos.html", {"request": request})

@router.get("/centroPessoal/devolucaopedidos", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/devolucaopedidos.html", {"request": request})

@router.get("/centroPessoal/pedidosenviados", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("pages/centroPessoal/pedidosenviados.html", {"request": request})







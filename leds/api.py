from ninja import Router

router = Router()

@router.get("/")
def index(request):
    return { 'status': 'running'}

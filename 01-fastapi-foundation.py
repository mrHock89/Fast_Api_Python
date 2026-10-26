from fastapi import FastAPI
from fastapi import Request
import uvicorn

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal Api for managing orders."
        "Handle creation, tracking of delivery systems"
    ),
    version="1.1.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


@app.get("/")
def read_root():
    """Root endpoint - Health Check"""
    # FastAPI converts this dict into JSON
    return {"message": "Welcome to swiggy Order service", 
    "status": "healthy"}

@app.get("/about")
def about():
    """Return API metadata"""
    return {
        "service": "order-service",
        "team": "backend platform",
        "region": "app-south-1",
        "version": "1.2.2" 
    }

@app.get("/orders")
def list_orders():
    """List recent orders""" 
    return {
        "orders": [
            {"id": 1, "item": "Butter Dhosa", "status": "Delivered"},
            {"id": 2, "item": "Paneer Chicken", "status": "Preparing"},
            {"id": 3, "item": "Masala Dhosa", "status": "Delivered"}
        ]
    }

@app.get("/orders/status")
def order_status():
    """Get Order Status"""
    return {
        "total_today": 2_340_23,
        "top_city": "Mumbai"
    }


@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params),
    }

@app.get(
    "orders/active",
    summary="Get Active Orders",
    description=(
        "Returns all orders that are currently being prepared"
        "or are out for delivery"
    ),
    tags=["orders"],
    response_description="List of active order objects",
    deprecated=False
)
def get_active_order():
    """This doctring also apprears in docs"""
    return {
        "active_orders": [
            {"id": 1, "item": "Masala Chicken", "status": "Out_for_delivery"}
        ]
    }

@app.get("/restaurants", tags=["Restaurants"])
def list_restro():
    """Another docstring for another endpoint"""
    return {
        "restaaurants": [
            {"test": "test"}
        ]
    }

@app.get("/restaurants/delhi", tags=["Restaurants"])
def list_restro_delhi():
    """Another docstring for another endpoint"""
    return {
        "restaaurants": [
            {"test": "test"}
        ]
    }
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .models import models, schemas
from .controllers import orders, sandwiches, recipes, resources, order_details
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order


@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)
#----------------------------------------------------------------------------------------------------------
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwich"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwich.create(db=db, sandwich=sandwich)


@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwich"])
def read_sandwich(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)


@app.get("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich


@app.put("/sandwiches/{sandwich_id}", response_model=schemas.Sandwich, tags=["Sandwich"])
def update_one_sandwich(sandwich_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich.update(db=db, sandwich=sandwich, sandwich_id=sandwich_id)


@app.delete("/sandwiches/{sandwich_id}", tags=["Sandwich"])
def delete_one_sandwich(sandwich_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, sandwich_id=sandwich_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="User not found")
    return sandwich.delete(db=db, sandwich_id=sandwich_id)
#----------------------------------------------------------------------------------------------------------
@app.post("/resources/", response_model=schemas.Sandwich, tags=["Resource"])
def create_resources(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resource.create(db=db, resource=resource)


@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resource"])
def read_resource(db: Session = Depends(get_db)):
    return resources.read_all(db)


@app.get("/resources/{resource_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_resource(resources_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resources_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource


@app.put("/resources/{resources_id}", response_model=schemas.Sandwich, tags=["Resources"])
def update_one_resource(resources_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resources_id=resources_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.update(db=db, resources=resources, resourceid=resources_id)


@app.delete("/resources/{resource_id}", tags=["Resources"])
def delete_one_resource(resources_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resources_id=resources_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="User not found")
    return resource.delete(db=db, resource_id=resources_id)
#-------------------------------------------------------------------------------------------------
@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipe"])
def create_recipe(resource: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipes=recipes)


@app.get("/recipes/", response_model=list[schemas.Recipe], tags=["Recipe"])
def read_recipe(db: Session = Depends(get_db)):
    return recipes.read_all(db)


@app.get("/recipes/{recipes_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipes_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipes_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe


@app.put("/recipes/{recipes_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(recipes_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, recipes_id=recipes_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.update(db=db, recipe=recipe, recipes_id=recipes_id)


@app.delete("/recipes/{recipe_id}", tags=["Recipe"])
def delete_one_recipe(recipes_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipes_id=recipes_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="User not found")
    return recipe.delete(db=db, recipes_id=recipes_id)
#-------------------------------------------------------------------------------------------------
@app.post("/order_details/", response_model=schemas.OrderDetail, tags=["Order_Details"])
def create_order_details(resource: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details.create(db=db, order_details=order_details)


@app.get("/order_details/", response_model=list[schemas.OrderDetail], tags=["Order_Details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details.read_all(db)


@app.get("/order_details/{order_details_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_order_details(order_details_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_details_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail


@app.put("/order_details/{order_details_id}", response_model=schemas.OrderDetail, tags=["Order_Details"])
def update_one_order_details(order_details_id: int, recipe: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    order_details_db = order_details.read_one(db, order_details_id=order_details_id)
    if order_details_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_details.update(db=db, order_details=order_details, order_details_id=order_details_id)


@app.delete("/order_details/{order_details_id}", tags=["Order Details"])
def delete_one_order_details(order_details_id: int, db: Session = Depends(get_db)):
    order_detail = order_details.read_one(db, order_details_id=order_details_id)
    if order_detail is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order_detail.delete(db=db, order_details_id=order_details_id)
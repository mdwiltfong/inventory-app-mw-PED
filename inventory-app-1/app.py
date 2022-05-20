from flask import Flask, request, render_template,flash,redirect
from sqlalchemy.exc import IntegrityError
from models import Item, ItemWarehouse, db, connect_db,Warehouse
from forms import CreateAssignment, CreateItem, CreateWarehouse, EditAssignment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']="it's a secret"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory-app-test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['WTF_CSRF_ENABLED'] = False
connect_db(app)
db.create_all()
@app.route('/')
def load_index():
    """ Returns homepage"""
    #all_items=db.view_all_items(db_name)
    items=Item.query.all()
    warehouses=Warehouse.query.all()
    return render_template("index.html", items=items,warehouses=warehouses)

@app.route('/create_item', methods=["POST","GET"])
def create_item():
    """Creates inventory item"""
    try:
            form=CreateItem()
            warehouses=Warehouse.query.all()
            form.warehouse_id.choices=[(w.name) for w in warehouses]
            if form.validate_on_submit():
                new_item = Item(name=form.name.data,
                                    price=form.price.data,
                                    quantity=form.quantity.data,
                                    sku=form.sku.data,
                                    warehouse_id=form.warehouse_id.data
                               )
                db.session.add(new_item)
                db.session.commit()
                flash('Item Created',"success")
                return redirect('/')  
    except IntegrityError:
            flash("SKU already exists","danger")
            return redirect('/')
          
    return render_template('create_item_form.html',form=form,warehouses=warehouses)
@app.route('/create_warehouse', methods=["POST","GET"])
def create_warehouse():
    """Creates Warehouse Location"""
    try:  
      form=CreateWarehouse()
      if form.validate_on_submit():
          new_warehouse = Warehouse(name=form.name.data)
          db.session.add(new_warehouse)
          db.session.commit()
          flash('Warehouse Created',"success")
          return redirect('/')
    except IntegrityError:
      flash("Warehouse Already Exists","danger")
      return redirect('/')
    
    return render_template('create_warehouse_form.html',form=form)
@app.route('/edit_item/<int:sku>/edit',methods=['GET','POST'])
def edit_item(sku):
  item=Item.query.get_or_404(sku)
  form=CreateItem(obj=item) 
  
  warehouses=Warehouse.query.all()
  form.warehouse_id.choices=[(w.name) for w in warehouses]
  form.warehouse_id.default=item.warehouse_id
  if form.validate_on_submit():
    item.name=form.name.data
    item.price=form.price.data
    item.quantity=form.quantity.data
    item.sku=form.sku.data
    item.warehouse_id=form.warehouse_id.data
    db.session.commit()    
    flash(f"Item {id} updated!","success")
    return redirect('/')

  else:
    return render_template("edit_item_form.html", form=form,item=item)

@app.route('/view_inventory/<int:sku>',methods=['GET','POST'])
def view_inventory(sku):
    item=Item.query.get_or_404(sku)
    return render_template("view_inventory.html",item=item)
@app.route('/edit_inventory/<int:sku>/<warehouse>',methods=['GET','POST'])
def edit_inventory(sku,warehouse):
    assignment=ItemWarehouse.query.filter(ItemWarehouse.items_sku ==sku, ItemWarehouse.warehouse_name==warehouse).first()
    form=EditAssignment(obj=assignment)
    warehouses=Warehouse.query.all()
    form.warehouse_name.choices=[(w.name) for w in warehouses]
    if form.validate_on_submit():
          assignment.items_sku=form.items_sku.data
          assignment.warehouse_name=form.warehouse_name.data
          assignment.quantity=form.quantity.data
          db.session.commit()    
          flash(f"Item {sku}'s inventory was updated!","success")
          return redirect(f'/view_inventory/{assignment.items_sku}')
    else:
        return render_template("edit_inventory_form.html",form=form,assignment=assignment)

@app.route('/assign_inventory/<int:sku>',methods=['GET','POST'])
def assign_inventory(sku):
      item=Item.query.get_or_404(sku)
      form=CreateAssignment()
      warehouses=Warehouse.query.all()
      form.warehouse_name.choices=[(w.name) for w in warehouses]
      if form.validate_on_submit():
          item.assignments.append(ItemWarehouse(warehouse_name=form.warehouse_name.data, quantity=form.quantity.data))
          db.session.commit()    
          flash(f"Item {sku}'s inventory was assigned!","success")
          return redirect(f'/view_inventory/{item.sku}')
      else:
          return render_template("edit_inventory_form.html",form=form,item=item)

@app.route('/delete_item/<int:id>',methods=['GET','POST'])
def delete_item(id):
  Item.query.filter_by(id=id).delete()
  db.session.commit()
  flash(f"Item {id} deleted!","success")
  return redirect('/')
    
# Makes sure this is the main process
"""app.run(
  host = "0.0.0.0", # or 127.0.0.1
  port = 8080, # make sure this is a non privileged port
  debug = True # this will allow us to easily fix problems and bugs
)"""
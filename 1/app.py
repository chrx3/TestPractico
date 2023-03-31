from flask import Flask, request
from flask_restful import Resource, Api, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#conexion a base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prod.db'
db = SQLAlchemy(app)

app.app_context().push()

#modelo base de datos
class Productos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)

    def __repr__(self):
        return self.name


prodFields = {
    'id':fields.Integer,
    'name':fields.String
}

#endpoints
class productos(Resource):
    @marshal_with(prodFields)
    #get de todos los elementos
    def get(self):
        prods = Productos.query.all()
        return prods

    @marshal_with(prodFields)
    def post(self):
        data = request.json
        prod = Productos(name=data['name'])
        db.session.add(prod)
        db.session.commit()

        prods = Productos.query.all()
        return prods

class producto(Resource):
    @marshal_with(prodFields)
    #get por id
    def get(self, id):
        prod = Productos.query.filter_by(id=id).first()
        return prod

    @marshal_with(prodFields)
    def put(self, id):
        data = request.json
        prod = Productos.query.filter_by(id=id).first()
        prod.name = data['name']
        db.session.commit()
        return prod

    @marshal_with(prodFields)
    def delete(self,id):
        prod = Productos.query.filter_by(id=id).first()
        db.session.delete(prod)
        db.session.commit()
        prods = Productos.query.all()
        return prods

# urls para llamar a la api
api.add_resource(productos,'/')
api.add_resource(producto,'/<int:id>')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
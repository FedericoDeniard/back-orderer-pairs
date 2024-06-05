from flask import Flask, request, jsonify
from flask_cors import CORS
from Packages.Package_Pairs.Pairs import *

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def get_data():
    data = request.json
    print(data)
    A: list = data["firstSet"]
    B: list = data["secondSet"]
    equation: str = data["equation"]
    operation = data["operation"]
    operation = int(operation)
    match operation:
        case 1:
            product: list = multiply_sets(A,B)
            relation: list = relationship(A,B,equation)
            relation_matrix: list = relationship_matrix(A,B,product,relation)
            domain: set = list(get_domain(product))
            range_set: set = list(get_range(product))
            property = ""
        case 2:
            product: list = multiply_sets(B,A)
            relation: list = relationship(B,A,equation)
            relation_matrix: list = relationship_matrix(B,A,product,relation)
            domain: set = list(get_domain(product))
            range_set: set = list(get_range(product))
            property = ""
        case 3:
            product: list = multiply_sets(A,A)
            relation: list = relationship(A,A,equation)
            relation_matrix: list = relationship_matrix(A,A,product,relation)
            domain: set = list(get_domain(product))
            range_set: set = list(get_range(product))
            property = relation_properties(A,relation)
        case 4:
            product: list = multiply_sets(B,B)
            relation: list = relationship(B,B,equation)
            relation_matrix: list = relationship_matrix(B,B,product,relation)
            domain: set = list(get_domain(product))
            range_set: set = list(get_range(product))
            property = relation_properties(B,relation)
    final_message = {"product": product,"relation": relation,"matrix": relation_matrix,"domain": domain,"range": range_set, "property": property}

    return jsonify(final_message), 200

if __name__ == '__main__':
    app.run()

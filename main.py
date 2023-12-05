from flask import Blueprint, Flask

from rfm_score import rfm_score_analysis
from utils.auth import authorization
from utils.helper import CustomerNotFoundErr, ValueNotFoundErr
from utils.routes import routes

app = Flask(__name__)
main = Blueprint('main', __name__)
app.register_blueprint(main)

@app.route("/")
def rfm():
    return "<p>OK</p>"


@app.route(routes['rfm_score'])
@authorization
def rfm_score_status(customer_id):
    result = {"result": {"rfm_score": None}}
    try:
        customer_id = int(customer_id)
        result["result"]["rfm_score"] = rfm_score_analysis(customer_id=customer_id)

    except CustomerNotFoundErr:
        return 'Customer was not Found.', 404

    except ValueNotFoundErr:
        return 'RFM was not Found.', 404

    except FileNotFoundError:
        return "Dataset was not found.", 404

    except Exception as err:
        return err, 500

    return result, 200

if __name__ == "__main__":
    app.run()

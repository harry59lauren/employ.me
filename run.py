from app import create_app
from app.models import db

app = create_app()

app.run(host='0.0.0.0', port=8080, debug=True)

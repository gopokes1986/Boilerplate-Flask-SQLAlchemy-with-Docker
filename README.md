# Flask-SQLAlchemy-Backbone-with-Docker

This is a base template of Flask application containerized using Docker.

The Flask application have a base template to connect to Sqlalchemy back-end and it also has the base template for Blueprint too.

Without Docker:
1. Pull from <code>flask_with_sqlalchemy_backbone</code> branch
2. Modify configurations in <code>app/app_config.py</code>
3. Run <code>db_setup.py</code> to create the database
4. Run <code>run.py</code>

With Docker:
1. Pull from <code>master</code>
1. Modify configurations in <code>app/app_config.py</code>
2. Run <code>db_setup.py</code> to create the database
3. Modify Dockerfile if necessary (the default should work fine in most cases)
4. Run <code>docker build -t flask_image:0.1 .</code>
5. Run <code>docker run --name flask_container -d -p 5000:5000 flask_image:0.1</code>



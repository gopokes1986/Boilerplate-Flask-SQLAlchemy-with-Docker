# Boilerplate-Flask-SQLAlchemy-with-Docker

This is a base template of Flask application containerized using Docker.

The Flask application have a base template to connect to Sqlalchemy back-end and it also has the base template for Blueprint too.

Without Docker:
1. Pull from <code>flask_with_sqlalchemy_backbone</code> branch
2. Modify configurations in <code>app/app_config.py</code>
3. Run <code>pip3 install requirements.txt</code>
4. Run <code>db_setup.py</code> to create the database
5. Run <code>run.py</code>

With Docker:
1. Pull from <code>master</code>
2. Modify configurations in <code>app/app_config.py</code>
3. Run <code>db_setup.py</code> to create the database
4. Modify Dockerfile if necessary (the default should work fine in most cases)
5. Run <code>docker build -t flask_image:0.1 .</code>
6. Run <code>docker run --name flask_container -d -p 5000:5000 flask_image:0.1</code>
7. Check logs using <code>docker logs -ft flask_container</code>

Tips:
1. The local database hostname should be your ip address. (not localhost)
2. The local database port should be 3306

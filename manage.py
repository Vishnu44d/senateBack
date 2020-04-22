import click
import jwt
import os

@click.group()
def cli():
    '''Welcome the to cli for managing Server'''
    pass

@click.command()
@click.option('--name', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True)
def addadmin(name, email, password):
    "Seed Admin data for testing"
    from server import SQLSession
    from senateBack.models.userModel import User
    import datetime
    import uuid

    session = SQLSession()
    admin = User(
        email=email,
        public_id=str(uuid.uuid4()),
        username=name,
        password=password,
        registered_on=datetime.datetime.utcnow(),
        last_updated_on=datetime.datetime.utcnow(),
        admin=True,
        varified=True,
        maintainer=True
    )
    try:
        session.add(admin)
        session.commit()
        session.close()
        api_key = jwt.encode({'email': admin.email, 'exp':datetime.datetime.utcnow() + datetime.timedelta(days=400)}, os.environ.get('SECRET_KEY')).decode('UTF-8')
        print("API_KEY: ", api_key)
    except Exception as e:
        print("err in creating admin")
        print(str(e))

@click.command()
@click.option('--email', prompt=True)
@click.option('--password', prompt=True)
def token(email, password):
    from senateBack.auth.auth import get_token
    data = {
        "email": email,
        "password": password
    }
    response, response_code = get_token(data)
    if(response_code==200):
        print(response['token'])
    else:
        print(response['message'])

@click.command()
def initdb():
    from server import engine, createTables
    createTables(engine)
    click.echo('Initialized the database')

@click.command()
def dropdb():
    from server import engine, destroyTables
    destroyTables(engine)
    click.echo('Dropped the database')

# @click.command()
# def admin():
#     addadmin()
#     click.echo('Admin added')

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(addadmin)
cli.add_command(token)


if __name__ == '__main__':
    cli()

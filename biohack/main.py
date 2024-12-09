import typer

app = typer.Typer()


@app.command()
def hello():
    print("Hello")


@app.command()
def bye():
    print("Bye")


if __name__ == "__main__":
    app()

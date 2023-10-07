import click


@click.group()
def main():
    pass


@main.command()
@click.option("--a", prompt="Hi friend. What's your name? ", type=str)
def say_hi(a):
    value = a
    click.echo(" Nice to meet you, {}".format(value))


if __name__ == "__main__":
    main()
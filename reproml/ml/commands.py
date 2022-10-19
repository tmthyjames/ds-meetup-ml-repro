import click


@click.group()
@click.option(
    "-r",
    "--rank",
    help="func for matching cities to preferences",
    default=[],
    multiple=True,
)
def ml(**kwargs) -> None:
    pass


@ml.command(help="Extract similarity data via Spark.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the census pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def match(**kwargs):
    pass

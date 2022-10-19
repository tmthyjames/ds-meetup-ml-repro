import click


@click.group(invoke_without_command=True)
def etl(**kwargs):
    pass


@etl.command(help="Run all jobs")
def run(**kwargs) -> None:
    from reproml.etl.census import run_census
    from reproml.etl.economic import run_economic

    run_census(**kwargs)
    run_economic(**kwargs)


@etl.command(help="run the lyrics data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the lyrics pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def lyrics(steps, **kwargs) -> None:
    from reproml.etl.lyrics import process_lyrics, run_lyrics

    path = run_lyrics()
    process_lyrics(path)


@etl.command(help="Run the economic data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the economic pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def economic(steps, **kwargs) -> None:
    from reproml.etl.economic import run_economic

    run_economic(steps=steps, **kwargs)


@etl.command(help="Run the employment data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the employment pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def employment(steps, **kwargs) -> None:
    from reproml.etl.employment import run_employment

    run_employment(steps=steps, **kwargs)


@etl.command(help="Run the environment data jobs.")
@click.option(
    "-s",
    "--steps",
    help="Specify which steps to run in the environment pipeline",
    default=["extract", "transform", "load"],
    multiple=True,
)
def environment(steps, **kwargs) -> None:
    pass
    # from reproml.etl.employment import run_employment

    # run_employment(steps=steps, **kwargs)

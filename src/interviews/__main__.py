"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """My Interviews Python."""


if __name__ == "__main__":
    main(prog_name="my-interviews-python")  # pragma: no cover

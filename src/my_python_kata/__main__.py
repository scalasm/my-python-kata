"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """My Python Kata."""
    print("My Python Kata - sorry, no CLI!")


if __name__ == "__main__":
    main(prog_name="my-python-kata")  # pragma: no cover

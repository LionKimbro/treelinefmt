
import inject.args as args
import inject.inject as inject


def run():
    args.readargs()
    inject.run()


if __name__ == "__main__":
    run()

